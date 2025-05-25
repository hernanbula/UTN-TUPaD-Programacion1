# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# ------------------------
#  Definición de funciones

def calculo_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculo_factorial(n-1)

# ------------------------
# Main

numero = int(input("Ingrese un número para calcular su factorial: "))
for i in range(1, numero+1):
    print(calculo_factorial(i))

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# ------------------------
#  Definición de funciones

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1)+fibonacci(posicion-2)

# ------------------------
# Main

numero = int(input("Ingrese un número para calcular su posición en fibonacci y mostrar la serie correspondiente: "))
for i in range(numero):
    print(fibonacci(i))


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula:
# 𝑛**𝑚 = 𝑛 ∗ 𝑛 **(𝑚−1)
# Prueba esta función en un algoritmo general.

# ------------------------
#  Definición de funciones

def potencia_recursiva(base,exp):
    if exp == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exp-1)

# ------------------------
# Main

base = int(input("Ingrese un número base para calcular una potencia: "))
exp = int(input("Ingrese un número de exponente para calcular la potencia: "))

for i in range(base):
    print(f"{i} ** {exp} = {potencia_recursiva(i,exp)}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

# ------------------------
#  Definición de funciones
  
def binario_recursivo(n):
    if n == 0:
        return ""
    else:     
       return binario_recursivo(n // 2) + str(n % 2)
    
# ------------------------
# Main

numero = int(input("Ingrese un número para calcular su binario: "))
print(binario_recursivo(numero))


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#  Requisitos:
    # La solución debe ser recursiva.
    # No se debe usar [::-1] ni la función reversed().

# ------------------------
#  Definición de funciones

def es_palindromo(palabra):
    if len(palabra) == 0:
        return False
    elif len(palabra) == 1:
       return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else: 
            return False      
    
# ------------------------
# Main

palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
print(es_palindromo(palabra))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
    # No se puede convertir el número a string.
    # Usá operaciones matemáticas (%, //) y recursión.
    # Ejemplos:
    # suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
    # suma_digitos(9) → 9
    # suma_digitos(305) → 8 (3 + 0 + 5)

# ------------------------
#  Definición de funciones

def suma_digitos(n):

    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
# ------------------------
# Main

numero = int(input("Ingrese un número para calcular la suma de sus digitos: "))
print(suma_digitos(numero))


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.
#  Ejemplos:
    # contar_bloques(1) → 1 (1)
    # contar_bloques(2) → 3 (2 + 1)
    # contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# ------------------------
#  Definición de funciones

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)

# ------------------------
# Main

numero = int(input("Ingrese uel numero de bloques de base para calcular \nel total de bloques que necesita para construir toda la pirámide: "))
print(contar_bloques(numero))


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 

# ------------------------
#  Definición de funciones

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def contar_digito(numero, digito):
    contador = 0
    if numero < 10:
        return 1 if numero == digito else 0
    else: 
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
# ------------------------
# Main

numero = leer_entero_validado("Ingrese número entero positivo", 0)
digito = leer_entero_validado("Ingrese un dígito (entre 0 y 9)", 0, 10)
print(contar_digito(numero, digito))