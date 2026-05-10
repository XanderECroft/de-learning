from collections import defaultdict
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

def filter_by_status(records, status):
    """Evaluates the status of each sales record and returns those matching
       the input filter
    """
    valid_records=[]
    for ale_record in records:
        if sale_record.get("status") == status:
            valid_records.append(sale_record)
    return valid_records

def total_by_product(records):
    """Sums total revenue by product for shipped orders only"""
    product_summation = defaultdict(float)
    for shipped_sales in filter_by_status(records,"shipped"):
        product_summation[shipped_sales["product"]] += shipped_sales["amount"]
    return dict(product_summation)

def top_region(records):
    """ Returns the region with highest total shipped amount."""
    product_summation = defaultdict(float)
    for shipped_sales in filter_by_status(records,"shipped"):
        product_summation[shipped_sales["region"]] += shipped_sales["amount"]
    return max(product_summation.items(),key=lambda x: x[1])

def format_summary(product_totals) ->str: 
    """ Formats the Sales Report and returns the string to caller 
        for further processing
    """
    report_output=[]
    report_output.append('=' * 25)
    report_output.append("Sales Summary Report")
    report_output.append('=' * 25)
    report_output.append("Shipped Revenue by Product")
    for k, v in product_totals.items():
        dollar_amount = "${:,.2f}".format(v)
        report_output.append(f"{k}: {dollar_amount}" )
    report_output.append("Top Region by Shipped Revenue:")
    top_reg, top_rev = top_region(sales)
    dollar_top_rev = "${:,.2f}".format(top_rev)
    report_output.append(f"{top_reg}: {dollar_top_rev}")
    return "\n".join(report_output)

print(format_summary(total_by_product(sales)))

# Output
#=========================
#Sales Summary Report
#=========================
#Shipped Revenue by Product
#Widget A: $3,720.00
#Widget B: $960.00
#Top Region by Shipped Revenue:
#South: $1,880.00


# =============================================================================
# Week 1 Review — Key Growth Opportunities
# =============================================================================
# 1. REMOVE UNUSED ENUMERATE
#    Using enumerate() when you don't need the index adds noise.
#    Prefer: "for record in records" over "for i, record in enumerate(records)"
#
# 2. REMOVE DEBUG CODE BEFORE COMMITTING
#    Commented-out print statements should be deleted, not left in.
#    If you need the code again, Git has it.
#
# 3. RETURN STATEMENTS DON'T NEED PARENTHESES
#    return(dict(x)) implies a function call. Use: return dict(x)
#
# 4. NAME VARIABLES FOR WHAT THEY CONTAIN
#    product_summation inside top_region() holds region totals.
#    The variable name should match its contents: region_totals
#
# 5. FUNCTIONS SHOULD NOT REACH FOR GLOBALS
#    format_summary() called top_region(sales) using the global sales list
#    instead of working only with its parameters. Every function should
#    operate exclusively on what it receives as arguments. If you need
#    a value, pass it in as a parameter.
#
# 6. PREFER F-STRINGS OVER .FORMAT()
#    "${:,.2f}".format(v) works but is older style.
#    Prefer: f"${v:,.2f}" — consistent with everything else.
#
# 7. IS NONE / IS NOT NONE OVER == NONE / != NONE
#    Always use identity checks for None, not equality checks.
#    Prefer: if x is None / if x is not None
#
# 8. NEVER SHADOW BUILT-IN NAMES
#    Naming a variable "list", "dict", "str", "type", or "id" overwrites
#    the built-in. Use descriptive names: errors, records, result.
# =============================================================================