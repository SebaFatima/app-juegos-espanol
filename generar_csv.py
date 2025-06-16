import os
import csv

carpeta_imagenes = "imagenes"
archivo_salida = "data/catalogo.csv"

# Asegurar que la carpeta de salida exista
os.makedirs("data", exist_ok=True)

# Crear archivo CSV
with open(archivo_salida, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["tema", "palabra", "path_imagen"])

    for tema in os.listdir(carpeta_imagenes):
        ruta_tema = os.path.join(carpeta_imagenes, tema)
        if os.path.isdir(ruta_tema):
            for archivo in os.listdir(ruta_tema):
                if archivo.endswith((".png", ".jpg", ".jpeg")):
                    palabra = os.path.splitext(archivo)[0].lower()
                    path_relativo = os.path.join(carpeta_imagenes, tema, archivo).replace("\\", "/")
                    writer.writerow([tema.lower(), palabra, path_relativo])

print("✅ CSV generado exitosamente en:", archivo_salida)
