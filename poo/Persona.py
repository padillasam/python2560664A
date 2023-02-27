class Persona:
    def __init__(self,nombre):
        self.__nombre=nombre
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))
