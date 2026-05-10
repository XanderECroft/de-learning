def clean_column_name(name: str) -> str:
    """
    Normalize a column name for use in a data warehouse.
    Strips whitespace, lowercases, replaces spaces with underscores
    
    Args:
        name: raw column name from source system
    Returns:
        normalized column name safe for SQL use
    """
    return name.strip().lower().replace(" ","_")

def apply_tax(amount: float, rate: float = 0.0875) -> float:
    """Apply tax rate to amount. Default rate is 8.75%"""
    return round(amount * (1+rate), 2)

def summarize_rows(rows: list[dict], amount_col: str = "amount") -> dict:
    """
    Compute basic stats over a list of row dicts.
    Returns a summary dict - like a GROUP BY ALL.
    """
    amounts = [r[amount_col] for r in rows if r.get(amount_col) is not None]
    if not amounts:
        return {"count":0, "total":0, "avg": 0, "max": 0}
    return {
        "count": len(amounts),
        "total": round(sum(amounts),2),
        "avg": round(sum(amounts) / len(amounts),2),
        "max": max(amounts)
    }

print(clean_column_name("  Order ID  "))         # order_id
print(apply_tax(100.00))                          # 108.75
print(apply_tax(100.00, rate=0.10))               # 110.0

orders = [{"amount": 150}, {"amount": 80}, {"amount": 220}]
print(summarize_rows(orders))
# {'count': 3, 'total': 450.0, 'avg': 150.0, 'max': 220}