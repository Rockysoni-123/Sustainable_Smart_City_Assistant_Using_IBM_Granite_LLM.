import json
from datetime import datetime
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import Credentials

# --- Configuration ---
MODEL_ID = "granite-13b-chat-v1"  # or use other Granite models available to you
PROJECT_ID = "your-watsonx-project-id"
API_KEY = "your-ibm-cloud-api-key"
REGION = "us-south"  # or "eu-de", etc.

# --- Connect to IBM Granite LLM ---
def initialize_granite_model():
    credentials = Credentials(api_key=API_KEY, url=f"https://{REGION}.ml.cloud.ibm.com")
    model = Model(model_id=MODEL_ID, project_id=PROJECT_ID, credentials=credentials)
    return model

# --- Generate Report Prompt ---
def generate_prompt(city_name, sustainability_data):
    return f"""
You are an AI assistant that creates sustainability reports for smart cities.
Generate a detailed sustainability performance summary for {city_name} using the data below.

Data:
{json.dumps(sustainability_data, indent=2)}

Include the following in your report:
- Overview of key sustainability metrics
- Notable improvements or concerns
- Suggestions for optimization
- Overall sustainability rating (Low/Medium/High)

The report should be in clear, professional language suitable for city council presentation.
"""

# --- Generate Report ---
def generate_sustainability_report(city_name, sustainability_data):
    model = initialize_granite_model()
    prompt = generate_prompt(city_name, sustainability_data)

    response = model.generate(prompt=prompt)
    return response['generated_text']

# --- Example Input Data (Replace with sensor feed or database) ---
example_data = {
    "energy_consumption": "22% lower than previous year",
    "renewable_energy_use": "65% of total city energy",
    "air_quality_index": 42,
    "water_consumption": "Average 120 liters per person/day",
    "waste_recycling_rate": "74%",
    "public_transport_uptake": "38% increase",
    "smart_traffic_management": "Reduced congestion by 30%"
}

# --- Run Main ---
if __name__ == "__main__":
    city = "Greenfield Smart City"
    print(f"\nGenerating sustainability report for {city}...\n")
    report = generate_sustainability_report(city, example_data)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"sustainability_report_{city.replace(' ', '_')}_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(report)

    print(f"Report saved to {filename}\n")
    print("----- Report Preview -----\n")
    print(report[:1000])  # Print preview of report
