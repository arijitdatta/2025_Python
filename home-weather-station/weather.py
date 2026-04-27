import requests
from config import API_KEY, CITY

def get_outdoor_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    print("Requesting:", url)

    response = requests.get(url, timeout=5)

    print("Status:", response.status_code)
    print("Response text:", response.text)

    data = response.json()

    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_dir": data["wind"]["deg"]
    }