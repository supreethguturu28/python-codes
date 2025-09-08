# Data Migration from PostgreSQL Database to MySQL database in python

import psycopg2
import mysql.connector

pg_connection = psycopg2.connect(dbname='my_db1',
                                 user='postgres',
                                 password='Supreeth@1',
                                 host='localhost',
                                 port='5432')
pg_cursor = pg_connection.cursor()

mysql_connection = mysql.connector.connect(user='root',
                                           password='Supreeth@1',
                                           host='localhost',
                                           database='supreeth')
mysql_cursor = mysql_connection.cursor()

# Query the schema of PostgreSQL table
pg_cursor.execute("""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = 'student_details'
""")
pg_columns = pg_cursor.fetchall()

# Define mapping of PostgreSQL data types to MySQL data types
data_type_mapping = {
    'integer': 'INT',
    'character varying': 'VARCHAR(255)',
    'text': 'TEXT',
    'numeric': 'DECIMAL',
    # Add more mappings as needed
}

# Construct CREATE TABLE statement for MySQL
create_table_query = "CREATE TABLE IF NOT EXISTS student_details ("
for column in pg_columns:
    column_name, pg_data_type = column
    mysql_data_type = data_type_mapping.get(pg_data_type, 'VARCHAR(255)')
    create_table_query += f"{column_name} {mysql_data_type}, "
create_table_query = create_table_query.rstrip(', ') + ")"
mysql_cursor.execute(create_table_query)
mysql_connection.commit()

# Query data from PostgreSQL
pg_cursor.execute("SELECT * FROM student_details")
student_records = pg_cursor.fetchall()

# Insert data into MySQL
for record in student_records:
    mysql_cursor.execute("INSERT INTO student_details (Student_ID,Student_Name,Student_Age,Student_City,"
                         "Student_Marks) VALUES (%s, %s, %s, %s, %s)", record)

# Commit the changes to MySQL
mysql_connection.commit()

pg_cursor.close()
pg_connection.close()

mysql_cursor.close()
mysql_connection.close()

print("Migration completed.")

