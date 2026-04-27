import serial
import re
from datetime import datetime

SERIAL_PORT = "/dev/cu.usbserial-0001"  # change for Mac: /dev/cu.usbserial-xxxx
BAUD = 115200

ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)

def parse_line(line):
    # Example: Temp: 32.5 °C | Humidity: 78.2
    match = re.search(r"Temp:\s*([\d.]+).*Humidity:\s*([\d.]+)", line)
    if match:
        temp = float(match.group(1))
        hum = float(match.group(2))

        return {
            "timestamp": datetime.now(),
            "temp": temp,
            "humidity": hum
        }
    return None


def read_sensor_data():
    """
    Read a single sensor reading from the serial port.
    Returns parsed data dict or None if no valid data received.
    """
    raw = ser.readline().decode("utf-8", errors="ignore").strip()

    if not raw:
        return None

    return parse_line(raw)