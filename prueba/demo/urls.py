from django.urls import path
from demo import views

#def trigger_error(request):
#    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.exit, name='exit'),
    path('ver/', views.ver_coleccion, name='ver_coleccion'),
    path('mostrar/', views.mostrar_coleccion, name='mostrar_coleccion'),

    #path('sentry-debug/', trigger_error),
    
]