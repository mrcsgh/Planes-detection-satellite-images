import os
from PIL import Image


input_folder = r"/AirplanesDetection/images/planes"
output_folder = r"/AirplanesDetection/images/planes/resized"
new_width = 960
new_height = 960
file_prefix = "img"

# Create the output folder if it doesn´t exist
os.makedirs(output_folder, exist_ok=True)

# Obtain the file list
image_files = [f for f in os.listdir(input_folder)]

# Process the images
for i, filename in enumerate(image_files):
    input_path = os.path.join(input_folder, filename)
    output_filename = f"{file_prefix}{i+1}.png"
    output_path = os.path.join(output_folder, output_filename)

    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
            resized_img.save(output_path, "PNG")
            print(f"Saved: {output_filename}")
    except Exception as e:
        print(f"Error with {filename}: {e}")

print("Process completed.")

