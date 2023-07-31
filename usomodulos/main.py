import sys
from sys import path
path.append('..\\MiPracticaPythonA\\modulos')

#path.append('C:\\Users\\usuario\\Dropbox\\sena2022\\Trimestre4-06octubre-17diciembre\\MiPracticaPythonA\\modulos')

import module
from modulo1 import suml,prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
