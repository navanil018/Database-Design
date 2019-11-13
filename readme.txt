Requirements
1)	Windows 10
2)	Google Chrome
3)	Python 3.7
4)	MySQL 5.7 – All Packages (Server, Client)
5)	Pymysql (pip install pymysql)
6)	Mysqlclient or MYSQL-python (pip install mysqlclient)
7)	Pandas (pip install pandas)
8)	Django (pip install Django)


Run python createTables.py to create database.
Run python initializeTables.py to populate the database.
After that type go to Library Management System folder where manage.py file is there.
Type, python manage.py makemigrations
Type, python manage.py migrate
To run server, type, python manage.py runserver
type 127.0.0.1:8000 in browser to run the application locally.