# services/utilities.py

def get_utility_status():
    print("\n[City Utilities Service]")
    # Simulated utility status (could be connected to city dashboards or open data)
    utilities = {
        "Electricity": "No outages reported",
        "Water Supply": "Scheduled maintenance in District 4 at 2 PM",
        "Waste Collection": "Running on schedule"
    }
    for utility, status in utilities.items():
        print(f"- {utility}: {status}")
