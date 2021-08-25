from interface_figura import Figura_Geometrica


class Retangulo(Figura_Geometrica):
    def __init__(self, base, altura) -> None:
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        print(f"Area: {self.base * self.altura}")

    def perimetro(self):
        print(f"Perimetro: {sum([(self.altura * 2), (self.base * 2)])}")
