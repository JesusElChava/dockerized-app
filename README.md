Clasificación de Imágenes con IA usando Streamlit y MySQL

Este proyecto es una aplicación web que clasifica imágenes con un modelo de IA (MobileNetV2) y guarda los resultados en una base de datos MySQL. Todo corre en contenedores Docker gracias a Docker Compose.
Estructura del proyecto:

├── app.py                 # Código principal de la aplicación
├── Dockerfile             # Configuración para crear la imagen Docker
├── docker-compose.yml     # Orquestación de servicios con Docker Compose
└── README.md              # Documentación del proyecto

Cómo clonar y ejecutar la aplicación:

    Clonar el repositorio:

git clone https://github.com/JesusElChava/dockerized-app.git

    Entrar al directorio del proyecto:

cd dockerized-app

    Construir y levantar los contenedores:

sudo docker compose up --build

    Abrir la aplicación en el navegador:
    http://localhost:8501

Uso de la aplicación:

    Subir una imagen: Selecciona un archivo JPG, PNG o JPEG.
    Clasificación: La IA analizará la imagen y mostrará las categorías con su probabilidad.
    Guardar en MySQL: La predicción se almacena con:
        Nombre de la imagen
        Categoría predicha
        Confianza (%)
        Fecha y hora

Ver resultados en MySQL:

Accede a la base de datos desde el contenedor:

sudo docker exec -it proyecto-db-1 mysql -u usuario -p

(Usa la contraseña definida en tu docker-compose.yml)

Consulta los resultados:

USE clasificacion;
SELECT * FROM predicciones;

Detener los contenedores:

Cuando termines, baja los contenedores con:

sudo docker compose down

Conclusión:

Este proyecto te permite clasificar imágenes con IA en tiempo real y guardar los resultados en MySQL. Todo encapsulado en Docker para facilitar su despliegue.



