class Calculadora:
    """[summary]
    """
    def sumar(self, a:int, b:int) -> int:
        """[summary]

        :param a: [description]
        :type a: [type]
        :param b: [description]
        :type b: [type]
        :return: [description]
        :rtype: int
        """
        return a + b

    def restar(self, a, b):
        """[summary]

        :param a: [description]
        :type a: [type]
        :param b: [description]
        :type b: [type]
        :return: [description]
        :rtype: [type]
        """
        return a - b

    def multiplicar(self, a, b):  # n
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return ZeroDivisionError
        if a % b != 0:
            return ValueError
        else:
            return a // b  # En Python 2.x esto funciona sin problemas, pero en Python 3, no. ¿Sabes arreglarlo?
