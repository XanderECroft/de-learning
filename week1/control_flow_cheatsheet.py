status = "shipped"
amount = 150.00

# if/elif/else  =  CASE WHEN
if status == "shipped":
    label = "complete"
elif status == "pending":
    label = "in-progress"
else:
    label = "other"

# Compound conditions  =  AND / OR
if status == "shipped" and amount > 100:
    print("high-value shipped order")

if status == "cancelled" or amount == 0:
    print("no revenue")

# Ternary  =  one-line CASE WHEN ... ELSE
flag = "big" if amount >= 100 else "small"

# in operator for membership  =  IN (...)
valid_statuses = ["shipped", "pending", "cancelled"]
if status in valid_statuses:
    print("valid status")

# not
if status not in ["shipped", "delivered"]:
    print("not yet complete")