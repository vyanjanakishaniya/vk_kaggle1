# This file works as mysql connector, here I have created a skeleton code for performing select queries on databse.
import mysql.connector
import pandas as pd

# Mysql credentials should be changed as per the your systems credentials. 
# I have written the connector code outside so that initialization can be done when someone imports this file.

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="technical_assignment"
)


def run(sql_query, params = ()):
    # Basic function to run commands, it takes input query string and optional set of parameter
    # as in future, we might have to create a new sql command which has no parameters.
    df = pd.read_sql(sql_query, con=db_connection, params=params)
    return df


def end():
    # It is always a good practice to close the connections.
    db_connection.close()