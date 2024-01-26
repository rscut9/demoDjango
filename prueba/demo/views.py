from django.shortcuts import render

from demo.utils.mongo_connection import MongoConn

from pymongo import MongoClient

# Vistas de la API

from django.shortcuts import render
from pymongo import MongoClient

def mostrar_coleccion(request):
    try:
        client = MongoClient('localhost', 27017)
        mydatabase = client.dumpmongo

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
                return render(request, 'ver_coleccion.html', {'colecciones': mydatabase.list_collection_names(), 'mensaje': mensaje})

    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'error_template.html', {'error_message': str(e)})

def ver_coleccion(request):
    try:
        client = MongoClient('localhost', 27017)
        mydatabase = client.dumpmongo
        colecciones = sorted(mydatabase.list_collection_names())

        return render(request, 'ver_coleccion.html', {'colecciones': colecciones})
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'error_template.html', {'error_message': str(e)})