class Calculadora:
    """Clase calculadora que realiza las operaciones matematicas mas elementales con numeros enteros
    """
    def sumar(self, a, b):
        """Suma dos numeros enteros y de vuelve su suma

        :param a: Primer numero de la suma
        :type a: entero
        :param b: Segundo numero de la suma
        :type b: entero
        :return: Suma de los parametros a y b
        :rtype: entero
        """
        return a + b

    def restar(self, a, b):
        """Resta dos numeros enteros y devuelve su resta

        :param a: Primer número de la resta
        :type a: Entero
        :param b: Segundo número dela resta
        :type b: Entero
        :return: Resta de a menos b 
        :rtype: entero
        """
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos numeros enteros y devuelve su multiplicacion

        :param a: Primer numero de la multiplicación
        :type a: entero
        :param b: Segundo numero de la multiplicación
        :type b: entero
        :return: Multiplicación de a por b
        :rtype: entero
        """
        return a * b

    def dividir(self, a, b):
        """Divide dos números enteros y devuelve su cociente

        :param a: Dividendo de la división
        :type a: Entero
        :param b: Divisor de la división
        :type b: Entero
        :return: Error al dividir entre 0 ó error si el resto no es 0 ó el cociente de la división. 
        :rtype: Entero ó error.
        """
        if b == 0:
            return ZeroDivisionError
        if a % b != 0:
            return ValueError
        else:
            return a // b
