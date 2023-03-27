import sqlite3
con=sqlite3.connect('C:\\padilla\\sqlite-tools\\db\\python.db')
print(type(con))
micursor=con.cursor()
print(type(micursor))