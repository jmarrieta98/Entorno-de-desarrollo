import unittest
import fizz_buzz


class Test_Fizz_Buzz(unittest.TestCase):

    def test_multiplo_3(self):
        """[summary]
        Autor:
            José Manuel Arrieta
        """
        numero = 9
        self.assertEqual("fizz", fizz_buzz.multiplo_3(numero))

    def test_multiplo_5(self):
        """[summary]
        Autor:
            Benito Jódar
        """
        numero = 10
        self.assertEqual("buzz", fizz_buzz.multiplo_5(numero))

    def test_multiplo_3_y_5(self):
        """[summary]
        Autor:
            José Manuel Arrieta
        """
        numero = 15
        self.assertEqual("fizzbuzz", fizz_buzz.multiplo_3_y_5(numero))

    def test_multiplos_3(self):
        """[summary]
        Autor:
            Benito Jódar
        """
        lista = [i for i in range(1, 31)]
        resultado = [1, 2, "fizz", 4, 5, "fizz", 7, 8, "fizz", 10, 11, "fizz", 13, 14, "fizz",
                     16, 17, "fizz", 19, 20, "fizz", 22, 23, "fizz", 25, 26, "fizz", 28, 29, "fizz"]
        self.assertEqual(resultado, fizz_buzz.multiplos_3(lista))

    def test_multiplos_5(self):
        """[summary]
        Autor:
            José Manuel Arrieta
        """
        lista = [i for i in range(1, 31)]
        resultado = [1, 2, 3, 4, "buzz", 6, 7, 8, 9, "buzz", 11, 12, 13, 14, "buzz",
                     16, 17, 18, 19, "buzz", 21, 22, 23, 24, "buzz", 26, 27, 28, 29, "buzz"]
        self.assertEqual(resultado, fizz_buzz.multiplos_5(lista))

    def test_multiplos_3_y_5(self):
        """[summary]
        Autor:
            Benito Jódar
        """
        lista = [i for i in range(1, 31)]
        resultado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, "fizzbuzz",
                     16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, "fizzbuzz"]
        self.assertEqual(resultado, fizz_buzz.multiplos_3_y_5(lista))

    def test_fizz_buzz(self):
        """[summary]
        Autor:
            José Manuel Arrieta
        """
        lista = [i for i in range(1, 31)]
        resultado = [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14,
                    "fizzbuzz",16, 17, "fizz", 19, "buzz", "fizz", 22, 23, "fizz", "buzz", 26, 
                    "fizz", 28, 29, "fizzbuzz"]
        self.assertEqual(resultado, fizz_buzz.fizz_buzz(lista))

    def test_contiene_3(self):
        """[summary]
        Autor:
            Benito Jódar
        """
        numero = 34
        self.assertEqual("fizz",fizz_buzz.contine_3(numero))

    def test_contiene_5(self):
        """[summary]
        Autor:
            José Manuel Arrieta
        """
        numero = 50
        self.assertEqual("buzz",fizz_buzz.contiene_5(numero))

    def test_contiene_3_y_5(self):
        """[summary]
        Autor:
            Benito Jódar
        """
        numero = 35
        self.assertEqual("fizzbuzz",fizz_buzz.contiene_3_y_5(numero))

    def test_def_fizz_buzz(self):
        """[summary]
        Autor:
            Benito Jódar
        """
        lista = [i for i in range(1, 36)]
        resultado = [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", "fizz", 14,
                    "fizzbuzz", 16, 17, "fizz", 19, "buzz", "fizz", 22, "fizz","fizz", "buzz", 26,
                    "fizz", 28, 29, "fizzbuzz","fizz","fizz","fizz","fizz","fizzbuzz"]
        self.assertEqual(resultado, fizz_buzz.def_fizz_buzz(lista))
