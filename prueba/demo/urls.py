from django.urls import path
from demo import views
from django.contrib import admin



urlpatterns = [
    path('', views.ver_coleccion, name='ver_coleccion'),
    path('mostrar/', views.mostrar_coleccion, name='mostrar_coleccion'),

    path('admin/', admin.site.urls),
    
]