import csv 
from pathlib import Path

# Establish Base Directory
BASE_DIR = Path(__file__).parent


with open("week2/orders.csv", newline="", encoding="utf-8") as f: 
    rows = list(csv.DictReader(f)) 
    
# Cast types 
for row in rows: 
    row["amount"] = float(row["amount"]) 
    row["order_id"] = int(row["order_id"]) 
    
# Filter to shipped orders only 
shipped = [r for r in rows if r["status"] == "shipped"] 
    
# Add a computed column 
for row in shipped: 
    row["amount_with_tax"] = round(row["amount"] * 1.0875, 2) 
        
# Write transformed output 
fieldnames = ["order_id", "customer", "product", "amount", "amount_with_tax"] 

with open("week2/orders_shipped.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore") 
    writer.writeheader() 
    writer.writerows(shipped) 

print(f"Wrote {len(shipped)} shipped orders to orders_shipped.csv")