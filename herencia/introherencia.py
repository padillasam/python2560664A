class Vehiculo:
    def __init__(self,tipo):
        self.tipo=tipo
    def descripcion(self):
        print('Soy generico no tengo descripcion',self.tipo)
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):
        return self.tipo
        #return Vehiculo.tipo
    def __str__(self):
        return 'Soy objeto de la clase Vehiculo'

class Herramienta:
    def __init__(self,proposito):
        self.__proposito=proposito
    def getProposito(self):
        return self.__proposito
    def __str__(self):
        return 'Soy objeto de la clase Herramienta'
class Terrestre(Vehiculo,Herramienta):
    def __init__(self,tipo,proposito):
        Herramienta.__init__(self,proposito)
        Vehiculo.__init__(self,tipo)        
    def datos(self):
        print('Tipo: ',super().getTipo())
        print('Tipo: ',super().getProposito())
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())


