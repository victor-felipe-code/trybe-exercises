from random import sample, choice
import json

PALAVRAS = list()

with open("lista_palavras.json") as palavras:
    PALAVRAS = json.load(palavras)
CHANCES = 3


def embaralha_palavra(palavra: str) -> "str":
    return palavra, "".join(sample(palavra, len(palavra)))


def sorteia_palavra() -> "str":
    return embaralha_palavra(choice(PALAVRAS))


def adivinha_palavra():
    tentativas = 0
    acertos = 0
    while tentativas <= CHANCES:
        if acertos == 3:
            break
        palavra_atual, palavra_embaralhada = sorteia_palavra()
        print(f"Adivinhe a palavra  --> {palavra_embaralhada}")
        palavra_jogador = input()
        tentativas = tentativas + 1
        if palavra_atual == palavra_jogador:
            print("Você acertou.")
            acertos = acertos + 1
        else:
            print(
                f"Você errou | tentativas restantes: {CHANCES - tentativas }"
            )


adivinha_palavra()
