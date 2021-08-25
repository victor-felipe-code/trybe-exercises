from interface_figura import Figura_Geometrica
import math


class Circulo(Figura_Geometrica):
    def __init__(self, raio) -> None:
        self.raio = raio

    def area(self):
        print(f"Area: {math.pi * math.pow(self.raio, 2)}")

    def perimetro(self):
        print(f"Perimetro: {self.raio * 2}")


c = Circulo(5)
c.area()
c.perimetro()
