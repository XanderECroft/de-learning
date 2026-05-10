# A list of dicts = a full result set
orders = [
    {"order_id": 1, "customer": "Alice", "amount": 150.00, "status": "shipped"},
    {"order_id": 2, "customer": "Bob",   "amount": 80.00,  "status": "pending"},
    {"order_id": 3, "customer": "Alice", "amount": 220.00, "status": "shipped"},
    {"order_id": 4, "customer": "Carol", "amount": 15.00,  "status": "cancelled"},
]

# WHERE status = 'shipped'
shipped = [o for o in orders if o["status"] == "shipped"]

# SUM(amount) WHERE status = 'shipped'
total = sum(o["amount"] for o in orders if o["status"] == "shipped")
print(f"Shipped total: ${total:.2f}")


# SELECT customer, amount — projection
names_amounts = [(o["customer"], o["amount"]) for o in orders]

# GROUP BY customer — manual aggregation
from collections import defaultdict
totals_by_customer = defaultdict(float)
for o in orders:
    totals_by_customer[o["customer"]] += o["amount"]
print(dict(totals_by_customer))
# {'Alice': 370.0, 'Bob': 80.0, 'Carol': 15.0}
print(totals_by_customer)