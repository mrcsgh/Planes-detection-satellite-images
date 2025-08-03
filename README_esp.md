# Detección de aviones en imágenes satelitales
Este repositorio contiene todo lo que he utilizado para crear mi propio conjunto de datos y utilizarlo con el modelo para la detección de objetos YOLOv8.

## 1. Creación del conjunto de datos

### 1.1 Captura de las imágenes
Las imágenes fueron tomadas con Google Maps en diferentes lugares del mundo para crear un conjunto de datos lo más divesificado posible. Este contiene:
> +100 imágenes con aviones (civiles y militares)

> +100 imágenes sin aviones

### 1.2 Preprocesamiento
Las imágenes se redimensionarion (960x960) y renombraron con el script `images_prep.py`

### 1.3 Etiquetado
Aquellas imágenes en las que aparecían aviones las etiqueté manualmente con [labelImg](https://github.com/HumanSignal/labelImg).
Y obtuve los archivos `.txt` vacíos para las imágenes sin aviones utilizando `empty_files.py`

### 1.4 Organizo las imágenes y etiquetas
Divido las imágenes y etiquetas `.txt` en entrenamiento y validación
> 222 imágenes etiquetadas para el entrenamiento (82% aprox)

> 50 imágenes etiquetadas para la validación (18% aprox)

### 1.5 Archivo `dataset.yaml`
Se escribe el archivo de configuración del conjunto de datos que incluye la ruta a las diferentes carpetas y los nombres que reciben las clases. En este caso una sola clase **0: airplane**

### 📂 Conjunto de datos disponible [aquí](https://www.kaggle.com/datasets/mgarch/airplane-detection-dataset)
