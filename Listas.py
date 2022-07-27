# Las colecciones son un tipo de estructuras de datos
# Listas
'''
Es un conjunto de elementos
Recordar de que las posiciones de las listas comienzan desde cero.
'''
# Deficion de lista
# En las listas se pueden almacenar cualquier tipo de datos.
nombre = ['Juan', 'Kat', 'Ricardo', 'Maria']

# Imprimir
print(nombre)
# Imprimir de forma individual
# Para acceder de forma ascendente --->
print(nombre[0])
print(nombre[1])
print(nombre[2])
# Para acceder de forma desecendente <---
print(nombre[-1])
print(nombre[-2])
print(nombre[-3])
# Imprimir un rango
print(nombre[0:2])  # (posicion_inicio : posicion_final)

# Iterar una lista (Recorrer la lista)
for i in [1, 2, 3, 4, 5]:
    print("Hola Mundo")
# Otro ejemplo
for i in nombre:
    print(f'Su nombre es: {i}')
else:
    print('No existen más nombres en las listas ')

# Tamaño de la lista:
print('Tu lista contiene: ', len(nombre), 'Elementos')
# Agregar un nuevo elemento a la lista: funcion append()
nombre.append('Jorge')
print(nombre)
# Insertar un elemento en una determinada posición: función insert(posicion, <dato>)
nombre.insert(0, 'Damian')
print(nombre)
# Eliminar un elemento de la lista: funcion remove(<dato>)
nombre.remove('Damian')
print(nombre)
# Eliminar el ultimo valor agregado
nombre.pop()
print(nombre)
# Eliminar un indice
del nombre[0]
print(nombre)
# Eliminar todos los elementos de la lista
nombre.clear()
print(nombre)
# Borrar la lista por completo
del nombre
print(nombre)  # Sale error al imprimir porque eliminamos la lista
