def pedir_entero_rango(mensaje: str, minimo: int, maximo: int) -> int:
    """Solicita un entero por consola hasta que sea numérico y esté dentro del rango."""
    # Bloque 1: Bucle while para insistir mientras el dato sea inválido
    while True:
        entrada = input(mensaje).strip()

        # Bloque 2: Manejo de excepciones ante entradas no numéricas (TC-02)
        try:
            valor = int(entrada)
        except ValueError:
            print("Error: Entrada no numérica. Por favor, ingresa un número entero válido.")
            continue

        # Bloque 3: Validación de rango permitido con if/else (TC-01)
        if minimo <= valor <= maximo:
            return valor
        else:
            print(f"Error: El valor debe estar entre {minimo} y {maximo}. Intenta de nuevo.")


def pedir_texto_no_vacio(mensaje: str) -> str:
    """Evita que el usuario deje campos de texto obligatorios vacíos."""
    while True:
        texto = input(mensaje).strip()
        if len(texto) >= 3:
            return texto
        else:
            print("Error: Debes ingresar una descripción válida (mínimo 3 caracteres).")