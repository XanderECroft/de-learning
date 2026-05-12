# read, write and navigate JSON

import json

# --- Parsing JSON strings (what you get from an API response) ---
# thisis reading a json formatted string into a dict
api_response = '{"status": "ok", "count": 3, "orders": [{"id": 1, "amount": 150.0}, {"id": 2, "amount": 80.0}]}'
data = json.loads(api_response) #load string, string -> dict

print(type(data))       # <class 'dict'>
print(data["status"])   # ok
print(data["count"])    # 3
print(data["orders"][0]["amount"]) #150.0

# --- Writing JSON
# this is taking a string and creating a json message
result = {"pipeline": "orders", "rows_loaded": 1500, "status": "success"} # a dict (key, value)
print(json.dumps(result))   #dump a string into json format
print(json.dumps(result, indent=2)) #pretty-printed

# --- File I/O ---
with open("week2/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
#the above takes a json and saves it

with open("week2/result.json", encoding="utf-8") as f:
    loaded = json.load(f)
#this loads a json from disk

# --- Handling dates (the common trap) ---
from datetime import datetime
data_with_dates = {"run_at": datetime.now(), "rows": 500}
# json.dumps(data_with_dates)           # FAILS — datetime not serializable
print(json.dumps(data_with_dates, default=str))   # Works: converts dates to strings
