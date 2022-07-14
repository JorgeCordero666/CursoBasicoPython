# Tipos de datos
'''Numericos, Diccionario, Booleanos, set, tipos de secuencia'''
'''!!!Una variable puede tener varios tipos de datos¡¡¡'''
# Tipo Numerico
x: int = 10  # Indicar el tipo de variable (:)
print(x)
type(x)  # funcion que indica el tipo de variable que es
print(type(x))

# Tipo Cadena
a = "Hola Mundo"
print(a)
type(a)  # Indicar el tipo de variable que es
print(type(a))

# Tipo flotante
decimal = 10.5
print(decimal)
type(decimal)  # Indicar el tipo de variable que es
print(type(decimal))

# Tipos Booleanos
v = True
f = False
print(v)
print(f)
type(v)
type(f)
print(type(v))
print(type(f))

# Manejo de cadenas
miGrupoFavorito = "SFDK"
comentario = "y es el mejor del mundo "
print(miGrupoFavorito)
# La concatenacion es unir cadenas
print("Mi grupo favorito es: " + miGrupoFavorito +
      " " + comentario)  # Forma 1 con el (+)
print("Mi grupo favorito es:", miGrupoFavorito,
      comentario)  # Forma 2 con la (,)

# Convertir de cadena a entero para realizar operaciones numericas
numero1 = "1"
numero2 = "2"
print('Concatenacion:', numero1 + numero2)

# Forma 1: Utilizando la funcion int() dentro de la funcion print()
print('Operacion numerica:', int(numero1)+int(numero2))

# Variables booleanas
miVariable = 3 > 2
print(miVariable)
# Las variables booleanas se utilizan en condicionales para tomar decisiones
if miVariable:
    print('El resultado fue verdadero')
else:
    print('El resultado fue falso')
