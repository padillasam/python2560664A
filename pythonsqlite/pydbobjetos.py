from Persona import *
import sqlite3
lista=[]
with sqlite3.connect('pythonsqlite/pythondb.db')as con:
    micursor=con.cursor()
    new_sql="SELECT *  from persona"
    #print(micursor.execute(new_sql).fetchall())
    lista=micursor.execute(new_sql).fetchall()

personas=[]
for fila in lista:
    id=fila[0]
    nombre=fila[1]
    apellido=fila[2]
    mail=fila[3]
    ob=Persona(id,nombre,apellido,mail)
    personas.append(ob)

print(personas)

for p in personas:
    print(p.getNombreCompleto())


