# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
# “Hola Mundo!”. Llamar a esta función desde el programa principal.

# ------------------------
#  Definición de funciones
def imprimir_hola_mundo():
    print("Hola mundo")

# ------------------------
# Main
imprimir_hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# ------------------------
#  Definición de funciones

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

# ------------------------
# Main

saludar_usuario(input("Ingrese su nombre: "))


# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# ------------------------
#  Definición de funciones

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def solicitar_dato(variable):
    variable = input(f"Ingrese {variable}: ")
    return variable
# ------------------------
# Main

nombre = solicitar_dato("nombre")
apellido = solicitar_dato("apellido")
edad = solicitar_dato("edad")
residencia = solicitar_dato("residencia")

informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# Calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

from math import pi
# ------------------------
#  Definición de funciones

def calcular_area_circulo(radio):
    area = round((pi * radio ** 2), 2)
    print(f"El área de un círculo con {radio} cm de radio es de: {area} cm².")
    
def calcular_perimetro_circulo(radio):
    perimetro = round((pi * radio * 2), 2)
    print(f"El perímetro de un círculo con {radio} cm de radio es de: {perimetro} cm.")

# ------------------------
# Main

radio = int(input("Ingrese el radio en cm para calcular el área y el perímetro del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# ------------------------
#  Definición de funciones

def solicitar_dato_numerico(variable):
    variable = int(input(f"Ingrese {variable}: "))
    return variable

def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60 # 1 hora = 60 minutos = 3600 segundos
    print(f"{segundos} segundos corresponde a {horas} horas")
    seg = segundos % 60
    minutos = (segundos // 60) % 60
    horas = round((segundos / 60) // 60)
    print(f"Lo cual corresponde a {horas} horas, {minutos} minutos y {seg} segundos")

# ------------------------
# Main
print("Para calcular a cuantas horas equivalen una cantidad de segundos:")
segundos_a_horas(solicitar_dato_numerico("segundos"))


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
# e imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# ------------------------
#  Definición de funciones

def solicitar_dato_numerico(variable):
    variable = int(input(f"Ingrese un n° de {variable}: "))
    return variable

def tabla_multiplicar(numero):
    for i in range(0, 11):
        producto = numero * i
        print(f"{numero} x {i} = {producto}")

# ------------------------
# Main

print("Para concer la tabla de multiplicar: ")
tabla_multiplicar(solicitar_dato_numerico("tabla"))


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# tupla = (suma, resta, multiplicacion, division)

# ------------------------
#  Definición de funciones

def leer_numero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n

def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    producto = a*b
    division = a/b

    resultados = (suma, resta, producto, division)

    return resultados

# ------------------------
# Main

a = leer_numero_validado("Ingrese un número entero que no sea 0", 1)
b = leer_numero_validado("Ingrese otro número entero que no sea 0", 1)
resultados = operaciones_basicas(a, b)
print(resultados)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# IMC = peso en kg / (altura en m)²

# ------------------------
#  Definición de funciones

def calcular_imc(peso, altura):
    imc = round((peso / (altura)**2),2)
    print(f"Su índice de masa corporal es {imc}")

# ------------------------
# Main

peso = float(input("Ingrese su peso en kgs: "))
altura = float(input("Ingrese su altura en mts: "))
calcular_imc(peso, altura)


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# ------------------------
#  Definición de funciones

def leer_float_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n

def celsius_a_fahrenheit(celsius):
    fahrenheit = 9/5 * celsius + 32
    print(f"{celsius} grados Celsius equivalen a {round(fahrenheit,2)} grados Fahrenheit")

# ------------------------
# Main
temp_min = -273.15 # Cero absoluto: 0 Kelvin (K) = -273.15 °C
temp_max = 1.41679 * (10 ** 32) # Temperatura máxima teórica (límite de Planck) 1.41679 × 10³² Kelvin
celsius = leer_float_validado("Ingrese la temperatura en grados celsius (entre el mínimo posible -273.15 C° y el máximo teórico 1.41679 x 10³² C°)", temp_min, temp_max)
celsius_a_fahrenheit(celsius)


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
# devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# ------------------------
#  Definición de funciones

def calcular_promedio(a, b, c):
    promedio = (a+b+c) / 3
    print(f"El promedio de los tres números ingresados es {promedio}")

# ------------------------
# Main

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
num3 = float(input("Ingrese un tercer número: "))

calcular_promedio(num1,num2,num3)