'''
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y 
pueden ir aumentando, traduciéndose en mejores beneficios. 
Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel           Puntuacion 
Inaceptable       0.0
Aceptable         0.4
Meritorio         0.6 o más 

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.
'''
usuario = input('Ingrese el nombre del usuario a quien quiere evaluar: ')
# la funcion float () convierte una cadena a decial
puntuacion = float(input('Ingrese la puntuacion obtenida: '))

if (puntuacion >= 0.6):
    print('Nivel de rendimiento meritorio')
elif (puntuacion == 0.4):
    print('Nivel de rendimiento aceptable')
elif (puntuacion == 0.0):
    print('Nivel de rendimiento inaceptable')
else:
    print('El valor ingresado no es permitido')
