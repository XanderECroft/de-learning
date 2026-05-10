# A dict = one row of data
order = {
    "order_id": 10248,
    "customer_id": "VINET",
    "total_due": 440.00,
    "status": "shipped",
    "ship_city": "Reims"
}

#Access by key
print(order["order_id"])

# .get() is safer - returns None (or default) if key missing
# this is ISNULL(col, default)
print(order.get("email"))  #None
print(order.get("email","N/A"))

#Iterate (like looping over the column names + values)
for key, value in order.items():
    print(f"{key:15} = {value}")

#Modify
order["status"] = "delivered"   #Updte existing key
order["processed_at"] = "2024-01-16"    #add new key
del order["ship_city"]                  # remove key

# Check existence (like checking if a column exists)
print("email" in order) #Fales
print("order_id" in order) #True

# All keys, all values
print(list(order.keys()))
print(list(order.values()))
