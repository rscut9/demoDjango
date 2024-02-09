from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CreateUserForm

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb://admin:admin%2B123%2B@localhost:27017/?authSource=admin')
mydatabase = client.test


def home(request):
    return render(request, 'home.html')

def exit(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # O redirecciona a la página que desees después del inicio de sesión exitoso
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        messages.error(request, 'Por favor, completa el formulario para iniciar sesión.')  # Agrega este mensaje si no es un método POST
    return render(request, 'login.html')

def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()

    return render(request, 'crear_usuario.html', {'form': form})

@login_required
# Mostrar la lista de colecciones disponibles
def ver_coleccion(request):
    try:
        # Obtiene la lista de colecciones y las ordena alfabéticamente
        colecciones = sorted(mydatabase.list_collection_names())

        # Renderiza la página 'ver_coleccion' con la lista de colecciones
        return render(request, 'ver_coleccion.html', {'colecciones': colecciones})
    except Exception as e:
        # Maneja cualquier excepción e imprime el mensaje de error
        print(f"Error: {e}")
        # Redirige a la página 'error_template' con el mensaje de error
        return render(request, 'error_template.html', {'error_message': str(e)})

# Mostrar los detalles de una colección
def mostrar_coleccion(request):
    try:
        # Si se ha enviado el formulario
        if request.method == 'GET':
            # Obtén el nombre de la colección desde la solicitud GET
            selected_collection = request.GET.get('coleccion', '')

            # Verifica que el nombre de la colección sea válido
            if selected_collection and selected_collection in mydatabase.list_collection_names():
                # Realiza la consulta a la colección seleccionada
                data = mydatabase[selected_collection].find()
                lista_datos = list(data)

                # Redirige a la página 'detalle_coleccion' con los datos
                return render(request, 'detalle_coleccion.html', {'coleccion': selected_collection, 'datos': lista_datos})
            else:
                mensaje = 'Colección no válida'
                # Redirige a la página 'ver_coleccion' con un mensaje de error
                return render(request, 'ver_coleccion.html', {'colecciones': mydatabase.list_collection_names(), 'mensaje': mensaje})

    except Exception as e:
        # Maneja cualquier excepción e imprime el mensaje de error
        print(f"Error: {e}")
        # Redirige a la página 'error_template' con el mensaje de error
        return render(request, 'error_template.html', {'error_message': str(e)})