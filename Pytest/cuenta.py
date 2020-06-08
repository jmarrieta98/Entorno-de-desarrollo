from dataclasses import dataclass

@dataclass
class CuentaBancanria:
    titular: str
    numero: str
    saldo: float
    tipoInteres: float
    saldo_minimo: float = 100

    def ingresar(self, Ingresar):
        self.saldo += Ingresar
        return self.saldo

    def retirar(self, Retirar):
        if self.saldo - Retirar >= self.saldo_minimo:
            self.saldo -= Retirar
        return self.saldo

    def verSaldo(self):
        return self.saldo

    def verTitular(self):
        return self.titular

    def verInteres(self):
        return self.tipoInteres

    def verSaldoMinimo(self):
        return self.saldo_minimo

    def cambiarTitular(self,nombre):
        self.titular = nombre
        return self.titular

    def cambiarSaldoMinimo(self,min):
        self.saldo_minimo = min
        return self.saldo_minimo

# poner titular             Echo
# ver titular               Echo
# retirar dinero            Echo
# ingresar dinero           Echo
# ver saldo                 Echo
# cambiar tipo de interes   Echo
# cambiar saldo minimo
# ver saldo mínimo          Echo
# ver tipo de interés       Echo


