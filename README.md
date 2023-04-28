# Semester Project
 MLDE22 Semester Project, Spring 2023

----------------------------------------------------------------------------

PROJECT MEMBERS AND RESPONSIBILITIES:

Niko Puro – Project management, developing backend part, created HTML page frames, databases, data collection page, interactive part of data analytics page. 

Kirill Sobolev – Most part of data analytics and visualization. 

Nikita Petrov – Interactive map, backend, setting up the MySQL server, video presentation script, editing and filming 

Vy Ngo – Frontend development, video presentation filming, project chairman, text content creator 

Hansa Pankow – Frontend development, text content creator, designer. 

---------------------------------------------------------------------------

Video presentation link:
https://www.youtube.com/watch?v=2j8Umjbrwjg

---------------------------------------------------------------------------

How to use MySQL Server

The server is running on Hostinger, it is on Ubuntu 22.04, without GUI.

IP: 154.49.137.221

remote connection via Terminal:
- ssh root@154.49.137.221

All the root passwords (OS and MySQL) are: ***********
Please message project members privately if access is needed

I have duplicated the python scripts for this server, the originals are still there, untouched. 
There is now a copy of each script, with "_server_" added to the end.

To log in to MySQL server as a root:
- mysql -u root -p

Use it to add new users if you want, give all permissions, etc.

SOMETIMES it is stuck
I have noticed that it gets stuck whenever I delete a table, or truncate one.
If youre stuck in MySQL, just restart the terminal and connect again.

run this to restart MySQL server:
- sudo systemctl restart mysql.service

Afther that, you should be able to login as a root again, and continue.


WHEN RUNNING WEBSITE LOCALLY

you can run the FLASK_APP=BerryNiceApp_server.py
everything else should work normally

---------------------------------------------------------------------------

Data_to_backend.ipynb, data_to_backend.py, Data_to_backend_server.ipynb
 
- are creating the schemas to the mysql database and table
- connect to the database. requirements {host, password and user}
- original data file "LUKE_ripe_berries_observation_dates.xlsx" is opened in this file and cleaned
- server uses "Interactive Map/region_data.csv" file for the interactive map

Installment requirements:

- numpy
- pandas
- seaborn
- matplotlib
- mysql.connector
- flask
- flask-cors
- reverse_geocoder


to get the Flask work

Terminal commands:

- set FLASK_DEBUG=true
- set FLASK_APP=BerryNiceApp.py
- flask run

After all is done. run the python file