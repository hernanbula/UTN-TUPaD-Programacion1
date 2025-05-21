#  Kata: Estructuras de Control (Bucles)

#  Ejercicio 1: Bucle for para números pares
#  Objetivo: Imprimir números pares usando un bucle for.
#  Instrucciones:
# 1. Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).
# 2. Usa un condicional o el paso del rango para lograrlo.
#  Preguntas de reflexión:
# • ¿Cómo modificarías el código para imprimir solo impares?
# • ¿Qué pasa si el rango fuera de 2 a 20 con paso 3?

for i in range(2,21,2):
    print(i)

for i in range(2,20,2):
    print(i+1)

for i in range(2,21,3):
    print(i)


# _________________________________________

# Ejercicio 2: Bucle while con suma acumulativa
#  Objetivo: Usar un bucle while para controlar una condición de salida.
#  Instrucciones:
# 1. Pide al usuario que ingrese números hasta que la suma supere 100.
# 2. Imprime la suma total al final.
#  Preguntas de reflexión:
# • ¿Qué ocurre si el primer número ingresado es mayor que 100?
# • ¿Cómo evitarías errores si el usuario ingresa texto?

suma = 0

while suma < 100:
    numero = (input("Ingrese un número para sumar al total: ")) 
    if numero.isdigit():
        suma = suma + float(numero)
    else:
        numero = (input("No ingrese un número válido. Ingréselo nuevamente para sumar al total: ")) 

print("La suma total es:", suma)


# _________________________________________

# Ejercicio 3: Filtrar palabras por letra inicial
#  Objetivo: Iterar sobre una lista y aplicar filtros.
#  Instrucciones:
# 1. Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), imprime
# solo las que empiezan con "a".
#  Preguntas de reflexión:
# • ¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también
# se cuente)?
# • ¿Qué método de strings es útil para esto?

frutas = ["manzana", "pomelo", "melon", "banana", "mandarina", "mango", "palta", "lechuga", "papa", "boniato"]
letra = "m"

for palabra in frutas:
    if palabra[0].lower() in letra:
        print(palabra)


# _________________________________________

#  Ejercicio 4: Tabla de multiplicar del 7
#  Objetivo: Usar un bucle para generar patrones.
#  Instrucciones:
# 1. Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).
#  Preguntas de reflexión:
# • ¿Cómo adaptarías el código para que el usuario elija la tabla?
# • ¿Qué estructura usarías para almacenar los resultados?

num = int(input("Ingrese un número para ver la tabla de multiplicar: "))
tabla = []
contador = 1

for i in range(1,11):
    tabla.append(num * i)
    print(num, "x", i, "=", num * i)

print(tabla)

for i in tabla:
    print(num, "x", contador, "=", i)
    contador += 1


# _________________________________________

#  Ejercicio 5: Contador de vocales
#  Objetivo: Contar caracteres específicos en un string.
#  Instrucciones:
# 1. Pide al usuario una cadena de texto.
# 2. Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.
#  Preguntas de reflexión:
# • ¿Cómo manejarías las vocales acentuadas (á, é)?
# • ¿Qué estructura de datos te ayudaría a optimizar el código?

palabra = input("Ingrese una palabra para contar sus vocales: ")
contador_vocales = 0

for i in range(len(palabra)):
    if palabra[i].lower() in "aáeéiéoóuú":
        contador_vocales += 1
print(f"La palabra {palabra} tiene {contador_vocales} vocales.")