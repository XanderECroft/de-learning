# Connection String Factory
def build_conn_string(host:str, database:str, port:int=1433, driver:str="ODBC Driver 18 for SQL Server") ->str:
    """Constructs a pyodbc connection string with ODBC 18 
       and the standard SQL Server port as default
    """
    return f"DRIVER={driver};SERVER={host},{port}; DATABASE={database};Trusted_Connection=True"

print(build_conn_string("sqldev01","Adventureworks"))
print(build_conn_string("sqldev01","Adventureworks",port=1434))
print(build_conn_string("sqldev01","Adventureworks", port=1434, driver= "ODBC Driver 16 for SQL Server"))

# Row Validator
def validate_order_row(row: dict) -> tuple[bool, list[str]]:
    """Data quality check on an order row, evaluating the order_id, 
       amount, and status code
    """
    list=[]
    is_valid = True
    if "order_id" not in row or row.get("order_id") < 0:
        list.append("Invalid order_id")
        is_valid = False
    if "amount" not in row or row.get("amount") < 0:
        list.append("Invalid amount")
        is_valid = False
    if row.get("status") not in ["pending", "shipped", "cancelled"]:
        list.append("invalid status")
        is_valid = False
    return (is_valid, list)
# AI Correction-- check for existance, then value:
#if "order_id" not in row:
#    errors.append("Missing order_id")
#    is_valid = False
#elif not isinstance(row["order_id"], int) or row["order_id"] <= 0:
#    errors.append("Invalid order_id — must be a positive integer")
#    is_valid = False

print(validate_order_row({"order_id":25, "amount":5.60, "status":"shipped"}))
print(validate_order_row({"order_id":-25, "amount":-5.60, "status":"shipped"}))
print(validate_order_row({"order_id":25, "amount":5.60}))

#Batch Processor
def process_in_batches(items: list, batch_size: int=100):
    """Receives a list of items and breaks them up into batches of size batch_size,
       returning a list of lists
    """
    chunks=[]
    for i in range(0, len(items),batch_size): 
        chunks.append(items[i:i+batch_size])
    return chunks

def fake_load(batch: list) -> int:
    """Simulates loading a batch into a database.  Returns the size of data load"""
    return len(batch)

#Simulation
input_list = list(range(0,250))
chunks = process_in_batches(input_list)
total_load = 0
#for i in range(0,len(chunks)):
for i, batch in enumerate(chunks):
    loaded = fake_load(batch)    
    total_load += loaded
    print(f"Loaded batch {i+1}: {loaded} rows {total_load} total)")



#Output
#DRIVER=ODBC Driver 18 for SQL Server;SERVER=sqldev01:1433, DATABASE=Adventureworks;Trusted_Connection=True
#DRIVER=ODBC Driver 18 for SQL Server;SERVER=sqldev01:1434, DATABASE=Adventureworks;Trusted_Connection=True
#DRIVER=ODBC Driver 16 for SQL Server;SERVER=sqldev01:1434, DATABASE=Adventureworks;Trusted_Connection=True
#[True, []]
#[False, ['Invalid order_id', 'Invalid amount']]
#[False, ['invalid status']]
#Loaded batch 0: 100 rows 100 total)
#Loaded batch 1: 100 rows 200 total)
#Loaded batch 2: 50 rows 250 total)

# Four days in and the structure of your code is already clean — functions 
# have docstrings, names are descriptive, and you're thinking about edge 
# cases. The things to carry into Day 5: never shadow built-in names 
# (list, dict, str, type, id), always check what happens when a value is 
# None before comparing it, and prefer enumerate over range(len(...)) 
# when you need both index and value.