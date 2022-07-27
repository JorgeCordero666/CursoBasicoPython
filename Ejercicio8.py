# Formas de utilizar la funcion range()
# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numerios divisibles entre 3
for i in range(10):
    if i % 3 == 0:
        print(i)
else:
    print("Fin del programa")

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimirlos

for i in range(2, 7):
    print(i)
else:
    print('Se acabo el programa')
# Ejercicio 3: Crear un rango de 3 a 10, pero con incremento de 2 en 2

for i in range(3, 11, 2):
    print(i)
else:
    print('Fin del programa')
