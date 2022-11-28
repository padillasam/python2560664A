import random
#intervalo=int(random.randint(-100,100))
x=int(random.randrange(100))
y=int(random.randrange(100))
print('x= ',x)
print('y= ',y)
if x<y:
    x,y=y,x
if x%y==0:
    print(x,'es multiplo de ',y)
else:
    print(x,'No es multiplo de ',y)


