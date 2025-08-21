import os
import requests
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not OPENWEATHER_API_KEY or not GROQ_API_KEY:
    raise RuntimeError(
        "Missing API keys. Set OPENWEATHER_API_KEY and GROQ_API_KEY in your .env file."
    )

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def get_weather(city, units="metric", days=3):
    """Fetch weather data from OpenWeather API (current + forecast)"""
    # Convert units for OpenWeather
    if units == "metric":
        unit_param = "metric"
    else:
        unit_param = "imperial"

    # Handle multi-word city names
    city_encoded = city.replace(" ", "%20")
    # Current weather
    current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={OPENWEATHER_API_KEY}&units={unit_param}"
    current_resp = requests.get(current_url)

    if current_resp.status_code != 200:
        return {"error": f"Could not fetch weather for '{city}'. Check city name."}

    current_data = current_resp.json()

    # Forecast (OpenWeather 5-day / 3-hour interval)
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_encoded}&appid={OPENWEATHER_API_KEY}&units={unit_param}"
    forecast_resp = requests.get(forecast_url)
    forecast_data = forecast_resp.json() if forecast_resp.status_code == 200 else {}

    return {
        "city": city,
        "current": {
            "description": current_data["weather"][0]["description"].title(),
            "temp": current_data["main"]["temp"],
            "feels_like": current_data["main"]["feels_like"],
            "humidity": current_data["main"]["humidity"],
            "icon": current_data["weather"][0]["icon"]
        },
        "forecast": forecast_data,  # raw forecast; can be processed later
        "units": "°C" if units == "metric" else "°F"
    }


def weather_chat(query, units="metric", days=3):
    """Decide if query is about weather or normal chat"""
    if "weather" in query.lower():
        # Extract city from query (skip common words)
        skip_words = {"what", "is", "the", "weather", "of", "today", "in", "at", "like", "for"}
        words = query.replace("?", "").split()
        city = " ".join([word for word in words if word.lower() not in skip_words])

        if city:
            weather_data = get_weather(city, units=units, days=days)
            if "error" in weather_data:
                return weather_data["error"]

            current = weather_data["current"]
            prompt = f"""
            The user asked: "{query}"

            Weather data for {city}:
            - Condition: {current['description']}
            - Temperature: {current['temp']}{weather_data['units']}
            - Feels like: {current['feels_like']}{weather_data['units']}
            - Humidity: {current['humidity']}%

            Write a clear and friendly weather report in 4–5 sentences.
            Start exactly like: "The weather in {city} is ..."
            Include condition, temperature, feels-like, and humidity.
            Explain briefly how it may feel outside (e.g., hot, sticky, breezy, pleasant).
            Do not add greetings or unrelated stories.
            """

            chat_completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}]
            )
            return chat_completion.choices[0].message.content.strip()

    # Fallback to normal chat
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": query}]
    )
    return chat_completion.choices[0].message.content.strip()
