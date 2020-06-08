import unittest
import expr_aritmetica


class TestsExprAritmetica(unittest.TestCase):
    """Clase Test de ExprAritmetrica

    :param TestCase: es una herencia para la clase 
    :type testCase: unittest
    """
    def setUp(self):
        """Es el inicializador de unittest que se hace setUp para traer la funcion
        """
        self.expresion = expr_aritmetica.ExprAritmetica()

    def test_extraer_operandos_y_operadores_en_2_mas_2(self):
        """Extrae operandos y operadores en la suma
        """
        self.assertEqual({'Operandos': [2, 2],
                          'Operadores': ['+']},
                         self.expresion.parse("2 + 2"))

    def test_extraer_operandos_y_operadores_en_10_entre_menos_5(self):
        """Extrae operandos y operadores de la resta
        """
        self.assertEqual({'Operandos': [10, -5],
                          'Operadores': ['/']},
                         self.expresion.parse("10 / -5"))

    def test_extraer_operandos_y_operadores_en_expr_sin_ptsis(self):
        """Extrae los operandos y operadores y quita los parentesis
        """
        self.assertEqual({'Operandos': [5, 4, 2, 2],
                          'Operadores': ['+', '*', '/']},
                         self.expresion.parse("5 + 4 * 2 / 2"))
