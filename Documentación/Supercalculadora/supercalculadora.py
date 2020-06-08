import expr_aritmetica
import calculadora


class Supercalculadora:
    """Clase supercalculdora que realiza operaciones simplificaciones y calculos elementales
    """
    def __init__(self, parser):
        """[summary]

        :param parser: [description]
        :type parser: [type]
        """
        self.calc = calculadora.Calculadora()
        self.parser = parser

    def __operar__(self, expr_descompuesta):
        """Operador de la clase supercalculadora
        
        :param expr_descompuesta: Tiene como claves operadores y operandos y sus valores son una lista de operadores y opeandos respectivamente
        :type expr_descompuesta: Diccionario
        :return: La posición de la operación y el calculo de dicha operación
        :rtype: Entero y entero
        """
        i = None
        res_intermedio = 0
        # intercambiar / y * por el error de la división
        if '*' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('*')
            res_intermedio = self.calc.multiplicar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        elif '/' in expr_descompuesta['Operadores']: 
            i = expr_descompuesta['Operadores'].index('/') 
            res_intermedio = self.calc.dividir(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])  
        elif '-' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('-')
            res_intermedio = self.calc.restar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        elif '+' in expr_descompuesta['Operadores']:
            i = expr_descompuesta['Operadores'].index('+')
            res_intermedio = self.calc.sumar(
                expr_descompuesta['Operandos'][i],
                expr_descompuesta['Operandos'][i + 1])
        else:
            # Es un error, tenemos que decidir que hacer en los test
            # siguientes
            # Forzamos el error para que no haya problemas luego
            assert False
        return (i, res_intermedio)

    def __simplificar__(self, expr_descompuesta):
        """Simplificador de la clase supercalculadora
        
        :param expr_descompuesta: Tiene como claves operadores y operandos y sus valores son una lista de operadores y opeandos respectivamente
        :type expr_descompuesta: Diccionario
        :return: El valor de la operación realizada
        :rtype: Entero
        """
        if expr_descompuesta['Operadores'] == []:
            return expr_descompuesta
        else:
            (i, res_intermedio) = self.__operar__(expr_descompuesta)
            expr_simplificada = expr_descompuesta
            expr_simplificada['Operadores'].pop(i)
            expr_simplificada['Operandos'].pop(i)
            expr_simplificada['Operandos'].pop(i)
            expr_simplificada['Operandos'].insert(i, res_intermedio)

            return self.__simplificar__(expr_simplificada)

    def calcular(self, expresion):
        """Metodo calcular de la clase supercalculadora
        
        :param expresion: Tiene como claves operadores y operandos y sus valores son una lista de operadores y opeandos respectivamente
        :type expresion: Diccionario
        :return: El valor de la operación realizada
        :rtype: Entero
        """
        return str(self.__simplificar__(
            self.parser.parse(expresion))['Operandos'][0])