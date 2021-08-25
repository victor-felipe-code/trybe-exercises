from statistics import mean, median, mode


class Estatistica:
    @staticmethod
    def media(value):
        return mean(value)

    @staticmethod
    def mediana(value):
        return median(value)

    @staticmethod
    def moda(value):
        return mode(value)
