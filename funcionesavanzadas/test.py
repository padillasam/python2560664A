# Definimos una función llamada crear_calculadora que toma un operador como argumento
def crear_calculadora(operador):
    def calcular(a, b):
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b != 0:
                return a / b
            else:
                return "Error: División por cero no permitida"
        else:
            return "Operador no válido"
    
    # Devolvemos la función interna calcular
    return calcular

# Usamos la función crear_calculadora para crear funciones específicas de cálculo
sumar = crear_calculadora("+")
restar = crear_calculadora("-")
multiplicar = crear_calculadora("*")
dividir = crear_calculadora("/")

resultado_resta = restar(20, 7)         # 
resultado_multiplicacion = multiplicar(6, 4)  # 
resultado_division = dividir(8, 2)      # 

# Imprimimos los resultados
print("Resultado de la suma:", sumar(10, 5))
print("Resultado de la resta:", resultado_resta)
print("Resultado de la multiplicación:", resultado_multiplicacion)
print("Resultado de la división:", resultado_division)





# # las funciones pueden retornar un tipo de dato es decir se puede hacer una funcion que complemente otra
# #  retornando el parametro que nececita la otra ella no sabe que es un funcion la que le entrega el dato 
# # a la funcion solo le interesa tener un dato 


# def cifra(palabra): #la funcion va a cifar y retona la litas donde se van a almacenar los numeros 
#     numeros = []

#     for caracter in palabra:
#         valor = ord(caracter)
#         numeros.append(valor)

#     return numeros


# # cifra("hola")

# def decifra(numeros): # y esta fucion recibe un lista como parametro  y imprime la lita que entrega la funcion cifra() 
#     cadena = ''.join(map(chr, numeros)) 
#     print(numeros,"\n","-"*len(cadena))
    
#     print (cadena) # imprime la lista y el descifrado
    
    
# lista=cifra("hola")
# decifra(lista)
# decifra(cifra("hola"))

# # #Explique el uso de argumentos de tipo posicionales (*args) y argumentos clave (**kwargs). 
# # #Escriba dos ejemplos con el código comentariado con la explicación

# # #1 Si a es multiplo de b. 
# # def EsMultiplo(a,b): #definimos una funcion con argumentos posicionales  los cuales son a y b. 
# # 	if a % b == 0: #hacemos una condicion para verificar si a es multiplo de b. 
# # 		print(a,'es multiplo de',b) #imprime si la condicion se cumple. 
# # 	elif b % a == 0: #usamos la condicion elif por si b es multiplo a. 
# # 		print(b,'es multiplo de',a) #imprime si esta condicion se cumple. 
# # 	else:
# # 		print('Ninguno es multiplo ¡ERROR!') #si ninguna de las condiciones se cumple imprime ¡ERROR! en la consola.
# # EsMultiplo(4,2) #llamamos la funcion y pasamos los dos argumento que a=4 y b=2, los dos son multiplos asi que no hay nigun error. 

# # #2 pasar varios datos a **kargs. 
# # def imprimir_datos(**kargs): #definimos la funcion imprimir_datos como argumento **kargs que puede recibir cantidad de argumentos. 
# # 	for clave, valor in kargs.items(): #el for establece una variable = clave para almacenar el (nombre del argumento) para almacenar el valor. 
# # 		print(f'{clave}: {valor}') #imprime la clave y valor en la consola 
# # imprimir_datos(nombre = "Nicolas", edad=19, ciudad="Bogota") #llamamos la funcion imprmir_datos con argumentos kargs
# # # el bucle for iterara a traves de los elemtos del diccionario.
