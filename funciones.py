from excepciones import PasswordValidationError
import re

def validar_password(password):
    try:
        not_correct = False
        message = []
        if not (8 <= len(password) <= 16):
            not_correct = True
            message.append("longitud entre 8 y 16 caracteres")
        if not re.search('[a-z]', password):
            not_correct = True
            message.append("contener al menos una letra minúscula")
        if not re.search('[A-Z]', password):
            not_correct = True
            message.append("contener al menos una letra mayúscula")
        if not re.search('[0-9]', password):
            not_correct = True
            message.append("contener al menos un dígito")
        if not re.search('[$@#]', password):
            not_correct = True
            message.append("debe contener al menos un caracter especial")
        if not_correct:
            mensaje_inicial = "La contraseña debe tener: "
            errores = ", ".join(message)
            raise PasswordValidationError(mensaje_inicial + errores)
        return True
    except Exception as e:
        print(f"Error - {e}")
        return False
