from abc import ABC, abstractclassmethod


class Manipulador_De_Log(ABC):
    @abstractclassmethod
    def log(cls, value):
        pass
