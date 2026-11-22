import json
from google import genai
from google.genai import types
from config.settings import GEMINI_API_KEY, MODEL_CANDIDATES


def generar_rutina_ia(perfil: dict, api_key: str | None = None) -> dict | None:
    """Envía el perfil del usuario a Google Gemini API y retorna la rutina en diccionario."""
    clave_activa = api_key if api_key is not None else GEMINI_API_KEY

    if not clave_activa:
        print("\n[Error en servicio de IA]: No se encontró una GEMINI_API_KEY válida en .env.")
        return None

    client = genai.Client(
        api_key=clave_activa,
        http_options=types.HttpOptions(timeout=90000),
    )

    prompt = f"""
    Actúa como entrenador físico y planificador académico.
    Crea una rutina semanal concisa para este perfil:
    - Enfoque: {perfil['enfoque']}
    - Edad: {perfil['edad']} años
    - Nivel: {perfil['nivel']}
    - Disponibilidad: {perfil['horas_dia']} horas/día
    - Objetivo: {perfil['objetivo']}

    Responde ÚNICAMENTE con un objeto JSON válido con esta estructura:
    {{
        "titulo": "Nombre corto de la rutina",
        "recomendacion_general": "Consejo breve en 1 oración",
        "dias": [
            {{
                "dia": "Lunes",
                "foco": "Tema o grupo muscular",
                "actividades": ["Bloque 1 (duración)", "Bloque 2 (duración)"]
            }}
        ]
    }}
    Reglas: Incluye los 7 días (Lunes a Domingo) con máximo 3 actividades breves por día.
    """

    for modelo in MODEL_CANDIDATES:
        try:
            respuesta = client.models.generate_content(
                model=modelo,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.7,
                    max_output_tokens=2048,
                ),
            )
            return json.loads(respuesta.text)

        except Exception as error:
            print(f"[Aviso IA]: Fallo con {modelo} ({error}).")

    print("\n[Error en servicio de IA]: Ningún modelo pudo responder en este momento.")
    return None