import os
import py7zr

# Recorre todos los archivos en la carpeta actual
for archivo in os.listdir('.'):
    if archivo.endswith('.7z') or '.7z.' in archivo:
        print(f"🔍 Extrayendo: {archivo}")
        try:
            with py7zr.SevenZipFile(archivo, mode='r') as z:
                # Extrae en una subcarpeta con el mismo nombre del archivo (sin extensión)
                nombre_carpeta = archivo.split('.7z')[0]
                os.makedirs(nombre_carpeta, exist_ok=True)
                z.extractall(path=nombre_carpeta)
            print(f"✅ Extraído en: {nombre_carpeta}")
        except Exception as e:
            print(f"❌ Error al extraer {archivo}: {e}")