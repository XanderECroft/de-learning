row_counts = [15420, 0, 98732, 42, 0, 7891, 0, 1203]

# Basic for loop
for count in row_counts:
    print(count)

# Loop with index (like ROW_NUMBER())
for i, count in enumerate(row_counts):
    print(f"Row {i}: {count:,}")

# --- List comprehensions: SELECT + WHERE in one line ---

# All counts (SELECT count FROM row_counts)
all_counts = [c for c in row_counts]

# Only non-zero (SELECT count FROM row_counts WHERE count > 0)
non_zero = [c for c in row_counts if c > 0]
print(non_zero)           # [15420, 98732, 42, 7891, 1203]

# Transform each value (SELECT count * 1.1 FROM row_counts WHERE count > 0)
grown = [c * 1.1 for c in row_counts if c > 0]

# Uppercase all table names (SELECT UPPER(name) FROM tables)
tables = ["orders", "customers", "products"]
upper_tables = [t.upper() for t in tables]
print(upper_tables)       # ['ORDERS', 'CUSTOMERS', 'PRODUCTS']

# Aggregate manually
total = sum(non_zero)
average = sum(non_zero) / len(non_zero)
maximum = max(non_zero)
print(f"Total: {total:,}  Avg: {average:,.0f}  Max: {maximum:,}")