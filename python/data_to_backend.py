import mysql.connector as mysql

mydb = mysql.connect(
        host="localhost",
        port="330",
        user="root",
        password="",
        auth_plugin="mysql_native_password"
        )

# select the correct database here)
mycursor = mydb.cursor()

# creates the database
mycursor.execute("CREATE DATABASE berry_nice")

# uses the database
mycursor.execute("USE berry_nice")

# creating the table
mycursor.execute("CREATE TABLE berryes (log_id INT, specie VARCHAR(255), state VARCHAR(255), date_of_observation Datetime, main_forest_type VARCHAR(255), other_forest_type VARCHAR(255), forest_development_class VARCHAR(255),x_cord INT, y_cord INT, PRIMARY KEY (log_id))")

