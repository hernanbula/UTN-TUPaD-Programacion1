# # Práctico 6: Estructuras de datos complejas  

# # Objetivo: Dominar el uso de estructuras de datos complejas en Python 
# # para almacenar, organizar y manipular datos de manera eficiente, 
# # aplicando buenas prácticas y optimizando el rendimiento de las aplicaciones. 

# # BULA, Hernán Enrique

# # 1) Dado el diccionario precios_frutas 

# # Añadir las siguientes frutas con sus respectivos precios: 
# # ● Naranja = 1200 
# # ● Manzana = 1500 
# # ● Pera = 2300 

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':  1450} 

# precios_frutas['Naranja'] = 1200 
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300


# # 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# # desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# # ● Banana = 1330 
# # ● Manzana = 1700 
# # ● Melón = 2800 

# precios_frutas['Banana'] = 1330 
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800


# # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
# # en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

# lista_precios = list(precios_frutas.values())
# print(lista_precios)


# # 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# # • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# # • Luego, pedí un nombre y mostrale el número asociado, si existe. 

# # ----------------------
# # Funciones
# # ----------------------

# def busqueda_contacto():
#     busqueda = None
#     while busqueda != "0":
#         busqueda = input("Ingrese un nombre para buscar el teléfono de contacto. Si quiere salir ingrese 0: ")
#         if busqueda in guia_telefonica:
#             print(f"El número de {busqueda} es {guia_telefonica[busqueda]}")
#         else:
#             print(f"No existe un contacto con el nombre {busqueda}")

# def es_numero():
#     numero = input("Ingrese el número de teléfono: ")
#     while not numero.isdigit():
#         print("Error: El teléfono debe contener solo números.")
#         numero = input("Ingrese el número nuevamente: ")
#     return numero

# # ----------------------
# # Main
# # ----------------------

# contacto = None
# guia_telefonica = {'Hernán': '123456', 'Vane': '65432', 'Laia': '3454321', 'Mar': '0987654', 'Nadia': '345678976543'}

# print("Si quiere, puede incorporar nuevos datos a la guía de telefónica, sino ingrese 0 y sale.")
# while contacto != "0":
#     contacto = input("Ingrese el nombre del contacto: ")
#     if contacto == "0":
#         break
#     guia_telefonica[contacto] = es_numero()

# print(guia_telefonica)

# busqueda_contacto()


# # 5) Solicita al usuario una frase e imprime: 
# # • Las palabras únicas (usando un set). 
# # • Un diccionario con la cantidad de veces que aparece cada palabra. 

# frase = input("Ingrese una frase: ").lower()
# palabras = frase.split()
# print(f"Todas las palabras usadas en la frase son: {palabras}")

# palabras_unicas = set(palabras)
# print(f"Las palabras utilizadas en la frase (sin repetir) son: {sorted(palabras_unicas)}")

# veces_palabra = {}
# for palabra in palabras:
#     if palabra in veces_palabra:
#         veces_palabra[palabra] += 1
#     else:
#         veces_palabra[palabra] = 1
# print(veces_palabra)


# # 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# # Luego, mostrá el promedio de cada alumno. 

# estudiantes = {}
# promedio_estudiantes = {}

# for i in range(3):
#     nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
#     notas = []
#     for i in range(3):
#         nota = int(input(f"Ingrese la nota {i+1}: "))
#         notas.append(nota)
#     estudiantes[nombre] = tuple(notas)
#     promedio_estudiantes[nombre] = sum(notas)/len(notas)

# print(f"Las notas de los estudiantes son:")

# for estudiante in promedio_estudiantes:
#     print(f"Las notas de {estudiante} son {estudiantes[estudiante]} lo que da un promedio de {promedio_estudiantes[estudiante]}")


# # 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
# # • Mostrá los que aprobaron ambos parciales. 
# # • Mostrá los que aprobaron solo uno de los dos. 
# # • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

# # En realidad lo que hago es dado dos sets de nombres, representando dos listas de estudiantes 
# # que aprobaron el Parcial 1 y el Parcial 2, respectivamente. Cambie numeros por nombres para que sea más realista.

# parcial1 = {"Karlys", "Nadia", "Agustina", "Luciana", "Malena", "Carolina", "Rocío", "Emilia", "Isabella Adelina", "Juan", "Bautista", "Luz Catalina"}
# parcial2 = {"Joaquin", "Malena", "Manuela", "Luz Catalina", "Milagros", "Carolina","Rocío", "Emilia", "Juan"}

# ambos_parciales = parcial1.intersection(parcial2)

# print(f"Aprobaron ambos parciales {len(ambos_parciales)}: {ambos_parciales}")

# un_parcial = parcial1 ^ parcial2 # un_parcial = set((parcial1.difference(parcial2)).union((parcial2.difference(parcial1))))

# print(f"Aprobaron solo un parcial {len(un_parcial)}: {un_parcial}")

# al_menos_un_parcial = parcial1.union(parcial2)

# print(f"Aprobaron al menos un parcial {len(al_menos_un_parcial)}: {al_menos_un_parcial}")


# # 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# # Permití al usuario: 
# # • Consultar el stock de un producto ingresado. 
# # • Agregar unidades al stock si el producto ya existe. 
# # • Agregar un nuevo producto si no existe. 

# # ----------------------
# # Funciones
# # ----------------------
# #
# #  Función para solicitar al usuario número entero validado y configurar el mensaje, minimo y máximo
# def leer_numero_validado(mensaje, min = float("-Inf"), max = float("Inf")): 
#     n = int(input(f"{mensaje}: "))
#     while n < min or n > max:
#         n = int(input(f"ERROR. {mensaje}: "))
#     return n

# # Función para solicitar al usuario la opción de menu entre 1, 2 o 3
# def leer_opcion_menu():
#     opcion = None
#     valida = False
#     print(f"\n{("-"*65)}\n Ingrese la opción de la acción que necesite realizar: \n\n 1: imprimir lista de productos y stock \n 2: consultar stock de un producto \n 3: agregar producto y/o stock \n 0: SALIR.\n")
#     while not valida:
#         opcion = input("Seleccione opción (1/2/3) o 0 para salir: ")
#         if opcion in {'1', '2', '3'}:
#             valida = True
#         elif opcion == "0":
#             return "0"
#         else:
#             print("ERROR: Debe ser 1, 2 o 3")
#     return int(opcion)

# # Función para solicitar al usuario la opción Si o No
# def leer_si_no(mensaje):
#     while True:
#         opcion = input(f"\n{mensaje} (S/N): ").strip().upper()
#         if opcion == "S":
#             return True
#         elif opcion == "N":
#             return False
#         else:
#             print("ERROR: Por favor ingrese solo 'S' o 'N'")

# # Función para consultar stock
# def consulta_stock():
#     busqueda = None
#     while busqueda != "0":
#         busqueda = input("\nIngrese un nombre del producto para consultar su stock. Si quiere salir ingrese 0: ")
#         if busqueda == "0":
#             break
#         elif busqueda in productos_stock:
#             imprimir_producto(productos_stock, busqueda)
#         else:
#             print(f"No existe el producto con el nombre {busqueda}")

# # Función para imprimir la lista anidada en formato tabla
# def imprimir_lista(lista): 
#         print("\n")
#         print("-"*45)
#         print(f"|  {'PRODUCTO':<30} | {'STOCK':>6}  |")
#         print("-"*45)
#         for producto in lista:
#             print(f"|  {producto:<30} | {lista[producto]:>6}  |")
#         print("-"*45)

# # Función de imprimir un artículo de una lista en formato tabla. Se adaptó la función imprimir_lista(lista)
# def imprimir_producto(lista, producto):
#         print("\n")
#         print("-"*45)
#         print(f"|  {'PRODUCTO':<30} | {'STOCK':>6}  |")
#         print("-"*45)
#         print(f"|  {producto:<30} | {lista[producto]:>6}  |")
#         print("-"*45)

# # Función para que el usuario agregue producto y stock a la lista
# def agregar_producto_stock():
#     print("\nIngrese producto y/o stock.") 
#     articulo = input("\nIngrese el nombre del artículo: ")
#     if articulo in productos_stock:
#         respuesta = leer_si_no("El artículo que está ingresando ya existe. ¿Quiere modificar su stock?")
#         if not respuesta:
#             manipular_lista(productos_stock)
#     stock = leer_numero_validado("\nIngrese el stock del artículo",0)
#     productos_stock[articulo] = stock

# def manipular_lista(opcion):

#     match opcion: # Switch para que el usuario elija la opción:
#         case 1: # Imprime lista de precios
#             imprimir_lista(productos_stock)
#             manipular_lista(leer_opcion_menu())
#         case 2: # Consulta stock
#             consulta_stock()
#             manipular_lista(leer_opcion_menu())
#         case 3: # Agregar producto y/o stock
#             agregar_producto_stock()
#             manipular_lista(leer_opcion_menu())
#         case _:
#             print(f"\nSaliste de la aplicación.\n\n{"/"*30}\n")

# # ----------------------
# # Main
# # ----------------------

# productos_stock = {
#  'Aceite Natura': 5,
#  'Tomate Arcor': 2,
#  'Mayonesa Hellmans': 15,
#  'Aceite Patito': 7,
#  'Azúcar Chango': 8,
#  'Arroz Gallo': 1,
#  'Fideos Matarazzo': 15,
#  'Leche Sancor': 8,
#  'Yogur Ilolay': 15,
#  'Queso Casancrem': 14,
#  'Jabón Ala': 9,
#  'Papel Elite': 11,
#  'Café Ardu': 5,
#  'Galletas Oreo': 10,
#  'Chocolate Águila': 3
# }

# manipular_lista(leer_opcion_menu())


# # 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# # Permití consultar qué actividad hay en cierto día y hora. 

# # ----------------------
# # Funciones
# # ----------------------

# from datetime import datetime, time

# # Función para solicitar al usuario la opción Si o No
# def leer_si_no(mensaje):
#     while True:
#         opcion = input(f"\n{mensaje} (S/N): ").strip().upper()
#         if opcion == "S":
#             return True
#         elif opcion == "N":
#             return False
#         else:
#             print("ERROR: Por favor ingrese solo 'S' o 'N'")

# def consultar_agenda(agenda):
#     dd = 0
#     mm = 6
#     aaaa = 2025
#     hh = -1
#     while not (dd > 0 and dd < 31):
#         dd = int(input("Ingrese el día (dd): "))
#     while not (mm > 0 and mm < 13):
#         mm = int(input("Ingrese el mes (mm): "))
#     while not (aaaa > 1999 and aaaa < 2100):
#         aaaa = int(input("Ingrese el año (aaaa): "))
#     while not hh > 0 and hh < 24:
#         hh = int(input("Ingrese el mes (mm): "))
#     hh = int(input("Ingrese la hora (hh): "))
#     evento = agenda.get((datetime(2025, mm, dd), time(hh)), "No hay evento")
#     print(f"Evento: {evento}")

# # ----------------------
# # Main
# # ----------------------

# agenda_junio2025 = {
#     # Domingo 1/6
#     (datetime(2025, 6, 1), time(9, 0)): "Preparar comida para la reunión",
#     (datetime(2025, 6, 1), time(11, 0)): "Juntada familiar",
    
#     # Lunes 2/6
#     (datetime(2025, 6, 2), time(9, 0)): "Reunión equipo trabajo",
#     (datetime(2025, 6, 2), time(13, 0)): "Almuerzo con jefe",
#     (datetime(2025, 6, 2), time(16, 0)): "Natación",
    
#     # Martes 3/6
#     (datetime(2025, 6, 3), time(10, 0)): "Turno dentista",
#     (datetime(2025, 6, 3), time(13, 0)): "Clase Facultad: Programación",
#     (datetime(2025, 6, 3), time(18, 0)): "Estudio grupal",
    
#     # Miércoles 4/6
#     (datetime(2025, 6, 4), time(8, 0)): "Gimnasio",
#     (datetime(2025, 6, 4), time(13, 0)): "Almuerzo con clientes importantes",
#     (datetime(2025, 6, 4), time(17, 0)): "Entrega de informe",
    
#     # Jueves 5/6
#     (datetime(2025, 6, 5), time(12, 0)): "Entrega proyecto final (deadline)",
#     (datetime(2025, 6, 5), time(20, 0)): "Cine: estreno nueva película",
#     (datetime(2025, 6, 5), time(23, 0)): "Cena post-cine",
    
#     # Viernes 6/6
#     (datetime(2025, 6, 6), time(10, 0)): "Limpieza profunda casa",
    
#     # Sábado 7/6
#     (datetime(2025, 6, 7), time(9, 0)): "Mercado semanal",
#     (datetime(2025, 6, 7), time(21, 0)): "Cumpleaños de Juan",
    
#     # Domingo 8/6
#     (datetime(2025, 6, 8), time(10, 0)): "Desayuno familiar",
#     (datetime(2025, 6, 8), time(16, 0)): "Paseo por parque ecológico",
    
#     # Lunes 9/6
#     (datetime(2025, 6, 9), time(11, 0)): "Revisión médica anual",
#     (datetime(2025, 6, 9), time(19, 0)): "Taller de cocina italiana",
    
#     # Martes 10/6
#     (datetime(2025, 6, 10), time(14, 0)): "Presentación proyecto cliente",
#     (datetime(2025, 6, 10), time(20, 30)): "Partido de fútbol semanal",
    
#     # Miércoles 11/6
#     (datetime(2025, 6, 11), time(15, 0)): "Webinar: Nuevas tecnologías Python",
    
#     # Jueves 12/6
#     (datetime(2025, 6, 12), time(9, 30)): "Veterinario con Toby",
#     (datetime(2025, 6, 12), time(18, 0)): "Reunión amigos universidad",
    
#     # Viernes 13/6
#     (datetime(2025, 6, 13), time(15, 0)): "Viaje a Córdoba (salida)",
#     (datetime(2025, 6, 13), time(19, 0)): "Check-in hotel",
    
#     # Sábado 14/6
#     (datetime(2025, 6, 14), time(8, 0)): "Excursión a las sierras",
#     (datetime(2025, 6, 14), time(20, 0)): "Cena típica",
    
#     # Domingo 15/6
#     (datetime(2025, 6, 15), time(13, 0)): "Almuerzo familiar (Día del Padre)",
#     (datetime(2025, 6, 15), time(19, 0)): "Regreso a casa",

#     # Lunes 16/6
#     (datetime(2025, 6, 16), time(9, 0)): "Reunión planificación semanal",
#     (datetime(2025, 6, 16), time(18, 0)): "Clase de yoga",

#     # Martes 17/6
#     (datetime(2025, 6, 17), time(11, 0)): "Charla sobre sustentabilidad",
#     (datetime(2025, 6, 17), time(20, 0)): "Cena con amigas/os",

#     # Miércoles 18/6
#     (datetime(2025, 6, 18), time(8, 0)): "Gimnasio",
#     (datetime(2025, 6, 18), time(16, 0)): "Entrega de presupuesto",

#     # Jueves 19/6
#     (datetime(2025, 6, 19), time(10, 0)): "Reunión con asesor/a contable",
#     (datetime(2025, 6, 19), time(19, 0)): "Teatro independiente",

#     # Viernes 20/6 (Feriado: Paso a la Inmortalidad de Belgrano)
#     (datetime(2025, 6, 20), time(12, 0)): "Almuerzo criollo",
#     (datetime(2025, 6, 20), time(17, 0)): "Acto conmemorativo",

#     # Sábado 21/6
#     (datetime(2025, 6, 21), time(9, 30)): "Caminata en la reserva natural",
#     (datetime(2025, 6, 21), time(22, 0)): "Noche de juegos",

#     # Domingo 22/6
#     (datetime(2025, 6, 22), time(10, 0)): "Brunch en casa de Lucía",
#     (datetime(2025, 6, 22), time(18, 0)): "Domingo de películas",

#     # Lunes 23/6
#     (datetime(2025, 6, 23), time(9, 0)): "Inicio sprint laboral",
#     (datetime(2025, 6, 23), time(14, 0)): "Entrevista laboral (remota)",

#     # Martes 24/6
#     (datetime(2025, 6, 24), time(13, 0)): "Almuerzo en nuevo restaurante",
#     (datetime(2025, 6, 24), time(19, 0)): "Preparar clase del miércoles",

#     # Miércoles 25/6
#     (datetime(2025, 6, 25), time(9, 0)): "Revisión de tareas estudiantiles",
#     (datetime(2025, 6, 25), time(17, 0)): "Encuentro con colegas",

#     # Jueves 26/6
#     (datetime(2025, 6, 26), time(10, 0)): "Control técnico del auto",
#     (datetime(2025, 6, 26), time(20, 0)): "Noche de jazz en el centro",

#     # Viernes 27/6
#     (datetime(2025, 6, 27), time(9, 0)): "Coaching profesional",
#     (datetime(2025, 6, 27), time(21, 0)): "Cena de fin de curso",

#     # Sábado 28/6
#     (datetime(2025, 6, 28), time(8, 0)): "Viaje a las sierras con amigas/os",
#     (datetime(2025, 6, 28), time(19, 0)): "Fogón y guitarra",

#     # Domingo 29/6
#     (datetime(2025, 6, 29), time(11, 0)): "Desayuno de campo",
#     (datetime(2025, 6, 29), time(17, 0)): "Regreso a casa",

#     # Lunes 30/6
#     (datetime(2025, 6, 30), time(10, 0)): "Revisión mensual de objetivos",
#     (datetime(2025, 6, 30), time(18, 0)): "Preparar agenda de julio"
# }

# bandera = True
# while bandera:
#     if leer_si_no("¿Quiere consultar la agenda de junio?"):
#         consultar_agenda(agenda_junio2025)
#     else:
#         bandera = False
#         print("\nUsted salió de la agenda.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

# ----------------------
# Funciones
# ----------------------

# Función para solicitar al usuario la opción Si o No
def leer_si_no(mensaje):
    while True:
        opcion = input(f"\n{mensaje} (S/N): ").strip().upper()
        if opcion == "S":
            return True
        elif opcion == "N":
            return False
        else:
            print("ERROR: Por favor ingrese solo 'S' o 'N'")

# Función para solicitar al usuario la opción de menu entre 1 o 2
def leer_opcion():
    opcion = None
    valida = False
    print(f"\n{("-"*65)}\n Ingrese la opción de la acción que necesite realizar: \n\n 1: Consultar capital \n 2: Consultar país\n")
    while not valida:
        opcion = input("Seleccione opción (1/2): ")
        if opcion in {'1', '2'}:
            valida = True
        else:
            print("ERROR: Debe ser 1 o 2")
    return opcion

# Función para consultar value de diccionario a partir de su key
def consulta_diccionario(diccionario, consulta):
        if consulta in diccionario:
            print("-"*45)
            print(f"\n {consulta} pertenece a {diccionario[consulta]}")
            print("-"*45)
        else:
            print("\nNo encontramos su consulta.\nPor favor ingrese otra: ")
            consulta_diccionario(diccionario)

# ----------------------
# Main
# ----------------------

atlas_paises = {
    "Afganistán": "Kabul",
    "Alemania": "Berlín",
    "Arabia Saudita": "Riad",
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Bélgica": "Bruselas",
    "Bolivia": "Sucre",
    "Brasil": "Brasilia",
    "Canadá": "Ottawa",
    "Chile": "Santiago",
    "China": "Pekín",
    "Colombia": "Bogotá",
    "Corea del Sur": "Seúl",
    "Costa Rica": "San José",
    "Cuba": "La Habana",
    "Ecuador": "Quito",
    "Egipto": "El Cairo",
    "El Salvador": "San Salvador",
    "España": "Madrid",
    "Estados Unidos": "Washington D.C.",
    "Filipinas": "Manila",
    "Finlandia": "Helsinki",
    "Francia": "París",
    "Grecia": "Atenas",
    "Guatemala": "Ciudad de Guatemala",
    "Honduras": "Tegucigalpa",
    "India": "Nueva Delhi",
    "Indonesia": "Yakarta",
    "Irak": "Bagdad",
    "Irán": "Teherán",
    "Italia": "Roma",
    "Japón": "Tokio",
    "Marruecos": "Rabat",
    "México": "Ciudad de México",
    "Nicaragua": "Managua",
    "Noruega": "Oslo",
    "Países Bajos": "Ámsterdam",
    "Panamá": "Ciudad de Panamá",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Polonia": "Varsovia",
    "Portugal": "Lisboa",
    "Reino Unido": "Londres",
    "República Dominicana": "Santo Domingo",
    "Rusia": "Moscú",
    "Suecia": "Estocolmo",
    "Suiza": "Berna",
    "Turquía": "Ankara",
    "Ucrania": "Kiev",
    "Venezuela": "Caracas"
}

atlas_ciudades = {}

for pais, capital in atlas_paises.items():
    atlas_ciudades[capital] = pais

bandera = True
while bandera:
    if leer_si_no("¿Quiere consultar el atlas?"):
        opcion = leer_opcion()
        if opcion == "1":
            consulta = input("\nIngrese el país para mostrarle su capital: ")
            consulta_diccionario(atlas_paises, consulta)
        elif opcion == "2":
            consulta = input("\nIngrese la capital para mostrarle el país al que pertenece: ")
            consulta_diccionario(atlas_ciudades, consulta)
    else:
        bandera = False
        print("\nUsted salió del atlas.")

