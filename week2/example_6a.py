import csv
from pathlib import Path

# Establish Base Directory
BASE_DIR = Path(__file__).parent

# First: create a sample CSV to work with
sample_data = [
    {"order_id": "1001", "customer": "Alice",   "product": "Widget A", "amount": "1200.00", "status": "shipped"},
    {"order_id": "1002", "customer": "Bob",     "product": "Widget B", "amount": "340.00",  "status": "pending"},
    {"order_id": "1003", "customer": "Alice",   "product": "Widget C", "amount": "95.00",   "status": "cancelled"},
    {"order_id": "1004", "customer": "Carol",   "product": "Widget A", "amount": "870.00",  "status": "shipped"},
    {"order_id": "1005", "customer": "Bob",     "product": "Widget B", "amount": "620.00",  "status": "shipped"},
]

output_file = BASE_DIR / "orders.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["order_id", "customer","product","amount","status"])
    writer.writeheader()
    writer.writerows(sample_data)

print("Written: week2/orders.csv")

# Now read it back
with open("week2/orders.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Read {len(rows)} rows")
print(rows[0])          #{'order_id': '1001', 'customer': 'Alice', ...}
print(type(rows[0]["amount"]))  # <class 'str'>  -- ALWAYS a string from CSV!

# Cast the types you need
for row in rows:
    row["amount"] = float(row["amount"])
    row["order_id"] = int(row["order_id"])

# Verify
print(f"Total amount: ${sum(r['amount'] for r in rows):,.2f}")