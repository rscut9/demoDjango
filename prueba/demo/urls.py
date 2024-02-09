from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout/', exit, name='exit'),
    path('ver/', ver_coleccion, name='ver_coleccion'),
    path('mostrar/', mostrar_coleccion, name='mostrar_coleccion'),
    path('crear_usuario/', create_user, name='crear_usuario'),
]