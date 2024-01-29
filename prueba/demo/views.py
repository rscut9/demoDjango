from django.shortcuts import render
from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
mydatabase = client.dumpmongo

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
