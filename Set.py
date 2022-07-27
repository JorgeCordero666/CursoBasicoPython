# Set
'''Es una coleccion que no posee orden y tampoco numeros de indice, 
   los elementos apareceran de forma aleatoria al imprimirlos,
   tampoco soporta documentos duplicados.
'''
# Definicion
planetas = {'Marte', 'Jupeter', 'Venus'}
print(planetas)
# Verificar si un elemento esta presente
print('Marte' in planetas)
# Agregar más elementos  con el metodo add()
planetas.add('Tierra')
print(planetas)
# Eliminar un elemento
planetas.remove('Tierra')
print(planetas)
# Limpiar todos los elementos del set
planetas.clear()
print(planetas)
# Eliminar por completo el set
del planetas
