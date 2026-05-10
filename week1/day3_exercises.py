# Row transformer
row = {"OrderID": "10248", "CustomerID": "VINET",
       "Freight": "32.38", "ShipCountry": "France", "Discount": None}

for key, value in row.items():
    print(f"{key:15} = {value}")

row["OrderID"] = int(row["OrderID"])
row["Freight"] = float(row["Freight"])
print(row.get("Discount", "0.0"))  
row["Discount"] = row.get("Discount") or 0.0
row["FreightWithTax"] = round(row["Freight"] * 1.2,2)
print(row)

# Mini GROUP BY
runs = [
  {"pipeline": "orders",    "status": "success", "rows": 1500},
  {"pipeline": "customers", "status": "failed",  "rows": 0},
  {"pipeline": "orders",    "status": "success", "rows": 1523},
  {"pipeline": "products",  "status": "success", "rows": 842},
  {"pipeline": "customers", "status": "success", "rows": 1100},
  {"pipeline": "orders",    "status": "failed",  "rows": 0},
]
from collections import defaultdict
totals_by_pipeline = defaultdict(float)
for o in runs:
    totals_by_pipeline[o["pipeline"]] += o["rows"]
print(dict(totals_by_pipeline))

failure_by_pipeline = defaultdict(int)
for o in runs:
    if o["status"]== "failed":
        failure_by_pipeline[o["pipeline"]] += 1
print(dict(failure_by_pipeline))

failed_pipelines = [(r["pipeline"]) for r in runs if r["status"] == "failed"]
print(list(set(failed_pipelines)))


#Schema introspection dict
schema = {
    "PremiumTransaction_id": {"type": "int",     "nullable": False, "max_length": None},
    "WrittenPremium_AMT":    {"type": "float",   "nullable": False, "max_length": None},
    "RateState_CDE":         {"type": "char",    "nullable": True,  "max_length": None},
    "ISO_CDE":               {"type": "varchar", "nullable": False, "max_length": 5},
    "CustomerName":          {"type": "varchar", "nullable": False, "max_length": 255},
}
# All nullable columns
nullable_cols = [col for col, props in schema.items() if props["nullable"]]

# All varchar columns with max_length > 100
long_varchars = [col for col, props in schema.items()
                 if props["type"] == "varchar" and (props["max_length"] or 0) > 100]

create_tbl = 'CREATE TABLE PREMIUM_TRANSACTION (\n'
for col, props in schema.items():
    create_tbl += f"{col} {props["type"]}"
    if props["max_length"] != None:
        create_tbl +=f"({props["max_length"]})"
    if props["nullable"]:
        create_tbl +=" NULL\n"
    else:
        create_tbl +=" NOT NULL\n"
create_tbl += ")"        

print(create_tbl)

#Missing commas, "None" is a python null.  use IS NOT None
#alternative
lines = []
for col, props in schema.items():
    line = f"    {col} {props['type']}"
    if props["max_length"] is not None:
        line += f"({props['max_length']})"
    line += " NULL" if props["nullable"] else " NOT NULL"
    lines.append(line)

create_tbl = "CREATE TABLE PREMIUM_TRANSACTION (\n"
create_tbl += ",\n".join(lines)
create_tbl += "\n)"
print(create_tbl)


#OUTPUT
# OrderID         = 10248
# CustomerID      = VINET
# Freight         = 32.38
# ShipCountry     = France
# Discount        = None
# None
# {'OrderID': 10248, 'CustomerID': 'VINET', 'Freight': 32.38, 'ShipCountry': 'France', 'Discount': None, 'FreightWithTax': 38.856}
# {'orders': 3023.0, 'customers': 1100.0, 'products': 842.0}
# {'customers': 1, 'orders': 1}
# ['customers', 'orders']
# CREATE TABLE PREMIUM_TRANSACTION (
# PremiumTransaction_id int NOT NULL
# WrittenPremium_AMT float NOT NULL
# RateState_CDE char NULL
# ISO_CDE varchar(5) NOT NULL
# CustomerName varchar(255) NOT NULL
# )

# Things to carry into Day 4: imports at the top, is not None instead 
# of != None, and join() for building delimited strings. That last one 
# comes up in almost every pipeline you'll ever write.