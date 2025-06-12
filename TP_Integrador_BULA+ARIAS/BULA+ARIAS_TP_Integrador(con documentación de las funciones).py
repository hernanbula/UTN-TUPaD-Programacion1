# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA

# Programación 1

# Profesor Coordinador: Alberto Cortez
# Profesora comisión 1: Prof. Cinthia Rigoni
# Tutor: Prof. Martín A. García

# Trabajo Práctico Integrador: Búsqueda y Ordenamiento

# Estudiantes: 
# Hernán E. Bula - hernanbula@gmail.com 
# Rodrigo Arias - roarias299@gmail.com 


# Actividades

'''
Objetivo: Aplicar y analizar los algoritmos fundamentales de búsqueda y ordenamiento utilizando Python, 
en el contexto de la gestión de datos de una lista de precios de artículos de supermercado.

Problema: Se dispone de una lista de artículos de supermercado. Cada artículo está representado por una 
estructura de datos de lista que contiene ID de artículo, nombre de producto y precio. 
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
        4: buscar un artículo (por ID, nombre o precio)
        5: ordenar lista por elemento (por ID, nombre o precio) y de manera ascendente o descendente
    -Definir las funciones de cada caso
    -Elegir un método de búsqueda
    -Elegir un método de ordenamiento
'''

# -------------------------
#  DEFINICIÓN DE FUNCIONES
# -------------------------


# Función para solicitar al usuario un dato, indicando el mensaje
def solicitar_dato(variable): 
    '''  
    Solicita al usuario un valor para la variable dada y lo retorna como string.  
    
    Parámetros:  
        variable (str): Texto descriptivo del dato a ingresar (ej: "edad").  
    
    Retorno:  
        str: Valor ingresado por el usuario.  
    '''  
    variable = input(f"\nIngrese {variable}: ")
    return variable


# Función para solicitar al usuario número float validado y configurar el mensaje, minimo y máximo
def leer_float_validado(mensaje, min = float("-Inf"), max = float("Inf")): 
    '''
    La función solicita al usuario un número de tipo float y valida que esté dentro de un rango específico (si se proporciona). 
    Si el número ingresado no está dentro del rango válido, la función continuará solicitando el número hasta que se ingrese un valor válido.
    
    Parámetros:
        mensaje (str): Mensaje que se muestra al usuario para solicitar el número.
        min (float, opcional): Valor mínimo permitido (inclusive). Por defecto es -Inf (sin límite inferior).
        max (float, opcional): Valor máximo permitido (inclusive). Por defecto es Inf (sin límite superior).
    
    Retorno:
        float: Número válido ingresado por el usuario que cumple con los límites especificados.
    
    Notas:
        La función convierte directamente la entrada del usuario a float, lo que puede generar un ValueError si se ingresa un valor no numérico. 
        Se recomienda manejar esta excepción externamente si es necesario.
    '''
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n


# Función para solicitar al usuario número entero validado y configurar el mensaje, minimo y máximo
def leer_numero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    '''
    Solicita un número entero validando que esté dentro del rango [min, max].
    
    Parámetros:
        mensaje (str): Texto mostrado al solicitar el número.
        min (int, opcional): Límite inferior (inclusive). Default: -infinito.
        max (int, opcional): Límite superior (inclusive). Default: +infinito.
    
    Retorno:
        int: Número válido ingresado por el usuario.
    
    Excepciones:
        ValueError: Si la entrada no es un número entero.
    '''
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n


# Función para solicitar al usuario la opción de menu entre 1, 2 o 3
def leer_opcion_menu():
    '''
    Solicita y valida una opción de menú numérica (1, 2 o 3).
    Si la opción ingresada no es válida, continúa solicitando hasta recibir una opción correcta.
    
    Retorno:
        int: Opción válida convertida a entero.
    '''
    opcion = None
    valida = False
    while not valida:
        opcion = input("Seleccione opción (1/2/3): ")
        if opcion in {'1', '2', '3'}:
            valida = True
        else:
            print("ERROR: Debe ser 1, 2 o 3")
    return int(opcion)


# Función para solicitar al usuario la opción Si o No
def leer_si_no(mensaje):
    """
    Solicita al usuario una confirmación S/N y devuelve un booleano.
    
    Argumentos:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        bool: True si el usuario ingresa 'S', False si ingresa 'N'
    """
    while True:
        opcion = input(f"\n{mensaje} (S/N): ").strip().upper()
        if opcion == "S":
            return True
        elif opcion == "N":
            return False
        else:
            print("ERROR: Por favor ingrese solo 'S' o 'N'")


# Función para imprimir la lista anidada en formato tabla. Para armar el formato tabla se solicitó asesoramiento de IA Deepseek
def imprimir_lista(lista):
    '''
    Imprime una lista de productos formateada como tabla.
    
    Parámetros:
    lista (list): Lista de tuplas con formato (id, producto, precio)
    
    Formato de salida:
    - Encabezado con ID, PRODUCTO y PRECIO
    - Filas alineadas con bordes
    - Precios formateados con 2 decimales y signo $
    '''
    print("\n\n")
    print("-"*65)
    print(f"{'ID':<5} | {'PRODUCTO':<40} | {'PRECIO':>12}")
    print("-"*65)
    for id_prod, articulo, precio in lista:
        print(f"{id_prod:<5} | {articulo:<40} | ${precio:>12.2f}")


# Función de imprimir un artículo de una lista en formato tabla. Se adaptó la función imprimir_lista(lista)
def imprimir_producto(producto):
    '''
    Imprime un único producto con formato de tabla alineada.

    Parámetros:
        producto (tuple): Tupla con formato (id: int, nombre: str, precio: float)
    
    Formato:
        - Mismo diseño que imprimir_lista() (encabezados y bordes)
        - Precio formateado con 2 decimales y símbolo $
    '''
    print("-"*65)
    print(f"{'ID':<5} | {'PRODUCTO':<40} | {'PRECIO':>12}")
    print("-"*65)
    id_prod, articulo, precio = producto
    print(f"{id_prod:<5} | {articulo:<40} | ${precio:>12.2f}")


# Función para agregar artículo a la lista, asignando un ID correlativo y solicitando datos al usuario (nombre + precio)
def agregar_articulo():
    '''
    Agrega un nuevo artículo a la lista de precios.
    
    Acciones:
        1. Genera automáticamente un ID (secuencial)
        2. Solicita nombre del artículo
        3. Valida el precio (mayor que 0)
        4. Agrega el artículo a lista_precios
    
    Estructura del artículo:
        [id: int, nombre: str, precio: float]
    
    Nota:
        Modifica la variable global lista_precios
    '''
    id_prod = lista_precios[len(lista_precios)-1][0]+1
    articulo = input("\nIngrese el nombre del artículo: ")
    precio = leer_float_validado("\nIngrese el precio del artículo", min = 0, max = float("Inf"))
    lista_precios.append([id_prod, articulo, precio])


# Función para eliminar un artículo de la lista, solicitando el número de ID al usuario
def eliminar_articulo():
    '''
    Elimina un artículo de la lista de precios por ID y muestra la lista actualizada.
    
    Flujo:
        1. Solicita y valida un ID existente
        2. Elimina el artículo correspondiente
        3. Muestra la lista actualizada
    
    Validación:
        - ID debe estar entre 1 y el máximo existente (usando leer_numero_validado)
    
    Efectos:
        - Modifica la variable global lista_precios
        - Reindexa los artículos restantes
    '''
    id_prod = leer_numero_validado("\nIngrese el ID del artículo para eliminarlo", 1, (len(lista_precios)))
    del lista_precios[id_prod-1]
    imprimir_lista(lista_precios)


# Función para modificar los datos de un artículo de la lista, solicitando los datos el ID al usuario y los datos a modificar nombre y precio.
def modificar_articulo():
    '''
    Modifica un artículo existente en la lista de precios.
    
    Flujo:
        1. Solicita y valida el ID del artículo a modificar
        2. Pide nuevo nombre y precio (validado > 0)
        3. Actualiza los datos del artículo
        4. Muestra el artículo modificado
    
    Validaciones:
        - ID debe ser válido (1 a cantidad de artículos)
        - Precio debe ser mayor que 0
    
    Efectos:
        - Modifica la variable global lista_precios
        - Conserva el ID original del artículo
    '''
    id_prod = leer_numero_validado("\nIngrese el ID del artículo a modificar", 1, (len(lista_precios)))
    articulo = input("\nIngrese el nombre nuevo del producto: ")
    precio = leer_float_validado("\nIngrese el precio nuevo del producto",0)
    lista_precios[id_prod-1][1] = articulo
    lista_precios[id_prod-1][2] = precio
    imprimir_producto(lista_precios[id_prod-1])


# Función para buscar un artículo de la lista, solicitando el dato al usuario para la búsqueda (id, nombre o precio)
def buscar_articulo():
    '''
    Busca artículos por diferentes criterios (ID, nombre o precio) y muestra los resultados.
    
    Flujo:
        1. Muestra menú de opciones de búsqueda
        2. Solicita criterio mediante leer_opcion_menu()
        3. Ejecuta búsqueda según opción seleccionada:
           - Case 1: Búsqueda por ID exacto
           - Case 2: Búsqueda por nombre exacto (case-sensitive)
           - Case 3: Búsqueda por precio exacto
        4. Muestra resultados con formato o mensaje de no encontrado
    
    Limitaciones actuales:
        - Búsqueda por nombre es case-sensitive
        - Búsqueda por precio no soporta rangos
        - No maneja múltiples coincidencias óptimamente
    
    Mejoras pendientes:
        - Normalización de texto (upper/lower)
        - Búsqueda por rangos de precio
        - Optimización de múltiples resultados
    '''
    print("\nIngrese la opción que necesite \n 1: para buscar por ID del producto \n 2: para buscar por nombre del producto \n 3: para buscar por precio.\n")
    opcion = leer_opcion_menu()

    match opcion:
        case 1:
            id_prod = leer_numero_validado("\nIngrese ID del producto", 1, (len(lista_precios)))
            imprimir_producto(lista_precios[id_prod-1])
        case 2:
            prod = solicitar_dato("nombre del producto") # falta mejorar la funcion para validar dato (upper, solo letra, etc.)
            encontrado = False # Bandera para saber si encuentra el producto o no
            for i in range(len(lista_precios)):
                if prod == lista_precios[i][1]:
                    imprimir_producto(lista_precios[i])
                    encontrado = True
            if not encontrado:            
                print(f"\n{"-"*65}\nNO existe un producto con el nombre: {prod}\n{"-"*65}")
                buscar_articulo()
        case 3:
            precio = leer_float_validado("\nIngrese precio del producto", 0)
            encontrado = False # Bandera para saber si encuentra el producto o no
            for i in range(len(lista_precios)):
                if precio == lista_precios[i][2]: # Falta mejorar para que pueda encontrar coincidencias entre un rango de precios
                    imprimir_producto(lista_precios[i])
                    encontrado = True
            if not encontrado:
                print(f"No exite un producto con el precio: {precio}")

        case _:
            pass


# Función para ordenar los artículos de la lista, solicitando al usuario por cual criterio: id, nombre o precio
def ordenar_lista():
    '''
    Ordena la lista de productos según criterio seleccionado (ID, nombre o precio) y orden (ascendente/descendente).
    
    Flujo:
        1. Muestra menú de opciones de ordenamiento
        2. Solicita criterio mediante leer_opcion_menu()
        3. Pide dirección de ordenamiento (Enter=ascendente, otra tecla=descendente)
        4. Ejecuta ordenar_selection_sort() con los parámetros correspondientes
    
    Parámetros de ordenamiento:
        - Case 1: Ordena por ID (índice 0)
        - Case 2: Ordena por nombre (índice 1)
        - Case 3: Ordena por precio (índice 2)
    
    Comportamiento:
        - Usa selection sort modificado (ordenar_selection_sort)
        - Orden ascendente por defecto
        - Modifica directamente lista_precios
    '''
    print("\nIngrese la opción que necesite \n 1: para ordenar por el ID del producto \n 2: para ordenar alfabéticamente por nombre del producto \n 3: para ordenar por precio.\n")
    indice = leer_opcion_menu() # Lee la opción validada entre 1,2 o 3
    orden = bool(input(f"\n{"-"*65}\nSi presiona enter, la lista se ordena de menor a Mayor por defecto. \nSi quiere ordenarla de manera descendente, ingrese cualquier tecla: "))
    match indice:
        case 1:
            ordenar_selection_sort(lista_precios,indice-1,orden)
        case 2:
            ordenar_selection_sort(lista_precios,indice-1,orden)
        case 3:
            ordenar_selection_sort(lista_precios,indice-1,orden)
        case _:
            pass


# Función con algoritmo de ordenamiento usando el método Selection Sort adaptado a una lista (de productos) de listas. 
# Para mejorarlo trabajamos con ayuda de IA Deepseek.
def ordenar_selection_sort(lista, indice_elemento, orden=False): # orden: Si True (mayor a menor), si False (menor a mayor). Default: False
    '''
    Ordena una lista de productos usando el algoritmo Selection Sort.
    
    Parámetros:
        lista (list): Lista de productos a ordenar
        indice_elemento (int): Índice de la columna para ordenar (0=ID, 1=nombre, 2=precio)
        orden (bool, opcional): False=ascendente (default), True=descendente
    
    Proceso:
        1. Recorre la lista buscando el elemento extremo (min/max según orden)
        2. Intercambia posiciones hasta ordenar completamente
        3. Muestra el resultado con imprimir_lista()
    
    Características:
        - El ordenamiento modifica la lista original
        - Evalúa según el tipo de dato en indice_elemento
        - No retorna valor (el resultado está en la lista modificada)
    '''
    n = len(lista)
    for i in range(n):
        # Inicializamos la posición del elemento extremo (mínimo o máximo)
        extremo = i
        for j in range(i+1, n):
            # Comparamos según el orden deseado
            if orden:  # Orden descendente (mayor a menor)
                if lista[j][indice_elemento] > lista[extremo][indice_elemento]:
                    extremo = j
            else:  # Orden ascendente (menor a mayor)
                if lista[j][indice_elemento] < lista[extremo][indice_elemento]:
                    extremo = j
        # Intercambiamos los elementos
        lista[i], lista[extremo] = lista[extremo], lista[i]
    
    imprimir_lista(lista)


# Función para ver opciones del menú principal:
def menu():
    '''
    Muestra el menú principal y solicita una opción al usuario.
    
    Flujo:
        1. Pide confirmación para ingresar al menú (S/N)
        2. Si es afirmativo (S):
           - Muestra todas las opciones disponibles
           - Solicita una opción mediante solicitar_dato()
        3. Retorna la opción en mayúsculas
    
    Opciones válidas:
        A: Imprimir lista
        B: Agregar artículo
        C: Eliminar artículo
        D: Modificar artículo
        E: Buscar artículo
        F: Ordenar lista
    
    Retorno:
        str: Opción seleccionada en mayúscula o None si no ingresa al menú
    '''
    ingreso = leer_si_no("¿Quiere ingresar al menu de opciones? ")
    if ingreso:
        print(f"\n{("-"*65)} \n{("-"*65)} \n\n Ingrese la opción de la acción que necesite realizar: \n\n A: imprimir lista de precios \n B: agregar artículo \n C: eliminar artículo \n D: modificar artículo \n E: buscar un artículo \n F: ordenar lista por elemento \n\n IMPORTANTE: Si ingresa cualquier otra tecla y enter, sale de la aplicación.")
        opcion = solicitar_dato("opcion")
        return opcion.upper()
    else:
        return None


# Función principal para ejecutar funciones del menu de la aplicación y realizar acciones sobre la lista según la opción seleccionada
# Controla el flujo principal de la aplicación.

def manipular_lista(opcion):
    '''
    Ejecuta operaciones sobre la lista de precios según la opción seleccionada.
    
    Parámetros:
        opcion (str): Letra mayúscula (A-F) que representa la acción a realizar
    
    Operaciones disponibles:
        A: Muestra toda la lista de precios
        B: Agrega nuevo artículo y muestra lista actualizada
        C: Muestra lista, elimina artículo y muestra lista actualizada
        D: Muestra lista, modifica artículo y muestra cambios
        E: Busca artículos por diferentes criterios
        F: Ordena la lista por diferentes atributos
    
    Flujo:
        - Cada operación muestra sus resultados
        - Vuelve a mostrar el menú después de completarse
        - Sale con cualquier otra tecla
    
    Notas:
        - Usa recursión para mantener el flujo (pero esto puede causar stack overflow en listas grandes)
        - Modifica la variable global lista_precios directamente
    '''
    match opcion: # Switch para que el usuario elija la opción:
        case "A": # Imprime lista de precios
            imprimir_lista(lista_precios)
        case "B": # Agrega artículo
            agregar_articulo()
            imprimir_lista(lista_precios)
        case "C": # Elimina artículo
            imprimir_lista(lista_precios)
            eliminar_articulo()
        case "D": # Modifica artículo existente
            imprimir_lista(lista_precios)
            modificar_articulo()
        case "E": # Busca un artículo
            buscar_articulo()
        case "F": # Ordena lista por elemento: id_prod, articulo, precio
            # Buscar y elegir el mejor método de ordenamiento para lista de listas
            ordenar_lista()
        case _:
            print(f"\nSaliste de la aplicación.\n\n{"/"*30}\n")
    if opcion != None:
        manipular_lista(menu())

    
# -------------------------
#  MAIN
# -------------------------

#  Lista inicial y ejecución

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

manipular_lista(menu())