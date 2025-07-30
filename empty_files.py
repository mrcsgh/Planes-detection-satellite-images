import os

folder = r"/PlanesDetection/images/others/resized"

# Obtain the file list
images_files = [f for f in os.listdir(folder)]

#Create the files .txt
for i, filename in enumerate(images_files):
    filename = filename.replace(".png", "")
    output_filename = f"{filename}.txt"
    output_paht = os.path.join(folder, output_filename)
    with open(output_paht, "w") as archivo:
            archivo.writelines('')

    print(f"File {output_filename} created.")

print("Process completed.")
