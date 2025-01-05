import pymysql as pmx
from pymysql import Error

try:
# establishing connection
    connection = pmx.connect(host="localhost", user="Shokori", password="max(1,2,3)is3", database="University")
except Error as e:
    print(e)
# creating cursor
cursor = connection.cursor()

""" the teacher asked to create a table called student with an id that is primary key and auto_increment
and a name column and salary. For the first part (I.)
"""
# creating a table called student with id, name and salary
student_table_command = "create table student(id int primary key auto_increment, name varchar(255), salary varchar(200));"
cursor.execute(student_table_command)
connection.commit()

"""I inserted the the data that was given to the table which covers the second part of the question (||.)"""
# Query to execute
command = "insert into Student(Name, salary) values('Ali', '1200k');"
command2 = "insert into Student(Name, salary) values('Ahmad', '23k');"
command3 = "insert into Student(Name, salary) values('Shirzad', '23k');"

# executing the command
cursor.execute(command)
cursor.execute(command2)
cursor.execute(command3)

#commiting afterwards
connection.commit()

connection.close()