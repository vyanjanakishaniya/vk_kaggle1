# I have created this file to upload data from csv file to MySQL database.
# It solves the problem of date time conversion from CSV file to MySQL database column of InvoiceDate.
import pandas as pd
import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="technical_assignment"
)
cursor = db_connection.cursor()

# Read data from CSV file into a DataFrame
csv_file = "data.csv"
df = pd.read_csv(csv_file, encoding = "ISO-8859-1")

df = df.dropna()

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Define the table name where you want to insert the data
table_name = "data"

# Define the columns to insert into
columns = ','.join(df.columns)

# Create a placeholders string for values
values_placeholder = ','.join(['%s'] * len(df.columns))

# Iterate through DataFrame rows and insert into the database
for index, row in df.iterrows():
    # Convert each row to a tuple of values
    values = tuple(row)
    
    # Construct the SQL query for insertion
    sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_placeholder})"
    
    # Execute the SQL query
    cursor.execute(sql_query, values)


# Commit the changes
db_connection.commit()

# Close the cursor and database connection
cursor.close()
db_connection.close()
