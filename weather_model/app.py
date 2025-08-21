import streamlit as st
import pandas as pd
import plotly.express as px
from utils import weather_chat, get_weather

st.set_page_config(page_title="AI Weather & Chat Assistant", layout="wide")
st.title("🌦️ AI Weather & Chat Assistant")

# --- User Inputs ---
query = st.text_input("Ask me anything (e.g., 'What is the weather of New York today?')")
units = st.radio("Select unit", ("Celsius", "Fahrenheit"))
days = st.slider("Forecast days", 1, 5, 3)

# --- Handle Button Click ---
if st.button("Ask") and query:
    response = weather_chat(query, units="metric" if units=="Celsius" else "imperial", days=days)
    st.write(f"Here’s your weather update 🌤️:\n\n{response}")

    # Optional: display chart for temperature forecast
    # Get city from query (same logic as utils)
    skip_words = {"what", "is", "the", "weather", "of", "today", "in", "at", "like", "for"}
    words = query.replace("?", "").split()
    city = " ".join([word for word in words if word.lower() not in skip_words])
    
    if city:
        data = get_weather(city, units="metric" if units=="Celsius" else "imperial", days=days)
        forecast = data.get("forecast", {})
        if forecast and "list" in forecast:
            # Process forecast into daily average
            df = pd.DataFrame(forecast["list"])
            df["dt_txt"] = pd.to_datetime(df["dt_txt"])
            df["temp"] = df["main"].apply(lambda x: x["temp"])
            df_daily = df.groupby(df["dt_txt"].dt.date)["temp"].mean().reset_index()
            fig = px.line(df_daily, x="dt_txt", y="temp", labels={"dt_txt":"Date", "temp":f"Temperature ({'°C' if units=='Celsius' else '°F'})"}, title=f"{city} Temperature Forecast")
            st.plotly_chart(fig)
