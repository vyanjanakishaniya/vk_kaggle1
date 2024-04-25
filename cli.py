import sys
import pandas as pd
import python_mysql_connector
import python_post_process


def main():
    # Take get the number of parameters submitted during the execution from command line.
    number_of_arguments = len(sys.argv)

    # If only one argument, means no command is being given.
    if number_of_arguments == 1:
        print("Error: Please go through the documentation and follow correct steps")
        print("Error: Command is required with proper parameter, only one argument passed")
        exit()
    
    # Command should always be the 1st parameter after file name and array starts with zero.
    command = sys.argv[1]

    # Converting all the command to lower so that the command is not case sentitive.
    command = command.lower()

    # Here there should be a if...elif...else ladder but since due to time constarin I was able to create
    # only one command which was given in the assignment description.
    if command == "demand":
        # I have only take the time frame and data between two dates, as with the inclusion of string type,
        # the result size reduces drastically.
        sql_query = "SELECT * FROM data WHERE InvoiceDate BETWEEN %s AND %s"
        params = (sys.argv[2], sys.argv[3],)
        df = python_mysql_connector.run(sql_query, params)
        print(len(df))


    if(len(df)>1):
        python_post_process.post_process(df)

    python_mysql_connector.end()




if __name__ == "__main__":
    main()