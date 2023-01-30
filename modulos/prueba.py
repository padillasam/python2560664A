import modulo1
from modulo1 import suml,prodl

print(modulo1.__counter)
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
x=[2,2,2,2,2]
y=[3,3,3,3,3]
print(suml(zeroes))
print(prodl(ones))
print(suml(x))
print(prodl(y))

print(modulo1.__counter)
