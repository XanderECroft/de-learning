import csv 
from pathlib import Path

# Establish Base Directory
BASE_DIR = Path(__file__).parent


    
# CSV type audit

# read input file
#AI suggestion was to do this to be consistent with BASE_DIR:
#with open(BASE_DIR / "orders.csv", newline="", encoding="utf-8") as f:
with open("week2/orders.csv", newline="", encoding="utf-8") as f: 
    rows = list(csv.DictReader(f)) 
    
# Print Header
headers = ["Column Name", "Raw Type", "Cast Type"]
widths  = [20, 10, 10]

print(" ".join(f"{h:{w}}" for h, w in zip(headers, widths)))
print(" ".join("-" * w for w in widths))

for col_name, raw_value in rows[0].items():
    try:
        int(raw_value)
        cast_type = "int"
    except ValueError:
        try:
            float(raw_value)
            cast_type = "float"
        except ValueError:
            cast_type = "str"
    print(f"{col_name:20} {"str":10} {cast_type:10}")
    #AI said not to hard-code "str"
    
# Multi-file CSV merge
# Write a script that: 
# (1) creates three separate CSV files — orders_jan.csv, orders_feb.csv, 
#     orders_mar.csv — each with 3–4 rows of made-up data including a 
#     month column, 
# (2) reads all three files in a loop, 
# (3) merges all rows into one list, 
# (4) writes a single orders_q1.csv. 
# Print the row count of each input file and the final merged file.

# Creating Separate CSVs
order_months=["jan", "feb", "mar"]
for order_month in order_months:
    sample_data = [
        {"order_id": "1001", "order_month": order_month, "customer": "Alice",   "product": "Widget A", "amount": "1200.00", "status": "shipped"},
        {"order_id": "1002", "order_month": order_month, "customer": "Bob",     "product": "Widget B", "amount": "340.00",  "status": "pending"},
        {"order_id": "1003", "order_month": order_month, "customer": "Alice",   "product": "Widget C", "amount": "95.00",   "status": "cancelled"},
    ]

    output_file = f"{BASE_DIR}/orders_{order_month}.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["order_id", "order_month", "customer","product","amount","status"])
        writer.writeheader()
        writer.writerows(sample_data)

#Read in files in a loop
monthly_orders = {}
for order_month in order_months:
    fname = f"week2/orders_{order_month}.csv"
    with open(fname, newline="", encoding="utf-8") as f: 
        monthly_orders[order_month] = list(csv.DictReader(f)) 

for month, rows in monthly_orders.items():
    print(f"orders_{month}.csv: {len(rows)} rows")

#Combine and output
all_orders = [item for sublist in monthly_orders.values() for item in sublist]

output_file = BASE_DIR/"orders_q1.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["order_id", "order_month", "customer","product","amount","status"])
    writer.writeheader()
    writer.writerows(all_orders)

print(f"orders_q1.csv: {len(all_orders)} rows")

#CSV diff checker
# Write a function diff_csvs(file_a, file_b, key_col) that reads two CSVs, 
# compares them by a key column, and reports: rows in A but not B, rows in
# B but not A, and rows in both where any value changed. 
# Test it by creating two slightly different versions of orders.csv — 
# add a row to one, change an amount in another. This is a simplified 
# version of a change-data-capture comparison, which you'll build for 
# real in later weeks.

def diff_csvs(file_a, file_b, key_col):
    # Read file_a into a dict
    with open(file_a, newline="", encoding="utf-8") as f: 
        filea_rows = list(csv.DictReader(f)) 
    # Read file_b into a dict
    with open(file_b, newline="", encoding="utf-8") as f: 
        fileb_rows = list(csv.DictReader(f)) 

    dict_a = {row[key_col]: row for row in filea_rows}
    dict_b = {row[key_col]: row for row in fileb_rows}

    for key in dict_a:
        if key not in dict_b:
            print(f"{key} in File A not found in File B")

    for key in dict_b:
        if key not in dict_a:
            print(f"{key} in File B not found in File A")

    for key in dict_a:
        if key in dict_b and dict_a[key] != dict_b[key]:
            print(f"Key {key} present in both files with data difference detected.")

diff_csvs("week2/orders_feb.csv","week2/orders_apr.csv","order_id")


# Output
#Column Name          Raw Type   Cast Type 
#-------------------- ---------- ----------
#order_id             str        int
#customer             str        str
#product              str        str
#amount               str        float
#status               str        str
#orders_jan.csv: 3 rows
#orders_feb.csv: 3 rows
#orders_mar.csv: 3 rows
#orders_q1.csv: 9 rows
#1004 in File B not found in File A
#1005 in File B not found in File A
#Key 1001 present in both files with data difference detected.
#Key 1002 present in both files with data difference detected.
#Key 1003 present in both files with data difference detected.