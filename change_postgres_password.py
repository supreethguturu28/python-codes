import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    user="postgres",
    password="Supreeth@1",
    host="localhost",
    database="postgres"
)

# Open a cursor to perform database operations
cursor = conn.cursor()

# Change the user password
new_password = "postgres"
cursor.execute(f"ALTER USER postgres WITH PASSWORD '{new_password}';")

# Commit the changes
conn.commit()

# Close communication with the database
cursor.close()
conn.close()
