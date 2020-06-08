import unittest
import ut_fizz_buzz


def multiplo_3(numero):
    """[summary]
    Autor:
        Benito Jódar

    Arguments:
        numero {[int]} -- [description]

    Returns:
        [fizz] -- [Si el numero es divisible entre 3]
        [numero] -- [si no es fizz]
    """
    if numero % 3 == 0:
        return "fizz"
    else:
        return numero


def multiplo_5(numero):
    """[summary]
    Autor:
        José Manuel Arrieta

    Arguments:
        numero {[int]} -- [description]

    Returns:
        [buzz] -- [Si el numero es divisible entre 5]
        [numero] -- [si no es buzz]
    """
    if numero % 5 == 0:
        return "buzz"
    else:
        return numero


def multiplo_3_y_5(numero):
    """[summary]
    Autor:
        Benito Jódar

    Arguments:
        numero {[int]} -- [description]

    Returns:
        [fizzbuzz] -- [Si el numero es divisible entre 3 y 5]
        [numero] -- [si no es fizzbuzz]
    """
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    else:
        return numero


def multiplos_3(lista):
    """[summary]
    Autor:
        José Manuel Arrieta

    Arguments:
        lista {[list int]} -- [description]

    Returns:
        [list] -- [Devuelve la lista con los numeros excepto los divisibles entre 3 que tiene fizz]
    """
    for i in range(0, len(lista)):
        if lista[i] % 3 == 0:
            lista[i] = "fizz"
    return lista


def multiplos_5(lista):
    """[summary]
    Autor:
        Benito Jódar

    Arguments:
        lista {[list int]} -- [description]

    Returns:
        [list] -- [Devuelve la lista con los numeros excepto los divisibles entre 5 que tiene buzz]
    """
    for i in range(len(lista)):
        if lista[i] % 5 == 0:
            lista[i] = "buzz"
    return lista


def multiplos_3_y_5(lista):
    """[summary]
    Autor:
    José Manuel Arrieta

    Arguments:
        lista {[list int]} -- [description]

    Returns:
        [list] -- [Devuelve la lista con los numeros excepto los divisibles entre 3 y 5 que tiene fizzbuzz]
    """
    for i in range(len(lista)):
        if lista[i] % 3 == 0 and lista[i] % 5 == 0:
            lista[i] = "fizzbuzz"
    return lista


def fizz_buzz(lista):
    """[summary]
    Autor:
        Benito Jódar

    Arguments:
        lista {[list int]} -- [description]

    Returns:
        [list] -- [Devuelve la lista en la que los divisibles entre 3 pone fizz los de 5 buzz y los de 3 y 5 fizzbuzz]

    """
    for i in range(len(lista)):
        if lista[i] % 3 == 0 and lista[i] % 5 == 0:
            lista[i] = "fizzbuzz"
        elif lista[i] % 3 == 0:
            lista[i] = "fizz"
        elif lista[i] % 5 == 0:
            lista[i] = "buzz"
    return lista


def contine_3(numero):
    """[summary]
    Autor:
        José Manuel Arrieta 

    Arguments:
        numero {[int]} -- [description]

    Returns:
        [fizz] -- [Si contiene un 3]
        [numero] -- [si no contiene un 3]
    """
    if "3" in str(numero):
        return "fizz"
    else:
        return numero


def contiene_5(numero):
    """[summary]
    Autor:
        Benito Jódar
    Arguments:
        numero {[int]} -- [description]

    Returns:
        [buzz] -- [Si contiene un 5]
        [numero] -- [si no contiene un 5]
    """
    if "5" in str(numero):
        return "buzz"
    else:
        return numero


def contiene_3_y_5(numero):
    """[summary]
    Autor:
        José Manuel Arrieta

    Arguments:
        numero {[int]} -- [description]

    Returns:
        [fizzbuzz] -- [Si contiene un 3 y 5]
        [numero] -- [si no contiene un 3 y 5]
    """
    if "3" in str(numero) and "5" in str(numero):
        return "fizzbuzz"
    else:
        return numero


def def_fizz_buzz(lista):
    """[summary]
    Autor:
        José Manuel Arrieta
    Arguments:
        lista {[list int]} -- [description]
    Returns:
        [list] -- [Devuelve la lista en la que los divisibles entre 3  y terminen en 3 pone fizz los divisibles de 5 y terminen en 5 buzz y los divisibles de 3 y 5 fizzbuzz]
    """
    for i in range(len(lista)):
        if lista[i] % 3 == 0 and lista[i] % 5 == 0 or "3" in str(lista[i]) and "5" in str(lista[i]):
            lista[i] = "fizzbuzz"
        elif lista[i] % 3 == 0 or "3" in str(lista[i]):
            lista[i] = "fizz"
        elif lista[i] % 5 == 0 or "5" in str(lista[i]):
            lista[i] = "buzz"
    return lista

   
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ut_fizz_buzz.Test_Fizz_Buzz))
    unittest.TextTestRunner(verbosity=1).run(suite)