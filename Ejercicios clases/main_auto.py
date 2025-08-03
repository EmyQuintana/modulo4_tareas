from auto import Vehiculo

class Auto(Vehiculo):
    def __init__(self, color, ruedas):
        super().__init__(color, ruedas)

    def arrancar(self):
        print("El auto arranco")