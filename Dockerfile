# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir streamlit tensorflow opencv-python pillow mysql-connector-python

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]

