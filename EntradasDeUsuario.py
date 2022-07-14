# Funcion input()
'''Sirve para procesar la entrada de datos del usuario'''
# La funcion input procesa datos de tipo string (Cadena)
resultado = input('Ingrese una palabra: ')
print('Valor proporcionado:', resultado)
print("Fin del programa")

# Procesar datos de tipo numerico

# Forma 1: En la misma variable utilizar la funcion int() y dentro de ella la funcion input()
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input('Escribe el segundo numero: '))
suma = numero1 + numero2
print('Forma 1: La suma de esos dos numeros es:', suma)
