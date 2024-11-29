# Usar una imagen base de Python 3.13.0
FROM python:3.13.0-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos (como requirements.txt) al contenedor
COPY requirements.txt .

# Instalar las dependencias de Python (Django y cualquier otra librería)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto al contenedor
COPY . .

# Exponer el puerto que Django usará
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
