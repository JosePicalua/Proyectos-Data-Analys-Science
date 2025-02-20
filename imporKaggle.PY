import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Ruta del archivo de API key
api_key_path = r'C:\Users\josep\.kaggle\kaggle.json'

# Solicitar el nombre del proyecto
project_name = input("Ingresa el nombre del proyecto: ").strip().replace(" ", "-").lower()

# Solicitar la carpeta donde guardar los archivos
download_path = input("Ingresa la ruta donde deseas guardar los archivos: ").strip()

# Crear la ruta final donde se guardará el dataset
final_path = os.path.join(download_path, project_name)
os.makedirs(final_path, exist_ok=True)

# Configurar la API manualmente
os.environ["KAGGLE_CONFIG_DIR"] = os.path.dirname(api_key_path)

# Inicializar la API
api = KaggleApi()
api.authenticate()

# Nombre de la competencia en minúsculas y sin espacios
competition = "house-prices-advanced-regression-techniques"

# Descargar archivos
api.competition_download_files(competition, path=final_path)

# Buscar el archivo ZIP descargado
zip_file = os.path.join(final_path, f"{competition}.zip")

# Descomprimir si el archivo existe
if os.path.exists(zip_file):
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(final_path)
    os.remove(zip_file)  # Eliminar el ZIP después de extraerlo
    print(f"Archivos descomprimidos en: {final_path}")
else:
    print("No se encontró el archivo ZIP.")
