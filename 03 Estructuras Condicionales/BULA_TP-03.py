# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad.")


# 2) Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))

print("Aprobado" if nota >= 6 else "Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un número par: "))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12 and edad >= 0:
    print("Usted pertenece a la categoría Niño/a.")
elif edad >=12 and edad < 18:
    print("Usted pertenece a la categoría Adolescente.")
elif edad >=18 and edad < 30:
    print("Usted pertenece a la categoría Adulto/a joven.")
elif edad >= 30:
    print("Usted pertenece a la categoría Adulto/a.")
else:
    print("No ingresó un número válido (positivo).")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

key = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if len(key) > 7 and len(key) < 15:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# 6. escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla. 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

# Importamos paquetes y funciones que necesitamos utilizar
import random
from statistics import mode, median, mean # moda (mode), mediana (median) y media (mean) 

# Generamos lista de 50 números de forma aleatoria
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos moda, mediana y media de lista de numeros_aleatorios
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Teniendo en cuenta la siguiente serie de 50 números aleatorios: ", numeros_aleatorios)

print(f"y su moda {moda}, mediana {mediana} y media {media} se determina que: ") 

if media == mediana == moda:
    print(" ● No hay sesgo")
elif media > mediana and mediana > moda:
    print(" ● Hay Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print(" ● Hay Sesgo negativo o a la izquierda")
else:
    print(" ● No se pudo determinar el sesgo.")


# 7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# cadena [inicio:final:pasos]
    # inicio- El índice inicial donde empezara la subcadena- por defecto es 0.
    # final- El índice final, donde terminara la subcadena - por defecto, es -1.
    # salto o paso- Número que indicara los saltos que seguirá la secuencia o subcadena. Por defecto es 1.

frase = input("Ingrese una palabra o frase: ")
cantidad_letras = len(frase);
ultima_letra = frase[-1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u": 
	print(frase,"!")
else:
	print(frase)

# Solución más sintética:
if frase[-1] in "AEIOUaeiou":
  print(frase,"!")
else:
  print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
    # 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    # 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    # 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("Ingrese el número 1, 2 o 3 dependiendo de la opción que desee:")
print("   ● 1. Si quiere su nombre en mayúsculas")
print("   ● 2. Si quiere su nombre en minúsculas.")
print("   ● 3. Si quiere su nombre con la primera letra mayúscula")

opcion = input()

if opcion == "1":
    print(str.upper(nombre))
elif opcion == "2":
    print(str.lower(nombre))
elif opcion == "3":
    print(str.title(nombre))
else:
    print("Ingreso un número invalido. Debe ingresar opción 1, 2 o 3.")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_Richter = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_Richter < 3 and magnitud_Richter >= 0:
    print(f"La magnitud del sismo {magnitud_Richter} es MUY LEVE según la escala de Richter")
elif magnitud_Richter >= 3 and magnitud_Richter < 4:
    print(f"La magnitud del sismo {magnitud_Richter} es LEVE según la escala de Richter")
elif magnitud_Richter >= 4 and magnitud_Richter < 5:
    print(f"La magnitud del sismo {magnitud_Richter} es MODERADO según la escala de Richter")
elif magnitud_Richter >= 5 and magnitud_Richter < 6:
    print(f"La magnitud del sismo {magnitud_Richter} es FUERTE según la escala de Richter")
elif magnitud_Richter >= 6 and magnitud_Richter < 7:
    print(f"La magnitud del sismo {magnitud_Richter} es MUY FUERTE según la escala de Richter")
elif magnitud_Richter >= 7:
    print(f"La magnitud del sismo {magnitud_Richter} es EXTREMO según la escala de Richter")
else:
    print("Ha ingresado un número negativo. Intente nuevamente.")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese si está en el hemisferio norte (N) o sur (S): ")
mes = int(input("Ingrese el número de mes actual (1 a 12): "))
dia = int(input("Ingrese el número de dia del mes actual (1 a 31): "))

# Periodos del año
    # 21 de marzo hasta el 20 de junio (incluidos)
    # 21 de junio hasta el 20 de septiembre (incluidos)
    # 21 de septiembre hasta el 20 de diciembre (incluidos)
    # 21 de diciembre hasta el 20 de marzo (incluidos)

if (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en Primavera.")
    else:
        print("Usted se encuentra en Otoño.")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en Verano.")
    else:
        print("Usted se encuentra en Invierno.")
elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en Otoño.")
    else:
        print("Usted se encuentra en Primavera.")
elif (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en Invierno.")
    else:
        print("Usted se encuentra en Verano.")
else:
    print("Usted ingresó mal el Hemisferio o un número erroneo de mes o dia")


