import mysql.connector as mysql
 
def upload_berryfile_to_mysql(data):
    
    for index, row in data.iterrows():
        id = 1
        
        sql = ("Insert INTO berryes (log_id, berry, state, observation_date, main_tree_typee, forest_development_class, x_cord, y_cord, year, month, day, week_number) VALUES (%s, %s, %s, %s,%s, %s, %s, %s.%s, %s, %s, %s)")
        val = [(f'{id}, {row["berry"]}, {row["state"]}, {row["observation_date"]}, {row["main_tree_typee"]}, {row["forest_development_class"]}, {row["x_cord"]}, {row["y_cord"]}, {row["year"]}, {row["month"]}, {row["day"]}, {row["week_number"]}')]

        id += 1

        print(sql)
