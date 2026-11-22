# FitStudIA – Recomendador Inteligente de Rutinas de Estudio y Fitness

Sistema modular por consola desarrollado en **Python 3.10+** que recopila los parámetros individuales del usuario (enfoque, nivel actual, edad, disponibilidad horaria diaria y objetivo principal) y los procesa mediante la **API de Google Gemini** para generar un plan semanal estructurado día por día.

**Autor:** Eddy Pinto  
**Institución:** Instituto Universitario de Tecnología Elías Calixto Pompa (IUTECP)  
**Asignatura:** Programación III[cite: 10]

---

## Características Principales

- **Menú interactivo:** Captura de perfil mediante estructuras modernas `match/case`.
- **Validación robusta:** Control de rangos y tipos de datos con bucles `while`, condicionales `if/else` y captura de excepciones `try/except ValueError`[cite: 3].
- **Integración con Google Gemini API:** Uso de `gemini-4-hydrogen` como modelo principal de baja latencia, con conmutación automática hacia modelos de respaldo (`gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-3.8-flash`) ante tiempos de espera agotados o picos de demanda[cite: 3].
- **Salida estructurada y exportación:** Recorrido semanal mediante ciclos `for` anidados y guardado local en formato `.txt` o `.json`[cite: 3].
- **Pruebas unitarias:** Suite automatizada (`unittest`) que certifica los casos de prueba TC-01 a TC-05[cite: 3].

---

## Estructura del Proyecto

```text
fitstudy_planner/
├── config/
│   └── settings.py          # Lectura de API Key desde .env y configuración de modelos
├── services/
│   └── ai_service.py        # Conexión con Google Gemini API, prompt JSON y respaldo automático
├── utils/
│   └── validators.py        # Validaciones de entrada con while, if/else y ValueError
├── modules/
│   └── planner.py           # Captura de perfil, impresión semanal y exportación .txt/.json
├── tests/
│   └── test_planner.py      # Scripts de prueba automatizados (TC-01 a TC-05)
├── .env.example             # Plantilla de configuración de variables de entorno
├── .gitignore               # Exclusión de entorno virtual y credenciales privadas
├── main.py                  # Punto de entrada principal de la aplicación
└── README.md                # Documentación del proyecto
```
