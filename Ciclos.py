# Cliclo While
#condiciones = True

# while condiciones:
#    print('Ejecutando ciclo while')
# else:
#   print('Fin del ciclo while')


contador = 0
while contador < 3:
    contador += 1
    print(contador)
else:
    print('Fin del cliclo WHILE')
# Cliclo For
# El ciclo for(), permite iterar una lista de elementos o una cadena
'''
Un bucle for establece la variable iteradora en cada valor de una lista,
arreglo o cadena proporcionada y repite el código en el cuerpo del bucle 
for() para cada valor de la variable iteradora.

'''

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')
# Palabra reservada break
# Se usa para detener el programa en un punto que nosotros queramos

for letra in 'Holanda':
    if letra == "a":

        print("La letra encontrada es:", letra)
        break  # Si en caso que no se pusiera break se imprimiria dos veces la letra a

else:
    print('Fin ciclo for')

# Palabra reservada continue
for i in range(6):  # La funcion range(), estable un rango entre numeros
    if i % 2 != 0:
        continue  # Continue ejecuta la siguiente iteracion y ya no el resto del codigo
    print(f'Valor: {i}')
# Palabra reservada pass
number = 0

for number in range(10):
    if number == 5:
        pass    # pass here

    print('Number is ' + str(number))

print('Out of loop')
