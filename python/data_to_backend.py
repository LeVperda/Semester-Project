# imported mysql.connector to be able to connect the database
import mysql.connector as mysql
from functions_for_api import upload_berryfile_to_mysql

# data management imports
import numpy as np
import pandas as pd
import seaborn as sns


# this cleanup is the sameone Tuomas made in the classes.

# load data in DataFrame
df = pd.read_excel("LUKE_ripe_berries_observation_dates.xlsx")

# translate some columns
df = df.rename(columns={"marja": "berry", "havainto pvm": "observation_date", "pääpuulaji": "main_tree_type",
                        "muu puulaji": "secondary_tree_type", "metsän kehitysluokka": "forest_development_class"})

# drop unneeded columns (for now)
df = df.drop("vaihe", axis=1)
df = df.drop("Välimatka karkeistetun ja todellisen sijainnin välillä", axis=1)

# translate the berry names
df['berry'] = df['berry'].replace(['mustikka'], 'bilberry')
df['berry'] = df['berry'].replace(['puolukka'], 'lingonberry')
df['berry'] = df['berry'].replace(['suomuurain'], 'cloudberry')

# translate main tree type
df['main_tree_type'] = df['main_tree_type'].replace(['koivu'], 'birch')
df['main_tree_type'] = df['main_tree_type'].replace(['kuusi'], 'spruce')
df['main_tree_type'] = df['main_tree_type'].replace(['mänty'], 'pine')
df['main_tree_type'] = df['main_tree_type'].replace(['muu'], 'other')

# helper function to replace "other" with the secondary tree type


def replace_other_tree_type(row):
    if row['main_tree_type'] == "other":
        return row['secondary_tree_type'].lower().replace(" ", "")
    else:
        return row['main_tree_type']


df['main_tree_type'] = df.apply(replace_other_tree_type, axis=1)

# translating the secondary forest types too
df['main_tree_type'] = df['main_tree_type'].replace('suo', 'swamp')
df['main_tree_type'] = df['main_tree_type'].replace('suota', 'swamp')
df['main_tree_type'] = df['main_tree_type'].replace('suopohja', 'swamp')
df['main_tree_type'] = df['main_tree_type'].replace('sekametsä', 'mixed')
df['main_tree_type'] = df['main_tree_type'].replace('seka', 'mixed')
df['main_tree_type'] = df['main_tree_type'].replace('sekapuusto', 'mixed')
df['main_tree_type'] = df['main_tree_type'].replace('lehtikuusi', 'larch')
df['main_tree_type'] = df['main_tree_type'].replace('aukea', 'open')
df['main_tree_type'] = df['main_tree_type'].replace('aukio', 'open')
df['main_tree_type'] = df['main_tree_type'].replace('eipuita', 'open')
df['main_tree_type'] = df['main_tree_type'].replace('puuton', 'open')
df['main_tree_type'] = df['main_tree_type'].replace(
    'vanhaavaivaiskoivua', 'softbirch')
df['main_tree_type'] = df['main_tree_type'].replace(
    'vaivaiskoivikko', 'softbirch')

# now we only have values in English
df['main_tree_type'].value_counts()

df['main_tree_type'] = df['main_tree_type'].astype(str)

df = df.drop("secondary_tree_type", axis=1)

# kasvatusmetsä = plantation_forest
# taimikko = seedling
# varttunut metsä = old_forest
# aukea = clearing

# translate the forest development class
df['forest_development_class'] = df['forest_development_class'].replace([
                                                                        'aukea'], 'clearing')
df['forest_development_class'] = df['forest_development_class'].replace(
    ['taimikko'], 'seedling')
df['forest_development_class'] = df['forest_development_class'].replace(
    ['varttunut metsä'], 'old')
df['forest_development_class'] = df['forest_development_class'].replace(
    ['kasvatusmetsä'], 'plantation')

# split the observation date into year, month, day and also a week number
df['year'] = df['observation_date'].dt.year
df['month'] = df['observation_date'].dt.month
df['day'] = df['observation_date'].dt.day
df['week_number'] = df['observation_date'].dt.isocalendar().week

df['berry'] = df['berry'].astype(str)
df['berry'].dtype


# data to the backend

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

# creates the database
mycursor.execute("CREATE DATABASE IF NOT EXISTS Berry_nice")

# selecting database
mycursor.execute("USE Berry_nice")

# creating the table
# mycursor.execute("CREATE TABLE IF NOT EXISTS berries (log_id INT, berry VARCHAR(255), observation_date Datetime, main_tree_typee VARCHAR(255), forest_development_class VARCHAR(255),x_cord INT, y_cord INT, year INT, month INT, day INT, week_number INT, PRIMARY KEY (log_id))")

mycursor.execute("CREATE TABLE IF NOT EXISTS berries (log_id INT, berry VARCHAR(255), main_tree_type VARCHAR(255), forest_development_class VARCHAR(255),x_cord INT, y_cord INT, year INT, month INT, day INT, week_number INT, PRIMARY KEY (log_id))")

# looping the data to the mysql 

# list of all items in excel sheet
val = []

# looping trough the dataframe
# getting the index number of the row for getting the id for the tables
# getting the row using iterrows
for index, row in df.iterrows():
    log_id = 10000 + index

    # data that will be inserted to the mysql
    data = f"{log_id}, {row['berry']}, {row['main_tree_type']}, {row['forest_development_class']}, {row['x']}, {row['y']}, {row['year']}, {row['month']}, {row['day']}, {row['week_number']}"

    # Convert the string to a tuple
    data_tuple = tuple(data.split(", "))

    # appending the data to the value list
    val.append(data_tuple)

# insert statement for the mysql
sql = "INSERT INTO berries (log_id, berry, main_tree_type, forest_development_class, x_cord, y_cord, year, month, day, week_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# excecute the command sql, add the values in list val
mycursor.executemany(sql, val)

# commit
mydb.commit()

# close
mydb.close()

# print the amount of rows inserted
print(mycursor.rowcount, "record inserted.")

