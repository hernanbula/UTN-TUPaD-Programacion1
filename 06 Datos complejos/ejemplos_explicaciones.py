#Ejemplos explicaciones video


#LISTAS

# #split

frase = input("Ingrese una frase: ")

lista_palabras = frase.split()

print(lista_palabras)

# concatenacion de listas

lista_concatenada = lista_palabras + list(range(5,0,-1)) + ["Despegue", True]

print(lista_concatenada)

# comprobar si un valor está en la lista

# Se usa el término in

print(f"Está la palabra cuenta en la lista: {"cuenta" in lista_concatenada}")

print(f"Está el número 1 en la lista: {1 in lista_concatenada}")

# TUPLAS
# Es igual a la lista, pero son inmutables y se definen con paréntesis
# no son mutables

tupla = ("Hola", 2, 3.5, True)

print(tupla[0])

# tuple convierte una lista en tuple

lista_a_tupla = tuple(lista_concatenada)

print(f"Lista convertida en tupla {lista_a_tupla[0:3]}")

# list convierte una tupla en lista

tupla_a_lista = list(lista_a_tupla)

tupla_a_lista.append("Tupla convertida a lista")

print(tupla_a_lista)

# SETS
# Coleccion de elementos del mismo tipo de datos.
# No admiten elementos duplicados.
# Son mutables 
# No se puede hacer slicing en los sets

mi_set = {33,4,5,6,22,43,5,77,89,123,4,5,77,77}

print(mi_set) # Elimina los duplicados {33, 4, 5, 6, 43, 77, 22, 89, 123}

# Se puede verificar si aparece un elemento en un set con operado ir

print(77 in mi_set)
print(8 in mi_set)

# DICCIONARIOS
# almacenand atos en pares key-value
# no están ordenados
# indexing a través de keys unicas
# admite diferentes tipos de datos

nombre_diccionario = {"key1": 1, "key2": 2}

colores = {"azul":"blue", "negro": "black", "rosado": "pink"}
print(colores)
print(colores["negro"])

# Metodos con diccionarios

#recuperar valores
print(colores.values())

# recuperar keys
print(colores.keys())

# elegir un elemento utilizando key
print(colores["rosado"])

# modificar los valores de una key
colores["azul"] = "Light blue"
print(colores)

# agregar nuevo key-value
colores["rojo"] = "red"
print(colores)