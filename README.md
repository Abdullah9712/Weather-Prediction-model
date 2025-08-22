# 🌦️ AI Weather & Chat Assistant
 
An interactive **Streamlit web app** that provides **real-time weather updates** for any city worldwide and answers general chat queries using the **LLaMA3-8B-8192 LLM** (served via **Groq API**).  

## **Features**

- Fetches **real-time weather data** using the **OpenWeather API**.  
- Generates **friendly, human-readable weather reports** in 4–5 sentences using **LLaMA3-8B-8192 (via Groq API)**.  
- Handles **general chat queries** using the same LLM.  
- Clean separation of **API keys** using `.env` for security.  
- User-friendly interface built with **Streamlit**.  

## **Demo**

Here are some screenshots of the AI Weather & Chat Assistant in action:  
![Weather report example](images/Image1.png)  
![Temperature Forecast example](images/Image2.png)  

## **Prerequisites**

- **Python 3.12** installed (recommended).  
- **OpenWeather API key** → Get one from **[openweathermap.org/api](https://openweathermap.org/api)**.  
- **Groq API key** → Generate one at **[console.groq.com/keys](https://console.groq.com/keys)**.  
- **Git** installed → Download from **[git-scm.com](https://git-scm.com/)**.

- **Python dependencies** (installed via `requirements.txt`):  

  - Streamlit  
  - Requests  
  - Groq Python SDK  
  - python-dotenv  

## **Setup**

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/weather-chat-assistant.git
cd weather-chat-assistant

# 2. Create a virtual environment (Python 3.12)
# On Windows:
py -3.12 -m venv venv
# On Mac/Linux:
python3.12 -m venv venv

# 3. Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up environment variables
# Create a `.env` file in the project root and add the following:
OPENWEATHER_API_KEY=your_openweather_key_here  
GROQ_API_KEY=your_groq_key_here                 
```

## **Usage**

1. Run the Streamlit app:
```bash
   streamlit run "weather model/app.py"
```
2. Open the URL shown in your terminal (usually `http://localhost:8501`) in a browser.  

3. Type a query in the input box:

   - Weather query:  
     What is the weather in London today?

   - General chat query:  
     Tell me a fun fact about space.

4. Click **Ask** to get the AI-generated response.

## **Project Structure**
AI-Weather-Chat-Assistant/
├─ app.py            # Streamlit app
├─ utils.py          # Functions for weather fetching & LLM
├─ requirements.txt  # Python dependencies
├─ README.md         # Project documentation
├─ .gitignore        # Files to ignore in git
├─ .env              # To store secrets API keys
├─ images/           # Images
│ ├─ Image1.png
│ └─ Image2.png

## **Future Improvements**

- Add **voice input & output** so users can speak their queries and get audio weather reports.  
- Integrate **severe weather alerts & notifications** for storms, rain, or heatwaves.  
- Provide **historical weather data** for a specific date or comparison over time.  
- Display **interactive maps** with weather overlays (temperature, clouds, rain).  
- Give **weather-based suggestions** like clothing or activity recommendations.  
- Allow users to **save favorite cities** for quick daily weather updates.  
- Enhance **chat features** with weather-based jokes, trivia, or fun facts.  
- Show **graphical trends** of temperature, humidity, or precipitation for the past week.  
- Integrate with **Google Calendar** to plan events based on the forecast.  
- Add **multi-language support** for weather reports and chat responses.  

## **Contact**

Created by Muhammad Abdullah  
📧 Email: abdullah2648.khan@gmail.com  
📞 Phone: +92-319-9539210  

