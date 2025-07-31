# Airplanes-detection-satellite-images
This repository contains all what I have used to create my own dataset and its use with the model for objects detection YOLOv8 .

# 1. Dataset Creation

## 1.1 Image Capture
The images were taken from Google Maps in different places around the world to create a dataset as diverse as possible. This includes:
> +100 images with airplanes (civilian and military)

> +100 images without airplanes

## 1.2 Preprocessing
The images were resized (960x960) and renamed using the script `images_prep.py`

## 1.3 Labeling
The images containing airplanes were manually labeled using [labelImg](https://github.com/HumanSignal/labelImg). And I obtained empty `.txt`files using `empty_files.py`

📂 Dataset available [here](https://www.kaggle.com/datasets/mgarch/airplane-detection-dataset)
