# imported mysql.connector to be able to connect the database
import mysql.connector as mysql


import random


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
    column_names = mycursor.column_names

    # loops trough all the rows
    for r in result:
        row_zip = zip(column_names, r)
        row_dict = dict(row_zip)
        dict_data.append(row_dict)

    return dict_data

# getting all the data at once
def getalldata():
    # mysql command for getting all customers
    mycursor.execute("SELECT * FROM berry_nice.berries;")

    myresult = mycursor.fetchall()

    # creating a dictionary from fetched data
    return create_dict(myresult)

def posting_berry_data(data):

    print(data)

    # making the data to variables
    #id = random(20000, 99999)
    xcord = data['x_cord']
    ycord = data['y_cord']
    forest_dev = data['dev_class']
    main_tree = data['tree_type']
    berry = data['berry']
    date = data['date']


    # sql command for inserting to wanted database.
    sql = "INSERT INTO berries (log_id, berry, main_tree_type, forest_development_class, x_cord, y_cord, year, month, day, week_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # given values from the website
    #val = [(id), (berry), (main_tree), (forest_dev), (xcord), (ycord), (forest_dev), (forest_dev), (forest_dev), (forest_dev)]

    # executing the command and the values
    #mycursor.execute(sql, val)

    # returns these to postman after inserting the data to database
    return f"salesman_id value is: {xcord}<br>" \
    #       f"name value is: {name}<br>" \
    #       f"city value is: {city}<br>" \
    #       f"commission value is: {commission}<br>"