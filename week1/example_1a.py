#No DECLARE needed - Python infers type
server_name = 'SQLPROD01'   # str
port = 1433                 # int
is_active = True            # bool
latency_ms = 14.7           # float

# Check the type (like SQL_VARIANT_PROPERTY)
print(type(server_name))    # <class 'str'>
print(type(port))           # <class 'int'>

# f-strings: cleaner than concatenation
# T-SQL: PRINT 'Server: ' + @server_name + 'Port: ' + CAST(@port as VARCHAR)
print(f"Server {server_name} Port: {port}")

# Arithmetic works as expected
rows_per_second = 1_000_000     #underscore = thousands separator (readable)
hours = 2
total_rows = rows_per_second * hours * 3600
print(f"Rows in {hours}h: {total_rows:,}") # :, formats with commas