# vk_kaggle1
The following is the brief description of the assessment.
I have created a python script to run the code and perform SQL scripts.
Code is modular and is flexible for further changes.
There are 3 main files to run the code, which are cli.py, python_mysql_connector.py and python_post_process.py

cli.py is the main script. I have created only one command which is demand.
This command gets list of all the orders(invoices data) from MySQL database between the range mentioned.
To run the code, it is expected to give 3 parameters.
First is the command which is "demand"
Second is the start date and third is the end date.
eg: python cli.py demand 2010-12-14 2020-12-19

Along with these, there is another file named csv_to_sql.py which is used to extract data from csv and store it in the MySQL database.
I have tried to avoid as much string value as possible because it helps in performing analysis.
It is not possible to perform encoding for columns such as InvoiceNo and StockCode as it will become very difficult and it might impact the result.
