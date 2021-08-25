from interfacer_manipulador_log import Manipulador_De_Log


class Log_Em_Arquivo(Manipulador_De_Log):
    @classmethod
    def __init__(cls) -> None:
        cls.__nome_arquivo = "src/exercicios/log/log_em_arquivo_txt.txt"

    @classmethod
    def log(cls, logs_text):
        file = cls.__nome_arquivo
        with open(file, "a") as file_logs:
            file_logs.write(f"{logs_text}\n")
