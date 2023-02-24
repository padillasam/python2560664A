def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 'a'))