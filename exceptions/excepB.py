values = (1, 0)
#x,y=10,12
#print(divmod(10,3))
try:
    q, r = divmod(*values)
    #print('valor de q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)

