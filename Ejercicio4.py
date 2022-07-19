'''
En el siguiente ejercicio se solicita calcular el area y el perimetro de un rectangulo, 
para ello debemos crear las siguientes variables:
alto (int)
ancho (int)

-El usuario debe proporcionar los valores de largo y ancho, y despues se debe imprimir el resultado
en el siguiente orden (formato):
Proporciona el alto:
Proporciona el ancho:
Area: <area>
Perimetro: <perimetro>
'''
# Codigo
alto = int(input('Proporciona el alto: '))
ancho = int(input('Proporciona el ancho:'))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area:', area)
print('Perimetro:', perimetro)
