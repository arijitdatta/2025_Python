from weather import get_outdoor_weather
from indoorSensorReader import read_sensor_data
import time
from decision_engine import decide


print("Starting Home Weather Decision System...")

last_weather_fetch = 0
weather_cache = None
WEATHER_REFRESH_INTERVAL = 3600  # seconds (1 hour)

while True:
    try:
        indoor_data = read_sensor_data()

        if not indoor_data:
            continue

        indoor = {
            "temp": indoor_data["temp"],
            "humidity": indoor_data["humidity"]
        }

        current_time = time.time()

        # Refresh weather only once per hour
        if (current_time - last_weather_fetch) > WEATHER_REFRESH_INTERVAL or weather_cache is None:
            weather_cache = get_outdoor_weather()
            last_weather_fetch = current_time

        outdoor = weather_cache

        print("\n--- INPUT DATA ---")
        print("Indoor:", indoor)
        print("Outdoor:", outdoor)

        action = decide(indoor, outdoor)

        print("--- SYSTEM DECISION ---")
        print(action)

    except Exception as e:
        print("Error:", e)