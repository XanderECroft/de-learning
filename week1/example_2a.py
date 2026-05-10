tables = ["Orders", "Customers", "Products", "Inventory", "Shipments"]

# Indexing - zero based (first element is[0])
print(tables[0])    # Orders
print(tables[-1])   # Shipments (negative = from end)

#Slicing [start:end] - end is EXCLUSIVE, like OFFSET x Rows FETCH next y
print(tables[1:3])  # ['Customers', 'Products']
print(tables[:2])   # ["Orders", "Customers"]
print(tables[3:])   # ["Inventory", "Shipments"]

# Length
print(len(tables))  # 5

#Mutating - lists are mutable (unlike SQL result sets)
tables.append("Returns")        # add to end
tables.insert(0, "Schemas")     # insert at position
tables.remove("Inventory")      # remove by value
popped = tables.pop()           # remove and return last item
print(tables)

# Sorting (in-place vs returning new)
tables.sort()       # modifies tables
sorted_copy = sorted(tables)    # returns new list, tables unchanged
tables.sort(reverse=True)       # descending