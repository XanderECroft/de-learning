table_name = " dbo.SalesOrderHeader  "

# T-SQL LTRIM/RTRIM -> .strip()
clean = table_name.strip()
print(clean)             # "dbo.SalesOrderHeader"

# T-SQL UPPER/LOWER -> .upper()/.lower()
print(clean.upper())        # "DBO.SALESORDERHEADER"

#T-SQL CHARINDEX -> .find() or 'in'
print("." in clean)         # True
print(clean.find("."))      # 3 (zero-based index)

# T-SQL SUBSTRING -> slicing [start:end]
schema = clean[:3]          # "dbo"
obj = clean[4:]             # "SalesOrderHeader"
print(f"Schema {schema}  Object: {obj}")

#T-SQL REPLACE -> .replace
fixed = clean.replace("dbo","sales")
print(fixed)                # "sales.SalesOrderHeader"

# T-SQL LEN -> len()
print(len(clean))           # 20

# Split on delibery (like STRING_SPLIT)
parts = clean.split(".")
print(parts)                #["dbo", "SalesOrderHeader"]
