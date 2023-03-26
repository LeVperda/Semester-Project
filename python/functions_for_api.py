# imported mysql.connector to be able to connect the database
import mysql.connector as mysql

# connecting to local host
mydb = mysql.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Kg39562K!jkm",
    auth_plugin="mysql_native_password"
)

# select the correct database here
mycursor = mydb.cursor()

# creating dictionary from gotten result
def create_dict(result):
    dict_data = []

    # column names as tuple
    culumn_names = mycursor.column_names

    # loops trough all the rows
    for r in myresult:
        row_zip = zip(column_names, r)
        row_dict = dict(row_zip)
        dict_data.append(row_dict)

    return dict_data

# getting all the data at once
def getalldata():
    # mysql command for getting all customers
    mycursor.execute("SELECT * FROM berry_nice.berryes;")

    myresult = mycursor.fetchall()

    # creating a dictionary from fetched data
    return create_dict(myresult)