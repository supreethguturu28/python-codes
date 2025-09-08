# Connection between Python and PostgreSQL using psycopg2

import psycopg2

db_name = "my_db1"
db_user = "postgres"
db_password = "Supreeth@1"
db_host = "localhost"
db_port = "5432"

try:
    conn = psycopg2.connect(database=db_name,
                            user=db_user,
                            password=db_password,
                            host=db_host,
                            port=db_port)
    print("Database connected successfully")
except:
    print("Database not connected")

cur = conn.cursor()
cur.execute("""
create table employee_details(ID int primary key not null,
                              Name varchar(20), Place varchar(20))""")

conn.commit()
print("Table created successfully")
