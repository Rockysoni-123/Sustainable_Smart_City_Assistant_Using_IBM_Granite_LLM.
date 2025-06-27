# services/transport.py

def get_transport_info():
    print("\n[Public Transport Service]")
    # Simulate public transport data (could be tied to real-time GTFS APIs)
    transport_info = {
        "Metro Line 2": "Arriving in 5 minutes",
        "Bus 45": "Delayed by 10 minutes",
        "Tram 7": "On schedule"
    }
    for line, status in transport_info.items():
        print(f"- {line}: {status}")
