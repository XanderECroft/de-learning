# flattening nested JSON
nested_orders = [
    {
        "order_id": 1001,
        "customer": {"id": "C001", "name": "Alice", "tier": "gold"},
        "shipping": {"city": "Chicago", "state": "IL", "zip": "60601"},
        "amount": 1200.00,
        "items": [{"sku": "W-A", "qty": 2}, {"sku": "W-B", "qty": 1}]
    },
    {
        "order_id": 1002,
        "customer": {"id": "C002", "name": "Bob", "tier": "silver"},
        "shipping": {"city": "Dallas", "state": "TX", "zip": "75201"},
        "amount": 340.00,
        "items": [{"sku": "W-C", "qty": 3}]
    }
]

def flatten_order(order: dict) -> dict:
    """Flatten one nested order dict to a single-level dict for DB loading."""
    return {
        "order_id":        order["order_id"],
        "amount":          order["amount"],
        "customer_id":     order["customer"]["id"],
        "customer_name":   order["customer"]["name"],
        "customer_tier":   order["customer"]["tier"],
        "ship_city":       order["shipping"]["city"],
        "ship_state":      order["shipping"]["state"],
        "ship_zip":        order["shipping"]["zip"],
        "item_count":      len(order["items"]),   # summarize the list
    }

flat_orders = [flatten_order(o) for o in nested_orders]
for row in flat_orders:
    print(row)
