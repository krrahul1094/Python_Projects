import mysql.connector

con = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'rahuldb',
    passwd = '12345'
)
print(con)