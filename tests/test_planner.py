import io
import unittest
from unittest.mock import patch, MagicMock
from utils.validators import pedir_entero_rango
from services.ai_service import generar_rutina_ia
from modules.planner import mostrar_rutina


class TestFitStudIA(unittest.TestCase):

    # TC-01: Rechazo de horas fuera de rango (-3 y 25) hasta recibir valor válido (2)
    @patch("builtins.input", side_effect=["-3", "25", "2"])
    def test_tc01_horas_fuera_de_rango(self, mock_input):
        resultado = pedir_entero_rango("Horas: ", 1, 12)
        self.assertEqual(resultado, 2)
        self.assertEqual(mock_input.call_count, 3)

    # TC-02: Captura de ValueError ante entrada no numérica ("tres")
    @patch("builtins.input", side_effect=["tres", "3"])
    def test_tc02_entrada_no_numerica(self, mock_input):
        resultado = pedir_entero_rango("Horas: ", 1, 12)
        self.assertEqual(resultado, 3)
        self.assertEqual(mock_input.call_count, 2)

    # TC-03: Llamada exitosa a Gemini API con perfil válido
    @patch("services.ai_service.genai.Client")
    def test_tc03_llamada_api_valida(self, mock_client_cls):
        mock_respuesta = MagicMock()
        mock_respuesta.text = '{"titulo": "Plan Estudio", "recomendacion_general": "Constancia", "dias": [{"dia": "Lunes", "foco": "Python", "actividades": ["Práctica 2h"]}]}'
        mock_client_cls.return_value.models.generate_content.return_value = mock_respuesta

        perfil = {"enfoque": "Estudio", "edad": 20, "nivel": "Principiante", "horas_dia": 2, "objetivo": "Dominar Python"}
        rutina = generar_rutina_ia(perfil, api_key="clave_valida_simulada")

        self.assertIsNotNone(rutina)
        self.assertEqual(rutina["titulo"], "Plan Estudio")

    # TC-04: Captura de error ante falla de red o API Key inválida
    @patch("services.ai_service.genai.Client")
    def test_tc04_falla_red_o_api_invalida(self, mock_client_cls):
        mock_client_cls.return_value.models.generate_content.side_effect = Exception("API_KEY_INVALID")

        perfil = {"enfoque": "Fitness", "edad": 22, "nivel": "Intermedio", "horas_dia": 1, "objetivo": "Fuerza"}
        rutina = generar_rutina_ia(perfil, api_key="clave_erronea")

        self.assertIsNone(rutina)

    # TC-05: Verificar recorrido e impresión semanal mediante ciclo for
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_tc05_impresion_rutina_semanal(self, mock_stdout):
        rutina_ejemplo = {
            "titulo": "Semana FitStudIA",
            "recomendacion_general": "Mantén el ritmo",
            "dias": [
                {"dia": d, "foco": "Bloque diario", "actividades": ["Actividad 1h"]}
                for d in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            ],
        }
        mostrar_rutina(rutina_ejemplo)
        salida = mock_stdout.getvalue()

        for dia in ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]:
            self.assertIn(dia, salida)


if __name__ == "__main__":
    unittest.main()