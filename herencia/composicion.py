class Aprendiz:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[]
    def agregarCurso(self,nombreCurso):
        self.__cursos.append(nombreCurso)
    def verCursos(self):
        return self.__cursos

class Curso:
    def __init__(self,nombreCurso):
        self.__nombreCurso=nombreCurso

    def getNombreCurso(self):
        return self.__nombreCurso
    
ob=Aprendiz('Miguel')
c1=Curso('Python Basico')
c2=Curso('Python Intermedio')
c3=Curso('Java Basico')

ob.agregarCurso(c1)
ob.agregarCursso(c2)
ob.agregarCurso(c3)

for curso in ob.verCursos():
    print(curso.getNombreCurso())
