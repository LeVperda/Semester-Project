import mysql.connector as mysql


def test(data):
    for x in range(len(data)):
            
        print(x)

 
def upload_berryfile_to_mysql(data):
    #mycursor.execute("CREATE TABLE berryes (log_id INT, specie VARCHAR(255), state VARCHAR(255), date_of_observation Datetime, main_forest_type VARCHAR(255), other_forest_type VARCHAR(255), forest_development_class VARCHAR(255),x_cord INT, y_cord INT, PRIMARY KEY (log_id))")


    for x in data:
        
        sql = "Insert INTO berryes (log_id, berry, state, observation_date, main_tree_typee, forest_development_class, x_cord, y_cord, year, month, day, week_number) VALUES (%s, %s, %s, %s,%s, %s, %s, %s.%s, %s, %s, %s)"
        val = [(f"{x}, {data[x].berry}, {data[x].state}, {data[x].observation_date}, {data[x].main_tree_typee}, {data[x].forest_development_class}, {data[x].x_cord}, {data[x].y_cord}, {data[x].year}, {data[x].month}, {data[x].day}, {data[x].week_number}")]

        print(x)