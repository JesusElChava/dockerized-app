# Clasificación de Imágenes con IA usando Streamlit y MySQL 

Este proyecto es una aplicación web construida con Streamlit que clasifica imágenes utilizando un modelo de IA preentrenado (**MobileNetV2**) y guarda las predicciones en una base de datos MySQL. Todo esto se ejecuta en contenedores Docker con Docker Compose.

## Requisitos
- **Docker** y **Docker Compose** instalados en tu máquina.
- Imagenes en formato **JPG**, **PNG** o **JPEG** para clasificar.

## Estructura del proyecto
```
├── app.py                 # Código principal de la aplicación Streamlit
├── Dockerfile             # Configuración para construir la imagen Docker
├── docker-compose.yml     # Orquestación de servicios con Docker Compose
└── README.md              # Documentación del proyecto
```

## Entrar a la ubicacion del docker compose

1. **Clonar el repositorio:**
```bash
cd <NOMBRE_DEL_PROYECTO_O_CARPETA>
```

2. **Construir y levantar los contenedores:**
```bash
sudo docker compose up --build
```

3. **Abrir la aplicación en el navegador:**
[http://localhost:8501](http://localhost:8501)

## Uso de la aplicación
1. **Sube una imagen:** Selecciona un archivo JPG, PNG o JPEG.
2. **Clasificación:** La IA analizará la imagen y mostrará las categorías con su probabilidad.
3. **Guardar en MySQL:** La predicción se almacena en la base de datos con:
   - **Nombre de la imagen**
   - **Categoría predicha**
   - **Confianza (%)**
   - **Fecha y hora**

## Ver resultados en MySQL

Si quieres ver las predicciones almacenadas, accede a MySQL desde el contenedor:
```bash
sudo docker exec -it proyecto-db-1 mysql -u usuario -p
```
Ingresa la contraseña (**password**, según tu `docker-compose.yml`).

Luego, consulta la tabla de predicciones:
```sql
USE clasificacion;
SELECT * FROM predicciones;
```

## Resultado esperado
```
+----+--------------------------+--------------------+-----------+---------------------+
| id | imagen_nombre            | clase              | confianza | fecha               |
+----+--------------------------+--------------------+-----------+---------------------+
|  1 | perro.jpg                | Cardigan           | 24.50     | 2025-02-25 12:30:00 |
|  2 | gato.png                 | Egyptian_cat       | 88.12     | 2025-02-25 12:35:00 |
+----+--------------------------+--------------------+-----------+---------------------+
```

## Detener los contenedores
Cuando termines, puedes bajar los contenedores con:
```bash
sudo docker compose down
```

## Conclusión
Esta aplicación te permite probar la clasificación de imágenes con IA en tiempo real y almacenar los resultados en MySQL. ¡Todo encapsulado en contenedores Docker para fácil despliegue! 
