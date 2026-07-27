import os
import glob

# 1. Imprime el directorio de trabajo actual
print("CWD:", os.getcwd())   # completa con la función de os que devuelve el CWD

# 2. Construye la ruta al CSV declaraciones_dirty.csv usando os.path.join
ruta_csv = os.path.join("data", "inputs", "declaraciones_dirty.csv")
print("Ruta CSV:", ruta_csv)

# 3. Verifica si el archivo existe
print("¿Existe?", os.path.exists(ruta_csv))

# 4. Imprime solo el nombre del archivo (sin carpetas)
print("Nombre:", os.path.basename(ruta_csv))

# 5. Lista todos los archivos CSV en data/inputs/ (usa glob con el patrón *.csv)
csvs = glob.glob(os.path.join("data", "inputs", "*.csv"))
print("CSVs encontrados:", csvs)

def inventario_carpeta(carpeta: str) -> dict:
    """
    Retorna un diccionario {nombre_archivo: tamaño_en_bytes}
    para todos los archivos en la carpeta indicada.
    No incluye subdirectorios.
    """
    # Pista: os.path.getsize(ruta) retorna el tamaño en bytes de un archivo
    inventario = {}
    for nombre in os.listdir(carpeta):
        ruta = os.path.join(carpeta, nombre)
        if os.path.isfile(ruta):
            inventario[nombre] = os.path.getsize(ruta)
    return inventario

inventario = inventario_carpeta("data/inputs")
for nombre, tamano in inventario.items():
    print(f"  {nombre}: {tamano:,} bytes")