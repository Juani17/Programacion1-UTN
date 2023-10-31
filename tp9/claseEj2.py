# Define la clase Cuenta
class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    def get_saldo(self):
        return self.saldo

    def mostrar(self):
        print(f"El titular es: {self.get_titular()}")
        print(f"El saldo es: {self.get_saldo()}")

    def ingresar(self, cantidad):
        if cantidad < 0:
            print("No se pueden realizar ingresos negativos.")
            return
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad < 0:
            print("No se pueden realizar retiros negativos.")
            return
        if cantidad > self.saldo:
            print("Saldo insuficiente.")
            return
        self.saldo -= cantidad