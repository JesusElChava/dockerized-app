import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import mysql.connector

# Conectar a la base de datos MySQL
conn = mysql.connector.connect(
    host="db",                # Nombre del servicio en Docker Compose
    user="usuario",
    password="password",
    database="clasificacion"
)

cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS predicciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    imagen_nombre VARCHAR(255),
    clase VARCHAR(255),
    confianza FLOAT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Guardar predicción en la base de datos
def guardar_prediccion(nombre, clase, confianza):
    sql = "INSERT INTO predicciones (imagen_nombre, clase, confianza) VALUES (%s, %s, %s)"
    valores = (nombre, clase, float(confianza))
    cursor.execute(sql, valores)
    conn.commit()

# Cargar modelo preentrenado
model = tf.keras.applications.MobileNetV2(weights="imagenet")

def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def predict(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]
    return decoded_predictions

# Interfaz Streamlit
st.title("Clasificación de Imágenes con IA")
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)
    st.write("Clasificando...")
    
    predictions = predict(image)
    for class_id, class_name, score in predictions:
        st.write(f"{class_name}: {score * 100:.2f}%")
        
        # Guardar en la base de datos
        guardar_prediccion(uploaded_file.name, class_name, score * 100)

st.success("Predicción guardada en la base de datos")

# Cerrar la conexión
cursor.close()
conn.close()
