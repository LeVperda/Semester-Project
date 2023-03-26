import mysql.connector as mysql



def upload_berry_to_mysql(data):
    
    log_id = 10000

    # data that will be inserted to the mysql
    data = f"{log_id}, {row['berry']}, {row['main_tree_type']}, {row['forest_development_class']}, {row['x']}, {row['y']}, {row['year']}, {row['month']}, {row['day']}, {row['week_number']}"

    # Convert the string to a tuple
    data_tuple = tuple(data.split(", "))

    # appending the data to the value list
    val.append(data_tuple)

# insert statement for the mysql
sql = "INSERT INTO berryes (log_id, berry, main_tree_type, forest_development_class, x_cord, y_cord, year, month, day, week_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# excecute the command sql, add the values in list val
mycursor.executemany(sql, val)

# commit
mydb.commit()

# close


# print the amount of rows inserted
print(mycursor.rowcount, "record inserted.")