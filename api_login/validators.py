import re
from django.core.exceptions import ValidationError

def evaluar_contrasenia(value):
    if not value or value.strip() == "":
       raise ValidationError("La contraseña no puede estar vacía")

    longitud = len(value) >= 12
    mayuscula = any(c.isupper() for c in value)
    numero = any(c.isdigit() for c in value)
    simbolo = any(c in "!@#$%^&*(),.?\":{}|<>" for c in value)

    puntos = sum([longitud, mayuscula, numero, simbolo])

    if puntos < 4:
        raise ValidationError("La contraseña no es segura")