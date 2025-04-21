# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

contador_digitos = 0
num = int(input("Ingrese un número entero para calcular la cantidad de dígitos: "))

while num > 0:
    contador_digitos += 1
    num = num // 10
print("El numero ingresado contiene",contador_digitos,"dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

num_min = int(input("Ingrese un número mínimo: "))
num_max = int(input("Ingrese un número máximo: "))
suma = 0

for i in range(num_min+1,num_max):
    suma += i

print("La suma de los n° comprendidos entre los 2 valores ingresados (excluyendo esos dos valores) es:",suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

acumulador = 0

num = int(input("Ingrese un número a sumar (use 0 para finalizar): "))

while num !=0:
    acumulador += num
    num = int(input("Ingrese otro número a sumar (use 0 para finalizar): "))

print("El total de la suma de los numeros ingresados es: ",acumulador)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

contador_intentos = 1
adivinar = random.randrange(10)

num_usuario = int(input("Ingrese un número entre 0 y 9 para adivinar: "))

while num_usuario != adivinar:
    contador_intentos += 1
    num_usuario = int(input("Ingrese otro número entre 0 y 9 para adivinar: "))

print("El usuario necesitó",contador_intentos,"intentos para acertar al número",adivinar)


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100,-1,-1):
    if i % 2 == 0:
        print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 
# y un número entero positivo indicado por el usuario.

acumulador = 0

num = int(input("Ingrese un número entero positivo: "))

while num < 0:
    num = int(input("ERROR. Ingrese un número entero positivo: "))

for i in range(num+1):
    acumulador += i

print("El total de la suma de los numeros comprendidos entre 0 y el n° ingresado es: ",acumulador)


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

RANGO = 10 # Cambiar a 100 para procesar 100 números
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(RANGO):
    num = int(input("Ingrese el valor número " + str(i) + ": "))
    
    if num < 0:
        negativos += 1
    else:
        positivos += 1
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Se ingresaron {pares} números pares, {impares} impares, {negativos} número negativos y {positivos} positivos.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

from statistics import mean

RANGO = 10 # Cambiar a 100 para procesar 100 números
lista = []

for i in range(RANGO):
    num = int(input("Ingrese el valor número " + str(i+1) + ": "))
    lista.append(num)

media = mean(lista)

print ("La media de los valores ingresados es: ", media)
    

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

inverso = 0

numero = int(input("Ingrese un número para invertir sus dígitos: "))
num = numero

while num != 0:
    digito = num % 10
    inverso = inverso * 10 + digito
    num = num // 10

print(f"Los dígitos invertidos del número {numero} son: {inverso}")