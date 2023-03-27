
import sqlite3
con=sqlite3.connect('pythonsqlite/pythondb.db')
micursor=con.cursor()

def seleccion(tabla, campo, operador,dato):
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista=micursor.execute(sentencia)
    return lista.fetchall()

#print(selects('persona','id','>','400'))

def modificar(tabla,campo,dato,id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE id={id}"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')

#modificar('persona','first_name','Faustino',2)

def eliminar(tabla,campo,dato):
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')

#eliminar('persona','first_name','Neda')

def insertar(tabla,id,fn,ln,mail):
    sentencia=f"INSERT INTO {tabla} VALUES ('{id}','{fn}','{ln}','{mail}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

insertar('persona',501,'Pablo','Marmol','marmol@mail.com')
seleccion('persona','id','=',501)