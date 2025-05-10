# #  Ejercicio 1: Validación de contraseña
# #  Objetivo: Analizar un programa existente que verifica una contraseña.
# # Instrucciones:
# # 1. Lee el siguiente código y explica qué hace:
#     # contrasena_correcta = "programacion1"
#     # contrasena_usuario = input("Introduce la contraseña: ")
#     # if contrasena_usuario == contrasena_correcta:
#     #  print("Contraseña correcta. Bienvenido.")
#     # else:
#     #  print("Contraseña incorrecta. Intenta de nuevo.")
# #  Preguntas de reflexión:
# # • ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas?
# # • ¿Cómo mejorarías el programa para dar más intentos?

# contrasena_correcta = "programacion1"
# contrasena_usuario = (input("Introduce la contraseña: "))

# while contrasena_usuario != contrasena_correcta:
#     print("Contraseña incorrecta. Intenta de nuevo.")
#     contrasena_usuario = (input("Introduce otra contraseña: "))
#     contrasena_usuario = contrasena_usuario.lower()

# print("Contraseña correcta. Bienvenido.")


# # _________________________________________

# # Ejercicio 2: Identificador de vocales
# #  Objetivo: Clasificar caracteres usando condicionales.
# #  Instrucciones:
# # 1. Solicita una letra al usuario.
# # 2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra ingresada es una vocal".
# # 3. En otro caso, imprime: "La letra ingresada no es una vocal".
# #  Preguntas de reflexión:
# # • ¿Cómo manejarías vocales acentuadas (á, é)?
# # • ¿Qué estructura usarías para simplificar las comparaciones?

# letra = input("Ingrese una letra: ")

# if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
#     print("La letra ingresada es una vocal")
# else:
#     print("La letra ingresada NO es una vocal")


# # _________________________________________

# # Ejercicio 3: Clasificador de números
# #  Objetivo: Determinar el signo de un número.
# #  Instrucciones:
# # 1. Pide un número al usuario.
# # 2. Si es positivo, imprime: "El número es positivo".
# # 3. Si es negativo, imprime: "El número es negativo".
# # 4. Si es cero, imprime: "El número es cero".
# #  Preguntas de reflexión:
# # • ¿Qué ocurre si el usuario ingresa un texto?
# # • ¿Cómo adaptarías el código para números decimales?

# numero = input("Ingrese un número: ")

# if numero in "1234567890" or "-":
#     numero = float(numero)

#     if numero == 0:
#         print("El número es cero.")
#     elif numero > 0:
#         print("El número es positivo.")
#     else:
#         print("El número es negativo")

# else:
#     print("No ingresó un número.")


# # _________________________________________

# # Ejercicio 4: Comparador de números
# #  Objetivo: Comparar dos números con condicionales.
# #  Instrucciones:
# # 1. Solicita dos números al usuario.
# # 2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
# # 3. Si el primero es menor, imprime: "El primer número ingresado es menor".
# # 4. Si son iguales, imprime: "Los números ingresados son iguales".
# #  Preguntas de reflexión:
# # • ¿Cómo modificarías el programa para comparar más de dos números?
# # • ¿Qué pasa si se ingresan valores no numéricos? 

# numero1 = input("Ingrese un número: ")

# while not numero1.isdigit():
#     print("Error. No ha ingresado un número. Inténtelo de nuevo.")
#     numero1 = input("Ingrese un número: ")

# numero2 = input("Ingrese otro número para comparar con el primero: ")

# while not numero2.isdigit():
#     print("Error. No ha ingresado un número. Inténtelo de nuevo.")
#     numero2 = input("Ingrese un número: ")

# if numero1 == numero2:
#     print(f"Los números ingresados son iguales: {numero1} = {numero2}")
# elif numero1 > numero2:
#     print(f"El primer número ingresado {numero1} es mayor que el segundo {numero2}")
# else:
#     print(f"El segundo número ingresado {numero2} es mayor que el primero {numero1}" )


# # _________________________________________

# #  Ejercicio 5: Clima según temperatura
# #  Objetivo: Clasificar temperaturas en rangos.
# #  Instrucciones:
# # 1. Pide la temperatura actual en °C.
# # 2. Si es ≤ 10°C, imprime: "Hace frío".
# # 3. Si está entre 10°C y 25°C, imprime: "Está templado".
# # 4. Si es > 25°C, imprime: "Hace calor".
# #  Preguntas de reflexión:
# # • ¿Cómo adaptarías el programa para usar °F?
# # • ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?

# temperatura = float(input("Ingrese la temperatura actual en C°: "))

# celsius_or_fahrenheit = input("Ingrese ""C"" si quiere el resulado en celsius o ""F"" si lo quiere en fahrenheit: ")

# if celsius_or_fahrenheit.upper() == "F":
#     tempfinal = (temperatura * 9/5) + 32
# elif celsius_or_fahrenheit.upper() == "C":
#     tempfinal = temperatura
# else:
#     print("Ingresó otra letra que no es C ni F. Se calculará por defecto en celsius.")
#     tempfinal = temperatura

# if temperatura < 0:
#     print(f"Hace mucho frío: {tempfinal} C°.")
# elif temperatura <= 10:
#     print(f"Hace frío: {tempfinal} C°.")   
# elif temperatura > 10 and temperatura <= 25:
#     print(f"Está templado: {tempfinal} C°.")
# elif temperatura > 25 and temperatura < 35:
#     print(f"Hace calor: {tempfinal} C°.")
# else:
#     print(f"Hace mucho calor:{tempfinal} C°.")


# # _________________________________________

# #  Ejercicio 6: Detector de años bisiestos
# #  Objetivo: Aplicar condiciones compuestas.
# #  Instrucciones:
# # 1. Pide un año al usuario.
# # 2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se
# # ingresó un año bisiesto".
# # 3. En otro caso, imprime: "Se ingresó un año no bisiesto".
# #  Preguntas de reflexión:
# # • ¿Por qué el año 1900 no es bisiesto?
# # • ¿Cómo validarías que el año sea positivo?

# anio = int(input("Ingrese un año para saber si es bisieto: "))

# while anio < 1:
#     anio = int(input("Error. Ingresó un número negativo. Ingrese un año: "))

# if (anio % 4 == 0) and not(anio % 100 == 0) or (anio % 400 == 0):
#     print("Se ingresó un año bisiesto")
# else:
#         print("Se ingresó un año que no es bisiesto")


# # _________________________________________

# #  Ejercicio 7: Ajustador de frases
# #  Objetivo: Manipular strings con condicionales.
# #  Instrucciones:
# # 1. Pide una frase o palabra al usuario.
# # 2. Si no termina en punto, añádelo al final.
# # 3. Imprime el resultado.
# #  Preguntas de reflexión:
# # • ¿Cómo manejarías frases que terminan con espacios?
# # • ¿Qué otros caracteres de puntuación podrías considerar?

# frase = input("Ingrese una frase: ")

# if frase[-1] != ".":
#     print(f"{frase}.")
# else:
#     print("La frase tiene punto final")


# # _________________________________________

# #  Ejercicio 8: Validador de contraseña segura
# #  Objetivo: Implementar múltiples condiciones.
# #  Instrucciones:
# # 1. Pide al usuario que cree una contraseña.
# # 2. Verifica que cumpla:
# # o 8+ caracteres y ≤20 caracteres.
# # o Al menos 1 mayúscula (usa .isupper()).
# # o Al menos 1 número (usa .isdigit()).
# # 3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
# # 4. Si no, imprime: "La contraseña no es segura.".
# #  Preguntas de reflexión:
# # • ¿Cómo añadirías la regla de usar un carácter especial?
# # • ¿Por qué es importante limitar la longitud máxima?
# print("")
# print("_________________________________________")
# print("")
# print("Crea una contraseña con más de 8 caracteres y menos de 20. Al menos 1 mayúscula y al menos 1 número")

# pass_ok = False
# largo = False
# usa_num = False
# usa_mayuscula = False

# while pass_ok == False:
#     password = input("Ingrese su contraseña: ")
    
#     if (len(password) >= 8 and len(password) <= 20):
#         largo = True
#     print(f"¿Largo correcto?: {largo}: {len(password)}")

#     for letras in password:
#         if letras.isdigit():
#             usa_num = True
#     print(f"¿Usa número?: {usa_num}")

#     for letras in password:
#         if letras.isupper():
#             usa_mayuscula = True
#     print(f"¿Usa mayusculas?: {usa_mayuscula}")

#     if largo == True and usa_num == True and usa_mayuscula == True:
#         pass_ok = True
#         print("¡Felicitaciones! Creaste tu contraseña.")
#     else:
#         print("La contraseña no es segura. Intentelo nuevamente")
#         largo = False
#         usa_num = False
#         usa_mayuscula = False


# # _________________________________________

#  Ejercicio 9: Mejorando mensajes de error
#  Objetivo: Dar retroalimentación específica al usuario.
#  Instrucciones:
# 1. Basado en el Ejercicio 8, mejora los mensajes de error:
# o Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al
# menos 8 caracteres.".
# o Si tiene >20 caracteres: "...no más de 20 caracteres.".
# o Si falta mayúscula: "...al menos una mayúscula.".
# o Si falta número: "...al menos un número.".
#  Preguntas de reflexión:
# • ¿Cómo evitarías repetir código al verificar cada condición?
# • ¿Qué ventajas tiene este enfoque para el usuario?

