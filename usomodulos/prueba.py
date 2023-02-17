from sys import path

#path.append('C:\\Users\\usuario\\Dropbox\\sena2022\\Trimestre4-06octubre-17diciembre\\MiPracticaPythonA\\modulos')

path.append('..\\MiPracticaPythonA\\modulos')
import modulo1
from modulo1 import suml,prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulo1.suml(zeroes))
print(modulo1.prodl(ones))
