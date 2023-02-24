try:
    #raise ZeroDivisionError
    print(1/0)
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:
    print(zde)
    #print('prueba error')