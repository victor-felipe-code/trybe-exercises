"""Exercício 1: Lembra do exercício da TV que já abstraímos? Hoje vamos
implementar ele,porém com algumas modificações. Veja o diagrama abaixo:"""

"""Atributos:
volume - será inicializado com um valor de 50 e só pode estar entre 0 e 99;
canal - será inicializado com um valor de 1 e só pode estar entre 1 e 99;
ligada - será inicializado com o valor de False ,
pois está inicialmente desligado.
Todos os atributos devem ser privados.
Métodos:
aumentar_volume - aumenta o volume de 1 em 1 até o máximo de 99;
diminuir_volume - diminui o volume de 1 em 1 até o mínimo de 0;
modificar_canal - altera o canal de acordo com o parâmetro recebido e
deve lançar uma exceção ( ValueError ) caso o valor esteja fora dos limites;
ligar_desligar - alterna o estado da TV entre ligado e desligado (True/False).
"""


class TV:
    def __init__(self) -> None:
        self.__volume = 50
        self.__canal = 1
        self.__ligada = False
        self.ligar_desligar()

    def __str__(self) -> str:
        return f"TV LIGADA\nCANAL {self.__canal}"

    def getter_attribute(self, name):
        attributess = {
            "volume": self.__volume,
            "canal": self.__canal,
            "ligada": self.__ligada,
        }
        return attributess[name]

    def ligar_desligar(self) -> None:
        """LIGA E DESLIGA TV"""
        self.__ligada = True if not self.__ligada else False
        if self.__ligada:
            print("TV ligando...")
        else:
            print("DESLIGANDO...")

    def aumenta_volume(self, volume: int) -> None:
        """Aumentar o volume"""
        print(f"Volume: {self.__volume}")
        if self.__volume <= 99:
            self.__volume = self.__volume + 1
            print(f"Volume: {self.__volume}")
        else:
            print("Volume 99")

    def diminuir_volume(self, volume: int) -> None:
        """Diminuir o volume"""
        print(f"Volume: {self.__volume}")
        if self.__volume > 0:
            self.__volume = self.__volume - 1
            print(f"Volume: {self.__volume}")
        else:
            print("Volume 0")

    def mudar_canal(self, canal: int) -> None:
        """Muda canal da tv"""

        if 1 <= canal <= 99:
            self.__canal = canal
            print(f"CANAL  {self.__canal}")
        else:
            print("Canal não existe!!!")
            raise ValueError({"args": "Valor inválido"})


tv_1 = TV()
print(tv_1)
