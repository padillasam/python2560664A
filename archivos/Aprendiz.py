class Aprendiz:
    def __init__(self,fname,lname,email,idAprendiz):
        self.__fname=fname
        self.__lname=lname
        self.__email=email
        self.__idAprendiz=idAprendiz
    def nombreCompleto(self):
        return self.__fname+' '+self.__lname
