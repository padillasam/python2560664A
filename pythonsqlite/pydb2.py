import sqlite3
with sqlite3.connect('pythonsqlite/pythondb.db')as con:
    micursor=con.cursor()
    new_sql="SELECT first_name,id from persona where id>250"
    print(micursor.execute(new_sql).fetchall())
   


