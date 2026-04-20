from rest_framework import serializers
from .models import Usuario, Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        
    def validate_contrasenia(self, value):
        if not value or value.strip() == "":
            raise serializers.ValidationError("La contraseña no puede estar vacía")

        longitud = len(value) >= 12
        mayuscula = any(c.isupper() for c in value)
        numero = any(c.isdigit() for c in value)
        simbolo = any(c in "!@#$%^&*(),.?\":{}|<>" for c in value)

        puntos = sum([longitud, mayuscula, numero, simbolo])

        if puntos < 4:
            raise serializers.ValidationError("La contraseña no es segura")
        return value    