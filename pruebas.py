from funciones import validar_password
 
try:
    # Solicitamos al usuario que ingrese la contraseña
    clave = input('Escriba la contraseña: ')
    if not clave:
        # Si la entrada está vacía, lanzamos una excepción ValueError
        raise ValueError("La contraseña no puede estar vacía")
    # Intentamos validar la contraseña ingresada
    print(validar_password(clave))
except ValueError as e:
    # Capturamos específicamente excepciones de tipo ValueError y mostramos un mensaje de error.
    print(f"Entrada inválida: {e}")
except Exception as e:
    # Capturamos cualquier otra excepción y mostramos un mensaje de error.
    print(f"Error inesperado: {e}")