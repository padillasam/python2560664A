def crear_calculadora(a,b):
    def calcular(*args, **kwargs):
        rtas=[]
        for op in args:
            if op == "+":
                #return a + b
                rtas.append(a + b)
            elif op == "-":
                #return a - b
                rtas.append(a - b)
            elif op == "*":
                #return a * b
                rtas.append(a * b)
            elif op == "/":
                if b != 0:
                    #return a / b
                    rtas.append(a / b)
                else:
                    return "Error: División por cero no permitida"
            else:
                return "Operador no válido"
        return rtas
    # Devolvemos la función interna calcular
    return calcular

# Usamos la función crear_calculadora para crear funciones específicas de cálculo
operacion = crear_calculadora(5,10)
# restar = crear_calculadora(5,10)
# multiplicar = crear_calculadora(5,10)
# dividir = crear_calculadora(5,10)

print(operacion('/','*','-','+'))
