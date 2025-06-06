# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA

# Programación 1
# Profesor: Prof. Cinthia Rigoni
# Tutor: Prof. Martín A. García

# Trabajo Práctico Integrador: Búsqueda y Ordenamiento

# Estudiantes: 
# Hernán E. Bula
# Rodrigo Arias


# Actividades

'''
Objetivo: Aplicar y analizar los algoritmos fundamentales de búsqueda y ordenamiento utilizando Python, 
en el contexto de la gestión de datos de una lista de precios de artículos de supermercado.

Problema: Se dispone de una lista de artículos de supermercado. Cada artículo está representado por una 
estructura de datos de lista que contiene [ID de artículo, nombre de producto, precio]. 
La información inicial se presenta como una lista de listas en Python (lista anidada), 
donde cada sub-lista representa un artículo.

Se propuso realizar un programa que permita al usuario incorporar nuevos artículos a la lista o borrar los existentes. 
Asimismo, mediante un algoritmo de búsqueda, el usuario puede buscar un artículo y mediante un algoritmo de ordenamiento,
puede solicitar ordenarlos por alguno de sus elementos: número de artículo, nombre del artículo o precio.

Partes del algoritmo a desarrollar
    -Un switch que el usuario elija una función:
        1: imprimir lista de precios
        2: agregar artículo
        3: eliminar artículo
        4: buscar un artículo
        5: ordenar lista por elemento
    -Definir las funciones de cada caso
    -Elegir el mejor método de búsqueda
    -Elegir el mejor método de ordenamiento
    -Comprobar la eficiencia de los algoritmos para ver cual es más eficiente a partir de las conclusiones.


'''

# ------------------------
#  Definición de funciones


# Función para solicitar al usuario un dato, indicando el mensaje
def solicitar_dato(variable): 
    variable = input(f"\nIngrese {variable}: ")
    return variable


# Función para solicitar al usuario número float validado y configurar el mensaje, minimo y máximo
def leer_float_validado(mensaje, min = float("-Inf"), max = float("Inf")): 
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n


# Función para solicitar al usuario número entero validado y configurar el mensaje, minimo y máximo
def leer_numero_validado(mensaje, min = float("-Inf"), max = float("Inf")): 
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n


# Función para imprimir la lista anidada en formato tabla. Para armar el formato tabla se solicitó asesoramiento de IA Deepseek
def imprimir_lista(lista): 
        print("\n\n")
        print("-"*65)
        print(f"{'ID':<5} | {'PRODUCTO':<40} | {'PRECIO':>12}")
        print("-"*65)
        for id_prod, articulo, precio in lista:
            print(f"{id_prod:<5} | {articulo:<40} | ${precio:>12.2f}")


# Función de imprimir un artículo de una lista en formato tabla. Se adaptó la función imprimir_lista(lista)
def imprimir_producto(producto):
    print("-"*65)
    print(f"{'ID':<5} | {'PRODUCTO':<40} | {'PRECIO':>12}")
    print("-"*65)
    id_prod, articulo, precio = producto
    print(f"{id_prod:<5} | {articulo:<40} | ${precio:>12.2f}")


# Función para agregar artículo a la lista, asignando un ID correlativo y solicitando datos al usuario (nombre + precio)
def agregar_articulo(): 
    id_prod = len(lista_precios)+1
    articulo = input("\nIngrese el nombre del artículo: ")
    precio = leer_float_validado("\nIngrese el precio del artículo", min = 0, max = float("Inf"))
    lista_precios.append([id_prod, articulo, precio])


# Función para eliminar un artículo de la lista, solicitando el número de ID al usuario
def eliminar_articulo(): 
    id_prod = leer_numero_validado("\nIngrese el ID del artículo para eliminarlo", 1, (len(lista_precios)))
    del lista_precios[id_prod-1]
    imprimir_lista(lista_precios)


# Función para modificar los datos de un artículo de la lista, solicitando los datos el ID al usuario y los datos a modificar nombre y precio.
def modificar_articulo(): 
    id_prod = leer_numero_validado("\nIngrese el ID del artículo a modificar", 1, (len(lista_precios)))
    articulo = input("\nIngrese el nombre nuevo del producto: ")
    precio = leer_float_validado("\nIngrese el precio nuevo del producto", min = 0, max = float("Inf"))
    lista_precios[id_prod-1][1] = articulo
    lista_precios[id_prod-1][2] = precio
    imprimir_producto(lista_precios[id_prod-1])


# Función para buscar un artículo de la lista, solicitando el dato al usuario para la búsqueda (id, nombre o precio)
def buscar_articulo(): 
    print("\nIngrese la opción que necesite \n 1: para buscar por ID del producto \n 2: para buscar por nombre del producto \n 3: para buscar por precio.\n")
    opcion = leer_numero_validado("Ingrese el número elegido",1,3) # falta mejorar la funcion para validar dato (upper, solo letra, etc.)

    match opcion:
        case 1:
            id_prod = leer_numero_validado("\nIngrese ID del producto", 1, (len(lista_precios)))
            imprimir_producto(lista_precios[id_prod-1])
        case 2:
            prod = solicitar_dato("\nIngrese nombre del producto") # falta mejorar la funcion para validar dato (upper, solo letra, etc.)
            encontrado = False # Bandera para saber si encontra el producto o no
            for i in range(0, len(lista_precios)):
                if prod == lista_precios[i][1]:
                    imprimir_producto(lista_precios[i])
                    encontrado = True
            if not encontrado:            
                print(f"No exite un producto con ese nombre {prod}")
        case 3:
            precio = leer_float_validado("\nIngrese precio del producto", 0)
            encontrado = False # Bandera para saber si encontra el producto o no
            for i in range(0, len(lista_precios)):
                if precio == lista_precios[i][2]:
                    imprimir_producto(lista_precios[i])
                    encontrado = True
            if not encontrado:
                print(f"No exite un producto con ese precio {precio}")

        case _:
            pass
    

# Función para ordenar los artículos de la lista, solicitando al usuario por cual criterio: id, nombre o precio
def ordenar_lista():
    print("\nIngrese la opción que necesite \n 1: para ordenar por el ID del producto \n 2: para ordenar alfabéticamente por nombre del producto \n 3: para ordenar por precio.\n")
    opcion = leer_numero_validado("Ingrese el número elegido",1,3) # falta mejorar la funcion para validar dato (upper, solo letra, etc.)

    match opcion:
        case 1:
            id_prod = leer_numero_validado("\nIngrese ID del producto", 1, (len(lista_precios)))
            print(f"Falta establecer el metodo de ordenamiento por {id_prod}")
        case 2:
            prod = solicitar_dato("\nIngrese nombre del producto") # falta mejorar la funcion para validar dato (upper, solo letra, etc.)
            print(f"Falta establecer el metodo de ordenamiento por {prod}")
            pass
        case 3:
            precio = leer_float_validado("\nIngrese precio del producto", 0)
            print(f"Falta establecer el metodo de ordenamiento por {precio}")
            pass
        case _:
            pass


# Función para ver el menu
def eleccion_opcion():  
    menu = input("\n¿Quiere ingresar al menu de opciones? (S/N): ")
    if menu.upper() == "S":
        print(f"\n{("-"*65)} \n{("-"*65)} \n\n Ingrese la opción de la acción que necesite realizar: \n\n A: imprimir lista de precios \n B: agregar artículo \n C: eliminar artículo \n D: modificar artículo \n E: buscar un artículo \n F: ordenar lista por elemento \n\n IMPORTANTE: Si ingresa cualquier otra tecla y enter, sale de la aplicación.\n")
        opcion = solicitar_dato("opcion") # falta mejorar la funcion para validar dato (upper, solo letra, etc.)
        return opcion.upper()


# Función para manipular el menu de la aplicación y realizar acciones sobre la lista
def manipular_lista(opcion):

    match opcion: # Switch para que el usuario elija la opción:
        case "A": # Imprime lista de precios
            imprimir_lista(lista_precios)
            manipular_lista(eleccion_opcion())
        case "B": # Agrega artículo
            agregar_articulo()
            imprimir_lista(lista_precios)
            manipular_lista(eleccion_opcion())
        case "C": # Elimina artículo
            imprimir_lista(lista_precios)
            eliminar_articulo()
            manipular_lista(eleccion_opcion())
        case "D": # Modifica artículo existente
            imprimir_lista(lista_precios)
            modificar_articulo()
            manipular_lista(eleccion_opcion())
        case "E": # Busca un artículo
            # Buscar y elegir el mejor método de búsqueda para lista de listas
            buscar_articulo()
            manipular_lista(eleccion_opcion())
        case "F": # Ordena lista por elemento: id_prod, articulo, precio
            # Buscar y elegir el mejor método de ordenamiento para lista de listas
            ordenar_lista()
            manipular_lista(eleccion_opcion())
        case _:
            print("Saliste de la aplicación.")

    
# ------------------------
# Main

lista_precios = [
    [1, "Aceite Natura - 900 cc", 2090.50],
    [2, "Tomate Arco en lata - 400 grs", 1190.00],
    [3, "Mayonesa RI-K - 250 grs", 1090.50],
    [4, "Aceite Patito - 1500 cc", 3590.50],
    [5, "Azúcar Chango - 1 kg", 990.90],
    [6, "Ensalada frutas lata - 850 grs", 1930.00],
    [7, "Arroz Gallo Oro - 1 kg", 1850.00],
    [8, "Fideos Matarazzo - 500 grs", 1680.50],
    [9, "Leche entera La Serenísima - 1 lt", 2320.00],
    [10, "Yogur bebible Ilolay - 1 lt", 2850.75],
    [11, "Queso crema Casancrem - 290 grs", 3890.00],
    [12, "Jabón líquido Ala - 750 ml", 6920.30],
    [13, "Papel higiénico Elite - 4 rollos", 4120.00],
    [14, "Café La Morenita - 500 grs", 9150.00],
    [15, "Galletas Oreo - 117 grs", 1500.00],
    [16, "Chocolate Águila - 100 grs", 5010.00]
]

manipular_lista(eleccion_opcion())



