import random
import pytest
from cuenta import *

cant_inicial = [random.randint(100, 5000)for _ in range(100)]
a_ingresar = [random.randint(100, 5000)for _ in range(100)]
a_retirar = [random.randint(100, 5000)for _ in range(100)]

testdata1 = [(cant_inicial[i], a_ingresar[i], cant_inicial[i]+a_ingresar[i])
             for i in range(len(cant_inicial))]

testdata2 = []
for i in range(len(cant_inicial)):
    if cant_inicial[i] - a_retirar[i] < 100:
        testdata2.append((cant_inicial[i], a_retirar[i], cant_inicial[i]))
    else:
        testdata2.append((cant_inicial[i], a_retirar[i], cant_inicial[i] - a_retirar[i]))



@pytest.mark.parametrize("cant_inicial,entrada,res_esperada", testdata1)
def testIngresar(cant_inicial, entrada, res_esperada):
    cuenta = CuentaBancanria("Arrieta", "1234-31233", cant_inicial, 0.1)
    assert cuenta.ingresar(entrada) == pytest.approx(res_esperada)

@pytest.mark.parametrize("cant_inicial,entrada,res_esperada", testdata2)
def testRetirar(cant_inicial, entrada, res_esperada):
    cuenta = CuentaBancanria("Arrieta", "1234-31233", cant_inicial, 0.1)
    assert cuenta.retirar(entrada) == pytest.approx(res_esperada)