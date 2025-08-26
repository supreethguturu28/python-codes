import pandas as pd
from io import StringIO


def generate_sql_insert_statements(csv_data, table_name):
    # Read the CSV data
    df = pd.read_csv(StringIO(csv_data))

    # Initialize a list to hold the insert statements
    insert_statements = []

    # Loop through each row in the DataFrame and create an INSERT statement
    for index, row in df.iterrows():
        # Start the INSERT statement
        insert_statement = f"INSERT INTO {table_name} ("

        # Add the column names
        columns = ", ".join(row.index)
        insert_statement += columns + ") VALUES ("

        # Add the values
        values = []
        for value in row.values:
            if pd.isna(value):
                values.append("NULL")
            elif isinstance(value, str):
                values.append(f"'{value}'")
            else:
                values.append(str(value))

        insert_statement += ", ".join(values) + ");"

        # Add the statement to the list
        insert_statements.append(insert_statement)

    return insert_statements


def generate_mongodb_insert_statements(csv_data, collection_name):
    # Read the CSV data into a DataFrame
    df = pd.read_csv(StringIO(csv_data))

    # Initialize a list to hold the insert statements
    insert_statements = []

    # Loop through each row in the DataFrame and create an insertOne statement
    for _, row in df.iterrows():
        # Start the insert statement
        insert_statement = f"db.{collection_name}.insertOne({{"

        # Add the field names and values
        fields_and_values = []
        for field, value in row.items():
            if pd.isna(value):
                fields_and_values.append(f'"{field}": null')
            elif isinstance(value, str):
                fields_and_values.append(f'"{field}": "{value}"')
            else:
                fields_and_values.append(f'"{field}": {value}')

        insert_statement += ", ".join(fields_and_values) + "});"

        # Add the statement to the list
        insert_statements.append(insert_statement)

    return insert_statements


# Example usage:
data = "Name,Age,Date\nRachel Caseyscience,53,2022-12-30 15:09:27\nJames Valdezfloor,32,2022-12-13 00:23:21"
tbl_name = "random_table"
coll_name = "random_collection"

sql = generate_sql_insert_statements(csv_data=data, table_name=tbl_name)
for sql_sql in sql:
    print(sql_sql)

mongo_db = generate_mongodb_insert_statements(csv_data=data, collection_name=coll_name)
for mongo in mongo_db:
    print(mongo)
