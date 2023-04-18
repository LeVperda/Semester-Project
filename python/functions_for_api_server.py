# imported mysql.connector to be able to connect the database
import mysql.connector as mysql
from datetime import datetime
import reverse_geocoder as rg


import random


# connecting to local host
mydb = mysql.connect(
    host="154.49.137.221",
    user="Nikita",
    password="CheeseTax",
    database="berry_nice",
    auth_plugin="mysql_native_password"
)

# --------------------------------------------------------
# select the correct database here
mycursor = mydb.cursor()

# --------------------------------------------------------
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

# --------------------------------------------------------
# getting all the data at once
def getalldata():
    # mysql command for getting all customers
    mycursor.execute("SELECT * FROM berry_nice.berries;")

    myresult = mycursor.fetchall()

    # creating a dictionary from fetched data
    return create_dict(myresult)

# --------------------------------------------------------
# getting map data
def getmapdata():
    mycursor.execute("SELECT html_id, count FROM berry_nice.region_counts;")

    myresult = mycursor.fetchall()

    return create_dict(myresult)

# --------------------------------------------------------
# function for posting the data to backend
def posting_berry_data(data):

    print(data)

    # making the data to variables
    id = random.randrange(20000, 99999)
    lat = data['lat']
    lon = data['lon']
    forest_dev = data['dev_class']
    main_tree = data['tree_type']
    berry = data['berry']
    date = data['datetime']

    # using Reverse_geocoder to find region, save to region variable
    region_data = rg.search((lat, lon))
    region = region_data[0]['admin1']

    # converting the input date from string to datetime
    date_datetime = datetime.strptime(date, '%Y-%m-%d')

    # getting the variables from datetime
    year = date_datetime.year
    month = date_datetime.month
    day_number = date_datetime.day
    week_number = date_datetime.isocalendar()[1]

    # --------------------------------
    print(f"datetime: {date_datetime}")
    print(type(date_datetime))
    print(f"year: {date_datetime.year}")
    print(f"month: {date_datetime.month}")
    print(f"day: {date_datetime.day}")
    print(f"weeknumber: {date_datetime.isocalendar()[1]}")

    # id
    print(id)

    # --------------------------------

    # sql command for inserting to wanted database.
    sql = "INSERT INTO berries (log_id, berry, main_tree_type, forest_development_class, lat, lon, year, month, day, week_number, region) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = []

    # given values from the website
    data = f"{id}, {berry}, {main_tree}, {forest_dev}, {lat}, {lon}, {year}, {month}, {day_number}, {week_number}, {region}"

    # Convert the string to a tuple
    data_tuple = tuple(data.split(", "))

    val.append(data_tuple)

    # executing the command and the values
    mycursor.executemany(sql, val)

    # updating region_counters
    msql = "UPDATE region_counts SET count=count+1 WHERE region LIKE %s"
    mval = (region,)
    mycursor.execute(msql, mval)

    # commit
    mydb.commit()

    # print the amount of rows inserted
    print(mycursor.rowcount, "record inserted.")
# --------------------------------------------------------

