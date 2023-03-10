from Aprendiz import *
from Curso import *

ap=Aprendiz('2560664A','Diego Suarez',123456)
c1=Curso('Python Intermedio',200)
c2=Curso('Python Avanzado',200)
#print(c1.getNombre())
ap.agregarCurso(c1)
ap.agregarCurso(c2)

for curso in ap.getCursos():
    print(curso.getNombre())
