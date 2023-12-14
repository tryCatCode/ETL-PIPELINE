import sqlite3
import pandas as pd


sql_connection = sqlite3.connect("STAFF.db")
print("Opened database successfully")

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = '/home/project/database_python/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, sql_connection, if_exists = 'replace', index =False)
print('Table is ready')

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, sql_connection)
print(query_statement)
print(query_output)

query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, sql_connection)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, sql_connection)
print(query_statement)
print(query_output)

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, sql_connection, if_exists = 'append', index =False)
print('Data appended successfully')

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, sql_connection)
print(query_statement)
print(query_output)


sql_connection.close()