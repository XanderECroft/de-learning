from datetime import datetime, date, timedelta, timezone

def normalize_date(test_date: str) ->date:
    test_formats= [
    "%Y-%m-%d","%m/%d/%Y","%Y-%m-%dT%H:%M:%S","%B %d, %Y","%d-%b-%y"
    ]
    
    for test_format in test_formats:
        try:
            return datetime.strptime(test_date,test_format).date()
        except:
            pass
    raise ValueError(f"Unable to parse date: '{test_date}' — no matching format found")

for tst_date in ["2024-01-15", "01/15/2024", "15-Jan-2024", "20240115", "2024-01-15T09:30:00","2024-13-32"]:
    try:
        normalized_date = normalize_date(tst_date)
        print(f"{tst_date:25} -> {normalized_date}")
    except ValueError as e:
        print(f"{tst_date:25} -> ERROR: {e}")

# Pipeline run timestamp enricher
# Take the list of dicts from the week 1 sales data (or recreate it). 
# Add these computed fields to each record: order_date parsed from string 
# to a date object, year, month, day_of_week (0=Monday), days_since_order 
# (from today), loaded_at_utc (current UTC datetime as ISO string). 
# Print the first three enriched records.

sales = [
  {"date": "2024-01-03", "product": "Widget A", "region": "North", "amount": 1200.00, "status": "shipped"},
  {"date": "2024-01-05", "product": "Widget B", "region": "South", "amount": 340.00,  "status": "shipped"},
  {"date": "2024-01-07", "product": "Widget A", "region": "North", "amount": 870.00,  "status": "pending"},
  {"date": "2024-01-08", "product": "Widget C", "region": "East",  "amount": 95.00,   "status": "cancelled"},
  {"date": "2024-01-10", "product": "Widget A", "region": "South", "amount": 1540.00, "status": "shipped"},
  {"date": "2024-01-12", "product": "Widget B", "region": "North", "amount": 620.00,  "status": "shipped"},
  {"date": "2024-01-15", "product": "Widget C", "region": "East",  "amount": 210.00,  "status": "pending"},
  {"date": "2024-01-18", "product": "Widget A", "region": "East",  "amount": 980.00,  "status": "shipped"},
]

def enrich_record(s: dict) -> dict:
    order_date = datetime.strptime(s["date"], "%Y-%m-%d").date()
    return {
        **s,
        "order_date":      order_date,
        "year":            order_date.year,
        "month":           order_date.month,
        "day_of_week":     order_date.weekday(),
        "days_since_order": (date.today() - order_date).days,
        "loaded_at_utc":   datetime.now(timezone.utc).isoformat(),
    }
sales_new = [enrich_record(s) for s in sales]
print(sales_new)

# Write a function get_load_window(last_loaded_at: datetime, lag_minutes: int = 5) -> tuple[datetime, datetime] 
# that returns a (start, end) tuple for an incremental load — start is last_loaded_at minus a 5-minute overlap 
# (to catch late arrivals), end is now minus lag_minutes (to avoid reading in-flight records). Both datetimes 
# should be UTC-aware. Print the window as a SQL WHERE clause: WHERE updated_at >= '...' AND updated_at < '...'. 
# This is an exact pattern from real incremental pipeline code.

def get_load_window(last_loaded_at: datetime, lag_minutes: int = 5, overlap_minutes: int = 5) -> tuple[datetime, datetime]:
    return (last_loaded_at - timedelta(minutes=overlap_minutes), datetime.now(timezone.utc) - timedelta(minutes=lag_minutes))

date_obj = datetime(2025,6,5,12,12,00, tzinfo=timezone.utc)
load_window=get_load_window(date_obj)
start_str = load_window[0].strftime('%Y-%m-%d %H:%M:%S')
end_str   = load_window[1].strftime('%Y-%m-%d %H:%M:%S')
print(f"WHERE updated_at >= '{start_str}' AND updated_at < '{end_str}'")