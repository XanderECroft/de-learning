#day1_exercises.py

#Connection string builder
# Variable Declaration
host = "SQLPROD01"
database = "AdventureWorks"
port = 1433
username = "etl_user"

#Connection string
conn = f"Server={host},{port};Database={database};User={username};"
print(conn)
print(len(conn))



#Table Name Parser
raw = " [dbo].[SalesOrderHeader] "

clean=raw.strip().replace("[","").replace("]","")
print(clean)        # dbo.SalesOrderHeader
print(clean[:3])    # dbo
print(clean[4:])    # SalesOrderHeader
clean_snake = ""
for char in clean[4:]:
    if char.isupper():
        char = "_"+char.lower()
    clean_snake += char
print(clean_snake[1:])  #sales_order_header

#Alternative to fix the leading _s
clean_snake = ""
for i, char in enumerate(clean[4:]):  #Enumerate gives an index
    if char.isupper() and i > 0:
        clean_snake += "_" + char.lower()
    else:
        clean_snake += char.lower()
print(clean_snake)


#Data type detective
order_id = "10248"
amount = "432.80"
is_shipped = "True"
order_date = "2024-01-15"
order_id_int = int(order_id)

#print(f"order_id: {order_id_int}: ", type(order_id_int))
print(f"order_id: {order_id_int}  type={type(order_id_int).__name__}")
#The .__name__ gives you just int instead of <class 'int'>, which is easier to read. 



amount_flt = float(amount)
print(f"amount: {amount_flt:.2f}: ", type(amount_flt))
#The :.2f format specifier is your FORMAT(@amount, 'N2')


is_shipped_bool = is_shipped.strip().lower()=="true"
print(f"is_shipped: {is_shipped_bool}: ", type(is_shipped_bool))

print(f"order_date: {order_date}", type(order_date))

total = amount_flt * 1.0875
print(f"Total Price :{round(total,2)}")


#Output
#Server=SQLPROD01,1433;Database=AdventureWorks;User=etl_user;
#60
#dbo.SalesOrderHeader
#dbo
#SalesOrderHeader
#sales_order_header
#order_id: 10248:  <class 'int'>
#amount: 432.8:  <class 'float'>
#is_shipped: True:  <class 'bool'>
#order_date: 2024-01-15 <class 'str'>
#Total Price :470.67