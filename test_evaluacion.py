import unittest

from evaluacion import Evaluacion


def crear(calificacion):
    # Arrange común
    return Evaluacion("Cristhoper", "Restaurante A", calificacion, "Excelente servicio")


class TestEvaluacion(unittest.TestCase):

    def test_evaluacion_valida_se_publica(self):
        evaluacion = crear(5)
        resultado = evaluacion.verificar(True)
        evaluacion.publicar()
        self.assertTrue(resultado)
        self.assertEqual(evaluacion.estado, "Publicada")

    def test_evaluacion_sin_consumo_es_rechazada(self):
        evaluacion = crear(5)
        resultado = evaluacion.verificar(False)
        self.assertFalse(resultado)
        self.assertEqual(evaluacion.estado, "Rechazada")

    def test_calificacion_mayor_a_5_es_rechazada(self):
        evaluacion = crear(6)
        self.assertFalse(evaluacion.verificar(True))
        self.assertEqual(evaluacion.estado, "Rechazada")

    def test_calificacion_menor_a_1_es_rechazada(self):
        evaluacion = crear(0)
        self.assertFalse(evaluacion.verificar(True))
        self.assertEqual(evaluacion.estado, "Rechazada")

    def test_valores_limite_y_medio_son_validos(self):
        for valor in (1, 3, 5):
            with self.subTest(calificacion=valor):
                evaluacion = crear(valor)
                self.assertTrue(evaluacion.verificar(True))
                self.assertTrue(evaluacion.publicar())
                self.assertEqual(evaluacion.estado, "Publicada")

    def test_no_se_puede_publicar_sin_verificar(self):
        evaluacion = crear(5)
        self.assertFalse(evaluacion.publicar())
        self.assertEqual(evaluacion.estado, "Pendiente")


if __name__ == "__main__":
    unittest.main()
