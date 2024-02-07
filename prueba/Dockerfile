# Dockerfile para la aplicación principal (backend) Django

# Utiliza la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido actual del directorio al directorio de trabajo
COPY . .

# Expone el puerto en el que la aplicación se ejecuta
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver"]
