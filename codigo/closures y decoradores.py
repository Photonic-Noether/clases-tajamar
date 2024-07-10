""" 
Un closure es una función anidada que recuerda los valores de las variables del
entorno en el que fue creada, incluso después de que ese entorno haya terminado
su ejecución. Es una característica de los lenguajes de programación que soportan
funciones de primera clase, como Python.
"""

def exterior(mensaje):
    def interior():
        print(mensaje)
    return interior

mi_closure = exterior("¡Hola, mundo!")
mi_closure()

# Hacer un closure calculadora con lambdas

""" 
Un decorador es un closure que devuelve
como return una funcion arbitraria, de
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

""" @medir_tiempo
def factorial(n):
    if n < 0:
        raise ValueError()
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial(1000) """

# Hacer un decorador de "Work in progress..."

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

#funcion_ejemplo()
