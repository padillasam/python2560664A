class Persona:
    nacionalidad='Colombia'    
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
    # def __init__(self):
    #     self.nombre=''
    #     self.documento=0
    def datosinstancias(self):
        print('nombre: tipo de dato',type(self.__nombre))
        print('documento: tipo de dato',type(self.__documento))

    def datos(self):
        return self.__nombre+str(self.documento)
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    

ob1=Persona('ana',123)
ob2=Persona('Luis',321)
ob2.correo='luis@mail.com'
ob2.datosinstancias()
print(ob2.getNombre())
ob2.setNombre('Pedro')
print(ob2.getNombre())
print(ob2.correo)






class Aprendiz(Persona):
    def __init__(self,nombre,ficha):
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('Pedro',12345)
print(app.getFicha())
print(app.getNombre())
