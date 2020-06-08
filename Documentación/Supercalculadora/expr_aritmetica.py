
class ExprAritmetica:
    """la clase ExprAritmetica aquella donde se realiza los operadores que van 
        a intervenir en factores numericos
    """
    def __es_numero__(self, cadena):
        """Se evalua si es cadena o numero el valor introducido y lo trasnforma a valor numerico,
        si es necesario
        
        :param cadena: String que lo vamos a transformar a entero
        :type cadena: Cadena
        :return: Evalua si es un error y devuelve
        :rtype: Booleano
        """
        
        try:
            int(cadena)
            return True
        except ValueError:
            return False

    def parse(self, exp):
        """Se evalua el operador que vamos a utilizar en la operacion con el valor numerico 

        :param exp: Operador que vamos utilizar 
        :type exp: Cadena
        :return: Diccionario de operadores y operandos
        :rtype: Diccionario
        """
        operandos = []
        operadores = []
        tokens = str.split(exp)
        for token in tokens:
            if self.__es_numero__(token):
                operandos.append(int(token))
            else:
                operadores.append(token)
        return {'Operandos': operandos, 'Operadores': operadores}
