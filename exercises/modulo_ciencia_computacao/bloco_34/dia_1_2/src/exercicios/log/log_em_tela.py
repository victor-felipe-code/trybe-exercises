from interfacer_manipulador_log import Manipulador_De_Log


class Log_Em_Tela(Manipulador_De_Log):
    @classmethod
    def log(cls, logs_text):
        print("-" * (len(logs_text) + 4))
        print(f"| {logs_text} |")
        print("-" * (len(logs_text) + 4))
