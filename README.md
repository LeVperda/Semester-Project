# Semester Project
 MLDE22 Semester Project, Spring 2023


How to use MySQL Server

The server is running on Hostinger, it is on Ubuntu 22.04, without GUI.

IP: 154.49.137.221

remote connection via Terminal:
- ssh root@154.49.137.221

All the root passwords (OS and MySQL) are: CheeseTax69

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