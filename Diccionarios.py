# Diccionarios
'''
Es una coleccion que nos permite almacenar una serie de mapeos entre dos conjuntos de elementos,
llamados key and values 
'''
# Definición
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Mnagement System'
}
print(diccionario)
# Cantidad de elementos
print('Cantidad de elementos de tu diccionario es: ', len(diccionario))
# Acceder a un elemento se debe proporcionar la clave
print(diccionario['IDE'])
# Modificar elementos
diccionario['IDE'] = 'integrated development environment'
# Recorrer los elementos de un diccionario (LLAVE)
for termino in diccionario:
    print(f'las claves son: {termino}')
# Recorrer los elementos de un diccionario (LLAVE, VALOR)

for termino, valor in diccionario.items():
    print(termino, valor)

# Recorrer solo las llaves
for clave in diccionario.keys():
    print(clave)
# Recorrer solo los valores
for i in diccionario.values():
    print(i)
# agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
# Eliminar un elemento: método pop
diccionario.pop('DBMS')
print(diccionario)
# Limpiar un diccionario
diccionario.clear()
