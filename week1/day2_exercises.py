# Pipeline stage tracker

# Original List
stages = ["extract", "validate", "transform", "load", "notify"]

#Print the first and last stages
print(f"First Stage: {stages[0]}, Last Stage: {stages[-1]}")

#Print all stages except the first and last
print(stages[1:-1])

#Print the stages in reverse order
stages.sort(reverse=True)
print(stages)
#Correction to not change original list
print(sorted(stages, reverse=True))



#Print the count of stages
print(f"length of stages: {len(stages)}")

#Print whether "audit" is in the list
audit = False
for entry in stages:
    if entry == "audit":
        audit = True
        print("Audit Found")
        break
if audit == False:
    print("No Audit Found")

#Better audit check:
print("audit" in stages)        # False
if "audit" not in stages:
    print("No Audit Found")

##Output
#First Stage: extract, Last Stage: notify
#['validate', 'transform', 'load']
#['validate', 'transform', 'notify', 'load', 'extract']
#length of stages: 5
#No Audit Found

#Row count filter
row_counts = [0, 1500, 0, 42080, 7, 0, 99, 0, 38410, 22]

#A list of only the non-zero counts
non_zero = [c  for c in row_counts if c > 0]
print(non_zero)

#A list of counts that are above the average of all non-zero counts
non_zero = [c for c in row_counts if c > 0] #Avoid zeros
avg = sum(non_zero) / len(non_zero)
above_avg = [c  for c in row_counts if c > avg]
print(above_avg)

#A list of strings in format "Table_4: 42,080 rows" for every non-zero count (use enumerate to get the index)
for i, count in enumerate(row_counts):
    if count> 0:
        print(f"Table_{i}: {count:,d} rows")

#Output
#[1500, 42080, 7, 99, 38410, 22]
#[42080, 38410]
#Table_1: 1,500 rows
#Table_3: 42,080 rows
#Table_4: 7 rows
#Table_6: 99 rows
#Table_8: 38,410 rows
#Table_9: 22 rows

#Error-- want to make a list (array), not print a literal list. Correct:
table_strings = [
    f"Table_{i}: {count:,} rows"
    for i, count in enumerate(row_counts)
    if count > 0
]
print(table_strings)


#Column name normalizer
cols = ["  Order ID  ", "CustomerName", "TOTAL DUE",
        "order_date", "ShipTo_City", "ZIP CODE"]

print(f"{[c.strip().lower().replace(" ","_") for c in cols]}")
print(f"{["src_" + c if c[0:5] != "order" else c for c in [c.strip().lower().replace(" ","_") for c in cols]]}")

#Recommendation
normalized = [c.strip().lower().replace(" ", "_") for c in cols]
prefixed   = [c if c.startswith("order") else f"src_{c}" for c in normalized]

print(normalized)
print(prefixed)


#Output
#['order_id', 'customername', 'total_due', 'order_date', 'shipto_city', 'zip_code']
#['order_id', 'src_customername', 'src_total_due', 'order_date', 'src_shipto_city', 'src_zip_code'] 


# The comprehension instinct is clearly there — you reached for it 
# naturally on exercise 3 without being prompted, and the 
# syntax is clean. The two things to carry into Day 3 are: never 
# mutate a list when you only need a display version of it, and always be 
# precise about which population you're computing statistics over. Both 
# of those will come up again in pandas.

