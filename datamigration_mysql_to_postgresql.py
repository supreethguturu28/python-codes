# Migration of Data from MySQL database to PostgreSQL Database in Python

import mysql.connector
import psycopg2

# Connect to MySQL Database
my_sql_database = 'supreeth'
mysql_connection = mysql.connector.connect(host='localhost', user='root', database=my_sql_database, password='Supreeth@1')
mysql_cursor = mysql_connection.cursor(dictionary=True)

# Connect to PostgreSQL Database
pg_connection = psycopg2.connect(host='localhost', user='postgres', password='Supreeth@1', dbname='my_db1')
pg_cursor = pg_connection.cursor()

# List of tables to migrate
tables_to_migrate = ['one']

for table in tables_to_migrate:
    # Fetch column names and types from MySQL information schema
    mysql_cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{my_sql_database}' AND TABLE_NAME = '{table}';")
    columns_info = mysql_cursor.fetchall()

    # Construct column definitions for PostgreSQL CREATE TABLE
    column_defs = [f"{column_info['COLUMN_NAME']} {column_info['DATA_TYPE']}" for column_info in columns_info]

    # Create PostgreSQL table with matching column definitions
    create_table_query = f"CREATE TABLE {table} ({', '.join(column_defs)})"
    pg_cursor.execute(create_table_query)

    # Fetch data from MySQL
    mysql_cursor.execute(f"SELECT * FROM {table};")
    data = mysql_cursor.fetchall()

    # Insert data into PostgreSQL table
    for row in data:
        placeholders = ', '.join(['%s'] * len(row))
        column_names = ', '.join(row.keys())
        insert_query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
        pg_cursor.execute(insert_query, tuple(row.values()))

    # Commit changes for the current table
    pg_connection.commit()

pg_cursor.close()
pg_connection.close()

mysql_cursor.close()
mysql_connection.close()

print("Migration completed.")
