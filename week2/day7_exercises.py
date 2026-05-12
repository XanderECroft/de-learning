# JSON round-trip
import json
import csv
from datetime import datetime
from pathlib import Path
import urllib.request

# Establish Base Directory
BASE_DIR = Path(__file__).parent

# instructions: Take your sales list of dicts from the week 1 project. Write it to a JSON 
# file with pretty-printing. Read it back. Assert the first record's amount matches the 
# original. Add a loaded_at key with datetime.now() to each record, then write again using 
# default=str. Print the first record from the file.

# Sales list of dicts from week 1:
sales = [
  {"date": "2024-01-03", "product": "Widget A", "region": "North", "amount": 1200.00, "status": "shipped"},
  {"date": "2024-01-05", "product": "Widget B", "region": "South", "amount": 340.00,  "status": "shipped"},
  {"date": "2024-01-07", "product": "Widget A", "region": "North", "amount": 870.00,  "status": "pending"},
  {"date": "2024-01-08", "product": "Widget C", "region": "East",  "amount": 95.00,   "status": "cancelled"},
  {"date": "2024-01-10", "product": "Widget A", "region": "South", "amount": 1540.00, "status": "shipped"},
  {"date": "2024-01-12", "product": "Widget B", "region": "North", "amount": 620.00,  "status": "shipped"},
  {"date": "2024-01-15", "product": "Widget C", "region": "East",  "amount": 210.00,  "status": "pending"},
  {"date": "2024-01-18", "product": "Widget A", "region": "East",  "amount": 980.00,  "status": "shipped"},
]

#save file as json
with open(BASE_DIR / "weekly_sales.json", "w", encoding="utf-8") as f:
    json.dump(sales, f, indent=2)

# load
with open(BASE_DIR / "weekly_sales.json", encoding="utf-8") as f:
    sales_from_disk = json.load(f)

if sales[0]["amount"] ==sales_from_disk[0]["amount"]:
    print("First Row Verification Confirmed")
else:
    print("First Row Verification Mismatch") 
# from AI- can use ASSERT:
assert sales[0]["amount"] == sales_from_disk[0]["amount"], \
    f"Amount mismatch: expected {sales[0]['amount']}, got {sales_from_disk[0]['amount']}"

for c in sales_from_disk:
    c["loaded_at"] = datetime.now() 

with open(BASE_DIR / "weekly_sales_with_timestamp.json", "w", encoding="utf-8") as f:
    json.dump(sales_from_disk, f, default=str, indent=2)

# Open and parse the JSON file
with open(BASE_DIR / "weekly_sales_with_timestamp.json", 'r') as file:
    data = json.load(file)

print(data[0])

# Nested JSON flattener
# Create a JSON file with at least 4 records that have this nested 
# structure: a top-level event_id, a nested user object (id, name, email),
# a nested metadata object (source, timestamp, version). 
# Write a flatten_event(record) function and apply it to all records. 
# Write the flat result to a CSV file. Print the column names of the 
# resulting CSV.

nested_webevents = [
    {
        "event_id": 1001,
        "user": {"id": "C001", "name": "Alice", "email": "Alice@domain.com"},
        "metadata": {"source": "192.168.1.118", "timestamp": "2026-05-11 23:00", "version": "A206"}
    },
    {
        "event_id": 1002,
        "user": {"id": "G002", "name": "Xander", "email": "Xander@domain.com"},
        "metadata": {"source": "192.168.1.1", "timestamp": "2026-05-12 23:00", "version": "A208"}
    },
    {
        "event_id": 1003,
        "user": {"id": "D090", "name": "Kaylee", "email": "Kaylee@domain.com"},
        "metadata": {"source": "192.145.10.445", "timestamp": "2026-05-09 23:00", "version": "A2"}
    },
    {
        "event_id": 1004,
        "user": {"id": "G007", "name": "Mal", "email": "Mal@domain.com"},
        "metadata": {"source": "192.168.3.118", "timestamp": "2026-05-05 23:00", "version": "A20"}
    },
]

def flatten_event(record):
    return {
        "event_id":        record["event_id"],
        "user_id":         record["user"]["id"],
        "user_name":   record["user"]["name"],
        "user_email":   record["user"]["email"],
        "source":       record["metadata"]["source"],
        "timestamp":      record["metadata"]["timestamp"],
        "version":        record["metadata"]["version"]
    }

flat_events = [flatten_event(o) for o in nested_webevents]
# get keys with fieldnames = list(flat_events[0].keys())
with open(BASE_DIR / "flattened_weblogs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["event_id", "user_id", "user_name","user_email","source","timestamp","version"])
    writer.writeheader()
    writer.writerows(flat_events)

with open(BASE_DIR / "flattened_weblogs.csv", newline="", encoding="utf-8") as f: 
    flattened_readback = list(csv.DictReader(f)) 
print(list(flattened_readback[0].keys()))

# OUTPUT
# First Row Verification Confirmed
# {'date': '2024-01-03', 'product': 'Widget A', 'region': 'North', 'amount': 1200.0, 'status': 'shipped', 'loaded_at': '2026-05-11 22:51:11.017627'}

#AI suggestion- more defensive
def flatten_event(record: dict) -> dict:
    user     = record.get("user", {})
    metadata = record.get("metadata", {})
    return {
        "event_id":   record.get("event_id"),
        "user_id":    user.get("id"),
        "user_name":  user.get("name"),
        "user_email": user.get("email"),
        "source":     metadata.get("source"),
        "timestamp":  metadata.get("timestamp"),
        "version":    metadata.get("version"),
    }

# Live API to JSON 
# Using the urllib.request module (built-in, no install needed — import urllib.request), 
# fetch the Open Meteo API for a city of your choice: 
# https://api.open-meteo.com/v1/forecast?latitude=44.97&longitude=-89.63&hourly=temperature_2m&forecast_days=1 
# (those coordinates are Wausau, WI — adjust if you like). Save the raw response to 
# week2/weather_raw.json. Then parse it and extract just the hourly temperature list. 
# Print the max and min temperature for the day.

url = "https://api.open-meteo.com/v1/forecast?latitude=44.97&longitude=-89.63&hourly=temperature_2m&forecast_days=1"
with urllib.request.urlopen(url) as response:
    weather_data = json.loads(response.read().decode('utf-8'))
with open(BASE_DIR / "24h_weather.json", "w", encoding="utf-8") as f:
    json.dump(weather_data, f, indent=2)
#API returns bytes
#    -> .decode("utf-8")     bytes to string
#    -> json.loads()         string to Python dict
#    -> json.dump()          Python dict to clean JSON file    