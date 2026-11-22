import json
from utils.validators import pedir_entero_rango, pedir_texto_no_vacio


def capturar_perfil() -> dict:
    """Captura y valida los datos del usuario para armar su perfil."""
    print("\n--- CONFIGURACIÓN DE TU PERFIL FITSTUDIA ---")

    # Bloque 1: Selección de enfoque con match/case
    print("1. Fitness / Entrenamiento")
    print("2. Estudio / Aprendizaje")
    print("3. Ambos (Plan integral Fit + Estudio)")
    op_enfoque = pedir_entero_rango("Selecciona tu enfoque (1-3): ", 1, 3)

    match op_enfoque:
        case 1:
            enfoque = "Fitness"
        case 2:
            enfoque = "Estudio"
        case _:
            enfoque = "Fit y Estudio"

    # Bloque 2: Selección de nivel actual con match/case
    print("\nNivel actual: 1. Principiante | 2. Intermedio | 3. Avanzado")
    op_nivel = pedir_entero_rango("Selecciona tu nivel (1-3): ", 1, 3)

    match op_nivel:
        case 1:
            nivel = "Principiante"
        case 2:
            nivel = "Intermedio"
        case _:
            nivel = "Avanzado"

    # Bloque 3: Captura de edad, horas disponibles y objetivo principal
    edad = pedir_entero_rango("Ingresa tu edad (12-90 años): ", 12, 90)
    horas_dia = pedir_entero_rango("Horas disponibles por día (1-12): ", 1, 12)
    objetivo = pedir_texto_no_vacio("Describe tu objetivo principal: ")

    return {
        "enfoque": enfoque,
        "nivel": nivel,
        "edad": edad,
        "horas_dia": horas_dia,
        "objetivo": objetivo,
    }


def mostrar_rutina(rutina: dict) -> None:
    """Recorre la rutina semanal mediante bucles for y la imprime en consola (TC-05)."""
    print("\n" + "=" * 55)
    print(f"RUTINA: {rutina.get('titulo', 'Plan Personalizado').upper()}")
    print("=" * 55)
    print(f"Recomendación: {rutina.get('recomendacion_general', '')}\n")

    # Bloque 4: Bucle for por cada día y bucle for anidado por cada actividad
    for bloque_dia in rutina.get("dias", []):
        print(f"[{bloque_dia.get('dia', 'Día').upper()}] -> Foco: {bloque_dia.get('foco', '')}")
        for actividad in bloque_dia.get("actividades", []):
            print(f"   • {actividad}")
        print("-" * 45)


def guardar_rutina(rutina: dict, perfil: dict, formato: str = "txt") -> str:
    """Guarda la rutina generada en un archivo local .txt o .json."""
    nombre_base = f"rutina_{perfil['enfoque'].lower().replace(' ', '_')}"

    # Bloque 5: Persistencia local en JSON o TXT
    if formato == "json":
        nombre_archivo = f"{nombre_base}.json"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump({"perfil": perfil, "rutina": rutina}, archivo, ensure_ascii=False, indent=4)
    else:
        nombre_archivo = f"{nombre_base}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"FITSTUDIA - {rutina.get('titulo', '').upper()}\n")
            archivo.write(f"Enfoque: {perfil['enfoque']} | Nivel: {perfil['nivel']} | {perfil['horas_dia']}h/día\n")
            archivo.write(f"Objetivo: {perfil['objetivo']}\n")
            archivo.write("=" * 55 + "\n\n")

            for bloque_dia in rutina.get("dias", []):
                archivo.write(f"{bloque_dia.get('dia', '').upper()} - {bloque_dia.get('foco', '')}\n")
                for actividad in bloque_dia.get("actividades", []):
                    archivo.write(f"  - {actividad}\n")
                archivo.write("\n")

    print(f"\nArchivo guardado exitosamente como: {nombre_archivo}")
    return nombre_archivo