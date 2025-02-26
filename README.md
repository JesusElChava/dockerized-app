🚀 Clasificador de Imágenes con IA

Este proyecto es una aplicación web que clasifica imágenes usando un modelo de Machine Learning (MobileNetV2) y almacena las predicciones en una base de datos MySQL. La aplicación se empaqueta en un contenedor Docker y se distribuye a través de Docker Hub para que cualquiera pueda ejecutarla fácilmente.

🛠️ Tecnologías usadas:

Python 3.9

Streamlit (para la interfaz web)

TensorFlow (modelo de clasificación de imágenes)

MySQL (base de datos para guardar predicciones)

Docker & Docker Compose (contenedores)

📂 Estructura del proyecto:

.
├── app.py                   # Código principal de la aplicación
├── Dockerfile               # Instrucciones para construir la imagen Docker
├── docker-compose.yml       # Configuración de los servicios Docker
├── requirements.txt         # Librerías necesarias
└── README.md                # Esta guía de instalación

🧩 Instalación local:

Clonar el repositorio:

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

Crear la imagen Docker:

docker build -t tu_usuario/clasificador:latest .

Levantar los contenedores (aplicación y base de datos):

docker-compose up

Abrir la aplicación en el navegador:

http://localhost:8501

🐳 Distribución con Docker Hub:

Iniciar sesión en Docker Hub:

docker login

Etiquetar la imagen:

docker tag clasificador:latest tu_usuario/clasificador:latest

Subir la imagen a Docker Hub:

docker push tu_usuario/clasificador:latest

Descargar y ejecutar la aplicación desde cualquier máquina con Docker:

docker pull tu_usuario/clasificador:latest

docker run -p 8501:8501 tu_usuario/clasificador:latest

Acceder a la aplicación:

http://localhost:8501

🟩 Uso de la aplicación:

Subir imagen: Haz clic en el botón para cargar una imagen.

Clasificación: El modelo predice las clases más probables.

Guardar resultados: Las predicciones se almacenan automáticamente en la base de datos MySQL.

📘 Consultar predicciones en MySQL:

Si quieres ver las predicciones almacenadas:

Acceder a la base de datos dentro del contenedor:

docker exec -it nombre_del_contenedor_mysql mysql -u usuario -p

Seleccionar la base de datos:

USE clasificacion;

Ver las predicciones:

SELECT * FROM predicciones;

🎯 Conclusión:

Con estos pasos, tu aplicación queda lista para ser ejecutada en cualquier máquina o compartida globalmente a través de Docker Hub. 🚀


