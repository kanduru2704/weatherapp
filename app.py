from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔑 Replace this with your OpenWeather API key
API_KEY = "YOUR_OPENWEATHER_API_KEY"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"].capitalize()
                }
            else:
                error = "City not found. Please try again."
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
