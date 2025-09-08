import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='supreeth',
                                         user='root',
                                         password='Supreeth@1')
    if connection.is_connected():
        cursor = connection.cursor()

        query = """insert into one(StudentID,FirstName,LastName,City,Marks)
                             values (8,'Harry','Porter','NC',14);"""

        cursor.execute(query)
        connection.commit()
        print("Executed")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")