from datetime import datetime
from typing import List, Type
from log_em_tela import Log_Em_Tela
from log_em_arquivo import Log_Em_Arquivo

from interfacer_manipulador_log import Manipulador_De_Log


class Log:
    def __init__(self) -> None:
        self.__manipuladores: List[Manipulador_De_Log] = []

    def __formatar(self, nivel: str, text: str) -> str:
        log_formatado = (
            f"[{nivel} "
            f"{datetime.today().strftime('%d/%m/%G-%H:%M:%S')}]: {text}"
        )

        return log_formatado

    def __log(self, nivel, log_text: str):
        for manipulador in self.__manipuladores:
            manipulador().log(self.__formatar(nivel, log_text))

    def adicionar_manipulador(
        self, manipulador: Type[Manipulador_De_Log]
    ) -> None:
        try:
            self.__manipuladores.append(manipulador)
        except Exception:
            print("Unknow error")

    def info(self, log_msg: str):
        nivel_servidor = "INFO"
        self.__log(nivel_servidor, log_msg)

    def alerta(self, log_msg: str):
        nivel_servidor = "ALERTA"
        self.__log(nivel_servidor, log_msg)

    def erro(self, log_msg: str):
        nivel_servidor = "ERRO"
        self.__log(nivel_servidor, log_msg)

    def debug(self, log_msg: str):
        nivel_servidor = "DEBUG"
        self.__log(nivel_servidor, log_msg)
