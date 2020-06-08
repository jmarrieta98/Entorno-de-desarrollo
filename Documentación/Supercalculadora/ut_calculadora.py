import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    """Clase Test de Supercalculadora

    :param TestCase: Herencia de unittest
    :type testCase: unittest
    """
    def setUp(self):
        """Inicializa la calculadora para que los unittest pueda utilizarlo

        :param unittest: Si mismo
        :type unittest: Testcalculadora
        """
        self.calc = calculadora.Calculadora()

    def test_sumar_2_y_2(self):
        """ Test que comprueba que suma de 2 + 2 es 4
        """
        self.assertEqual(4, self.calc.sumar(2, 2))

    def test_sumar_5_y_7(self):
        """Test que comprueba que la suma de 5 y 7 es 12
        """
        self.assertEqual(12, self.calc.sumar(5, 7))

    def test_sumar_propiedad_conmutativa(self):
        """Test que comprueba la propiedad conmutativa en la suma
        """
        self.assertEqual(self.calc.sumar(5, 7),
                         self.calc.sumar(7, 5))

    def test_restar_5_y_3(self):
        """Test que comprueba que la resta de 5 y 3 es 2
        """
        self.assertEqual(2, self.calc.restar(5, 3))

    def test_restar_2_y_3(self):
        """Test que comprueba que la resta de 2 y 3 es -1
        """
        self.assertEqual(-1, self.calc.restar(2, 3))

    def test_restar_no_propiedad_conmutativa(self):
        """Test que comprueba la propiedad no conmutativa de la resta
        """
        self.assertNotEqual(self.calc.restar(5, 3),
                            self.calc.restar(3, 5))

    def test_sumar_numeros_negativos(self):
        """Test que comprueba la suma de numeros negativos
        """
        self.assertEqual(0, self.calc.sumar(2, -2))

    def test_restar_numeros_negativos(self):
        """Test que comprueba la resta de numeros negativos
        """
        self.assertEqual(-7, self.calc.restar(-5, 2))
        self.assertEqual(-5, self.calc.restar(-7, -2))

    def test_division_exacta(self):
        """Test que comprueba la división exacta positiva
        """
        self.assertEqual(1, self.calc.dividir(2, 2))
        self.assertEqual(2, self.calc.dividir(10, 5))

    def test_division_exacta_negativa(self):
        """Test que comprueba la división exacta negativa
        """
        self.assertEqual(-2, self.calc.dividir(10, -5))
        self.assertEqual(2, self.calc.dividir(-10, -5))

    def test_division_no_entera_da_excepcion(self):
        """Test que comprueba que el resultado de la división es entero.
        """
        self.assertEqual(ValueError, self.calc.dividir(3, 2))

    def test_division_por_0(self):
        """Test que comprueba que el divisor de la division es 0.
        """
        self.assertEqual(ZeroDivisionError, self.calc.dividir(3, 0))

    def test_multiplicar_simple(self):  
        """Test que comprueba que la multiplicación con números positivos funciona correctamente.
        """
        self.assertEqual(8, self.calc.multiplicar(4, 2))

    def test_multiplicar_negativa(self):
        """ Test que comprueba que la multiplicación con números negativos funciona correctamente.

        """
        self.assertEqual(-8, self.calc.multiplicar(-4, 2))
        self.assertEqual(-8, self.calc.multiplicar(4, -2))
        self.assertEqual(8, self.calc.multiplicar(-4, -2))
