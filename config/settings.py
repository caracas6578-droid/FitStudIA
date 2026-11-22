import os
from dotenv import load_dotenv

# Bloque 1: Carga de variables desde el archivo .env
load_dotenv()

# Bloque 2: Definición de credenciales y cadena de respaldo de modelos
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
MODEL_NAME = "gemini-4-hydrogen"

# Ordenados por prioridad y velocidad comprobada
MODEL_CANDIDATES = [
    MODEL_NAME,
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3.8-flash",
]