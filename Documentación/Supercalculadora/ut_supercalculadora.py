import unittest
import supercalculadora
import expr_aritmetica
import ut_calculadora
import ut_expr_aritmetica


class TestsSupercalculadora(unittest.TestCase):
    """Clase Test de Supercalculadora

    :param unittest: [description]
    :type unittest: [type]
    """
    def setUp(self):
        """Inicializa la expresion aritmétrica para que los unittest pueda utilizarlo

        :param unittest: Si mismo
        :type unittest: TestSupercalculadora
        """
        self.sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica())

    def test_sumar(self):
        """Comprueba si la función sumar no tiene errores
        """
        self.assertEqual("4", self.sc.calcular("2 + 2"))

    def test_restar(self):
        """Comprueba si la función restar no tiene errores
        """
        self.assertEqual("0", self.sc.calcular("2 - 2"))

    def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
        """Comprueba si la función de la expresión compleja sin precedensia no tiene errores
        """
        self.assertEqual("6", self.sc.calcular("5 + 4 - 3"))

# añade función de simplificar
    def test_expresion_compleja_sin_parentesis_con_precedencia(self):
        """Comprueba si la función de la expresión compleja con precedensia no tiene errores
        """
        self.assertEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))
        self.assertEqual("-1", self.sc.calcular("4 / 2 - 3"))
        self.assertEqual("1", self.sc.calcular("4 / 2 - 3 + 1 + 6 / 3 - 1"))
        self.assertEqual(
            "-8", self.sc.calcular("4 / -2 + 3 + -1 + -6 / -3 - 10"))
