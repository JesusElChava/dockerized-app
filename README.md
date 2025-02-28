Clasificación de Imágenes con IA usando Docker y MySQL

Introducción

Este proyecto es una aplicación web que permite clasificar imágenes utilizando un modelo de IA preentrenado (MobileNetV2). La aplicación está desarrollada con Streamlit y se ejecuta en un contenedor Docker, mientras que las predicciones se almacenan en una base de datos MySQL en otro contenedor.

Tecnologías usadas:

Python 3.9

Streamlit (para la interfaz web)

TensorFlow (modelo de clasificación de imágenes)

MySQL (base de datos para guardar predicciones)

Docker & Docker Compose (contenedores)

Estructura del proyecto:

.
├── app.py                   # Código principal de la aplicación
├── Dockerfile               # Instrucciones para construir la imagen Docker
├── docker-compose.yml       # Configuración de los servicios Docker
├── requirements.txt         # Librerías necesarias
└── README.md                # Esta guía de instalación

Instalación local:

Cómo clonar y ejecutar el proyecto

Si no tienes los archivos localmente, puedes clonarlos desde GitHub:

Clonar:
  git clone <URL_DEL_REPOSITORIO> (https://github.com/JesusElChava/dockerized-app.git)
Entrar al directorio:
  cd proyecto
Ejecutar con compose:
  docker-compose up --build

Abrir la aplicación en el navegador:

http://localhost:8501

Crear la imagen Docker:

docker pull jesusjesus15/clasificador:latest

Correr imagen descargada:

docker run -d --name mi_clasificador jesusjesus15/clasificador:latest

Abrir la aplicación en el navegador:

http://localhost:8501

Uso de la aplicación:

Subir imagen: Haz clic en el botón para cargar una imagen.

Clasificación: El modelo predice las clases más probables.

Guardar resultados: Las predicciones se almacenan automáticamente en la base de datos MySQL.

Consultar predicciones en MySQL:

Si quieres ver las predicciones almacenadas:

Acceder a la base de datos dentro del contenedor:

docker exec -it nombre_del_contenedor_mysql mysql -u usuario -p

Seleccionar la base de datos:

USE clasificacion;

Ver las predicciones:

SELECT * FROM predicciones;

Conclusión:

Con estos pasos, tu aplicación queda lista para ser ejecutada en cualquier máquina o compartida globalmente a través de Docker Hub. 


