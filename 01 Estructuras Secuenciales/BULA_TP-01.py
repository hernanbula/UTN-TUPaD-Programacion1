# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA

# Programación 1
# Profesor: Prof. Cinthia Rigoni
# Tutor: Prof. Martín A. García

# Práctico 1: Estructuras secuenciales
# Estudiante: Hernán E. Bula


# Actividades

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
# realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área su perímetro.
radio = int(input("Ingrese el radio del círculo para calcular su área y perímetro:"))
pi = 3.14159
area = pi * radio * radio
perimetro = pi * radio * 2
print(f"Un círculo de un radio de {radio}, tiene un área de {area} y un perimetro de {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese los segundos para calcular a cuantas horas equivale: "))
horas = (segundos / 60) / 60 # 1 hora = 60 minutos = 3600 segundos
print(f"{segundos} segundos corresponde a {horas} horas")
seg = segundos % 60
minutos = (segundos // 60) % 60
horas = round((segundos / 60) // 60)
print(f"Lo cual corresponde a {horas} horas, {minutos} minutos y {seg} segundos")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un número para saber la tabla de multiplicar: "))
for i in range(0, 11):
    producto = numero*i
    print(f"{numero} x {i} = {producto}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese un número entero que no sea 0: "))
num2 = int(input("Ingrese otro número entero que no sea 0: "))
suma = num1+num2
division = num1/num2
producto = num1*num2
resta = num1-num2
print(f"el resultado de sumar ambos números es {suma}, de dividirlos {division}, de multiplicarlos {producto} y de restarlos {resta}.")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
        # IMC = peso en kg / (altura en m)²
altura = float(input("Ingrese su altura en mts: "))
peso = float(input("Ingrese su peso en kgs: "))
imc = peso / (altura)**2
print(f"Su índice de masa corporal es {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
        # Temperatura en Fahrenheit = 9/5 * Temperatura en Celsius + 32
celsius = float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = 9/5 * celsius + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
num3 = float(input("Ingrese un tercer número: "))
promedio = (num1+num2+num3) / 3
print(f"El promedio de los tres números ingresados es {promedio}")
