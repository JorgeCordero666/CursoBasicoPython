# Para entender el funcionamiento ejecutar en modo Debug
numero = 0
while numero <= 10:
    suma = numero + 1
    numero += 1
print('La suma es: ', str(suma))

# Imprimir numeros del 0 al 5
i = 0
while i < 6:  # Para utilizar el numero cinco se debe usar el operador (<=)
    print(i)
    i += 1
else:
    print('Fin de la ejecucion')

# Imprimir numeros de 1 al 5 de forma descendente
j = 5
while j >= 1:
    print(j)
    j -= 1
else:
    print('La ejecucion ha terminado')
