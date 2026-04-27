import subprocess
import re
import json
import os
import ipaddress
from concurrent.futures import ThreadPoolExecutor

DEVICE_FILE = "known_devices.json"
SUBNET = "192.168.1.0/24"

def load_known_devices():
    if os.path.exists(DEVICE_FILE):
        with open(DEVICE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_known_devices(devices):
    with open(DEVICE_FILE, "w") as f:
        json.dump(devices, f, indent=4)

def ping(ip):
    subprocess.run(
        ["ping", "-c", "1", "-W", "1", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def populate_arp():
    print("Triggering ARP table population...")
    network = ipaddress.ip_network(SUBNET)

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(ping, network.hosts())

def get_arp_table():
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    return result.stdout

def parse_arp(arp_output):
    devices = []
    lines = arp_output.split("\n")

    for line in lines:
        match = re.search(r'\((.*?)\) at ([0-9a-f:]+)', line)
        if match:
            ip = match.group(1)
            mac = match.group(2)

            # Ignore broadcast + multicast
            if mac == "ff:ff:ff:ff:ff:ff":
                continue
            if ip.startswith("224."):
                continue

            devices.append((ip, mac))

    return devices

def main():
    known_devices = load_known_devices()

    populate_arp()
    arp_output = get_arp_table()
    devices = parse_arp(arp_output)

    print("\nConnected Devices:\n")

    for ip, mac in devices:
        if mac not in known_devices:
            print(f"New device detected: {mac} (IP: {ip})")
            name = input("Assign a name to this device: ")
            known_devices[mac] = name
            save_known_devices(known_devices)

        print(f"{known_devices.get(mac, 'Unknown')} | IP: {ip} | MAC: {mac}")

    print("\nScan complete.\n")

if __name__ == "__main__":
    main()