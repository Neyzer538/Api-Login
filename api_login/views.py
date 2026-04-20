from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Usuario, Rol
from .serializer import UsuarioSerializer, RolSerializer

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        nombre = request.data.get("nombre")   # ahora es username
        contrasenia = request.data.get("contrasenia")

        try:
            usuario = Usuario.objects.get(nombre=nombre, contrasenia=contrasenia, estado=True)
            serializer = UsuarioSerializer(usuario)
            return Response({"message": "Login exitoso", "usuario": serializer.data}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

class ListaUsuarioView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class ListaRolView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer