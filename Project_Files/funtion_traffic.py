# services/traffic.py

def get_traffic_update():
    print("\n[Traffic Service]")
    # Simulate traffic data (replace with a real API like TomTom, HERE, or Google Maps)
    traffic_data = {
        "Main Street": "Heavy congestion",
        "Highway 101": "Flowing smoothly",
        "City Center": "Accident reported, 15-minute delay"
    }
    for location, status in traffic_data.items():
        print(f"- {location}: {status}")
