import csv
import os
import time

LOG_FILE = "decision_log.csv"


def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "indoor_temp",
                "indoor_humidity",
                "outdoor_temp",
                "outdoor_humidity",
                "wind_dir",
                "mode",
                "open_windows",
                "user_feedback"
            ])


def log_decision(indoor, outdoor, action, feedback):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            time.strftime("%Y-%m-%d %H:%M:%S"),
            indoor["temp"],
            indoor["humidity"],
            outdoor["temp"],
            outdoor["humidity"],
            outdoor["wind_dir"],
            action["mode"],
            ",".join(action["open"]),
            feedback
        ])