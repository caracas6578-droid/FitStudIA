from modules.planner import capturar_perfil, mostrar_rutina, guardar_rutina
from services.ai_service import generar_rutina_ia
from utils.validators import pedir_entero_rango


def ejecutar_aplicacion() -> None:
    print("==============================================")
    print("   FITSTUDIA - RECOMENDADOR INTELIGENTE       ")
    print("==============================================")

    # Bloque 1: Bucle principal del menú
    while True:
        print("\nMenú Principal:")
        print("1. Crear nueva rutina personalizada")
        print("2. Salir")

        opcion = pedir_entero_rango("Selecciona una opción (1-2): ", 1, 2)

        match opcion:
            case 2:
                print("¡Éxitos en tus metas! Cerrando FitStudIA...")
                break

            case 1:
                # Bloque 2: Orquestación del flujo completo
                perfil = capturar_perfil()
                print("\nConectando con Gemini API para construir tu rutina...")

                rutina = generar_rutina_ia(perfil)

                if rutina:
                    mostrar_rutina(rutina)
                    print("\n¿Deseas guardar esta rutina en un archivo local?")
                    print("1. Guardar como .txt | 2. Guardar como .json | 3. No guardar")
                    op_guardar = pedir_entero_rango("Elige una opción (1-3): ", 1, 3)

                    if op_guardar == 1:
                        guardar_rutina(rutina, perfil, formato="txt")
                    elif op_guardar == 2:
                        guardar_rutina(rutina, perfil, formato="json")


if __name__ == "__main__":
    ejecutar_aplicacion()