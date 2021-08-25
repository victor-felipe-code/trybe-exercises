from interface_figura import Figura_Geometrica


class Quadrado(Figura_Geometrica):
    def __init__(self, lado) -> None:
        super().__init__()
        self.lado = lado

    def area(self):
        print(f"Area: {self.lado**2}")

    def perimetro(self):
        print(f"Perimetro: {sum([self.lado for x in range(0, 4)])}")
