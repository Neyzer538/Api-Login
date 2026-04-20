from django.urls import path
from .views import ListaUsuarioView, UsuarioDetalleView, ListaRolView, RolDetalleView, LoginView

urlpatterns = [
    path('usuarios/', ListaUsuarioView.as_view(), name='Lista-Usuarios'),
    path('usuarios/<int:pk>/', UsuarioDetalleView.as_view(), name='Detalle-Usuario'),
    path('roles/', ListaRolView.as_view(), name='Lista-Roles'),
    path('roles/<int:pk>/', RolDetalleView.as_view(), name='Detalle-Rol'),
    path("login/", LoginView.as_view(), name="login"),
]
