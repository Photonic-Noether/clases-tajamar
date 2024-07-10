""" 
Un closure es una función anidada que recuerda los valores de las variables del
entorno en el que fue creada, incluso después de que ese entorno haya terminado
su ejecución. Es una característica de los lenguajes de programación que soportan
funciones de primera clase, como Python o Javascript.
"""

def exterior(mensaje):
    # Una forma
    def interior():
        print(mensaje)
        
    # Otra forma
    interior = lambda: print(mensaje)
    return interior

mi_closure = exterior("¡Hola, mundo!")
mi_closure()

def calculadora(valor1: int, operacion: str, valor2: int):
    if operacion == "+":
        calculo = lambda: valor1 + valor2
    elif operacion == "-":
        calculo = lambda: valor1 - valor2
    elif operacion == "*":
        calculo = lambda: valor1 * valor2
    elif operacion == "/":
        try:
            calculo = lambda: valor1 / valor2
        except ZeroDivisionError:
            print("No puedes dividir por 0")
            calculo = None
    else:
        raise ValueError()
    try:
        print(f"{calculo() if calculo else "No hay resultado"}")
    except Exception as e:
        print(str(e))  # Solo por si hay otros errores raros
    return calculo
 
calc = calculadora(10, "/", 2)
calc()

""" 
Un decorador es un closure que devuelve como return una funcion arbitraria, de
forma que complementa (o decora) otra funcion
"""

import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {round(fin - inicio, 3)} segundos")
        return resultado
    return wrapper

@medir_tiempo
def suma(a, b):
    time.sleep(2)
    return a + b

resultado = suma(3, 4)
print(f"Resultado: {resultado}")

# Decorador de En proceso
def process_decorator(func):
    def wrapper(*args, **kwargs):
        print("En proceso ...")
        return func(*args, **kwargs)
    return wrapper

@process_decorator
def suma(a, b):
    time.sleep(2)
    return a + b

resultado = suma(3, 4)

def decorador_con_args(arg1, arg2):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"Argumentos del decorador: {arg1}, {arg2}")
            resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@decorador_con_args("Hola", "Mundo")
def funcion_ejemplo():
    print("Función ejecutada")

funcion_ejemplo()
