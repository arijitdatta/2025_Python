from weather import get_outdoor_weather
from indoorSensorReader import read_sensor_data
import time
from decision_engine import decide
from logger import init_log, log_decision
from feedback import get_feedback

print("Starting Home Weather Decision System...")

# Initialize log file
init_log()

last_weather_fetch = 0
weather_cache = None
WEATHER_REFRESH_INTERVAL = 3600  # 1 hour

last_decision_time = 0
DECISION_INTERVAL = 600  # 10 minutes

doors_open = True   # change manually if needed

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

        # Run decision only every 10 minutes
        if (current_time - last_decision_time) >= DECISION_INTERVAL:

            print("\n--- INPUT DATA ---")
            print("Indoor:", indoor)
            print("Outdoor:", outdoor)

            action = decide(indoor, outdoor, doors_open)

            print("--- SYSTEM DECISION ---")
            print(action)

            # Get user feedback (HITL)
            feedback = get_feedback()

            # Log decision + feedback
            log_decision(indoor, outdoor, action, feedback)

            last_decision_time = time.time()

    except Exception as e:
        print("Error:", e)