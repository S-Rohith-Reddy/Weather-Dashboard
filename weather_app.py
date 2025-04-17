from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

API_KEY = "d4e052e76fa446662fb61eb06404f282"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return None

    # Get timezone offset in seconds
    timezone_offset = data["timezone"]
    utc_time = datetime.utcnow()
    local_time = utc_time + timedelta(seconds=timezone_offset)

    # Convert to IST if country is India
    if data["sys"]["country"] == "IN":
        ist = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(ist)

    # Rain data (may be missing)
    rain = data.get("rain", {}).get("1h", 0)

    weather_info = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "rain": rain,
        "description": data["weather"][0]["description"].capitalize(),
        "icon": data["weather"][0]["icon"],
        "local_time": local_time.strftime("%Y-%m-%d %H:%M:%S"),
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"]
    }

    return weather_info

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather_data(city)
    return render_template("index.html", weather=weather)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

