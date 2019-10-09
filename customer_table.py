### first ###
### install PyMySQL ###
### configure Apache by locating & updating httpd.conf ###
### should be in the ScriptAlias for the cgi; on mac it's preset to /Library/WebServer/CGI-Executables/
### change script's permissions in terminal:  sudo chmod 755 customer_table.py ###

#!/usr/local/bin/python3    use the absolute path of python interpreter ###
print("Content-Type: text/html")
print()

import pymysql
import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
a = form.getvalue('first_name')
b = form.getvalue('last_name')
c = form.getvalue('cid')
d = form.getvalue('customer_type')
e = form.getvalue('DOB')
f = form.getvalue('rewards')
print("Here is the updated Customers table:")

# Open connection to the database
db = pymysql.connect("localhost","root","password","project_folder",autocommit=True)

# Start a cursor object using cursor() method
cursor = db.cursor()

insert = f"""INSERT INTO Customers (first_name,last_name,cid,customer_type,DOB,rewards) VALUES
('{a}','{b}','{c}','{d}','{e}','{f}')"""
cursor.execute(insert)

sql_ret = "SELECT * FROM Customers;"
cursor.execute(sql_ret)

# Fetch all the rows using fetchall() method.
data = cursor.fetchall()
print(data)

# disconnect from server
db.close()
