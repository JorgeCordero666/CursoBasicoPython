# Tuplas
'''Es un conjunto ordenado e inmutable(no se puede modificar) de elementos del mismo o diferente tipo'''
# Definición
# Siempre se coloca una coma al final cuando se tiene un elemento
frutas = ('Naranja', 'Platano', 'Mandarina')
# Cantidad de elementos
print('La cantidad de elementos son: ', len(frutas))
print(frutas)
# acceder a un elemento en especifico
print(frutas[0])
# navegacion inversa
print(frutas[-1])
# acceder a un rango de valores
print(frutas[0:1])  # No se incluye el ultimo valor indicado

# Iterar una tupla

for fruta in frutas:
    print('La fruta que escogio fue:', fruta)

print('Las frutas escogidas fueron:', frutas[0], frutas[1], frutas[2])
'''Modificar una tupla'''
# 1. Convertir una tupla a una lista: función list()
frutasLista = list(frutas)
# 2. Modificar la lista
frutasLista[0] = 'Pera'
# 3.Convertir una lista a una tupla: función tuple()
frutas = tuple(frutasLista)
print(frutas)
