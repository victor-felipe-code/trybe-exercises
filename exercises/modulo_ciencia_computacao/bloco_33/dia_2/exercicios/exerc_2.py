# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa
# usuária tenha que adivinhar uma palavra que será mostrada com as letras
# mbaralhadas. O programa terá uma lista de palavras e escolherá uma
# aleatoriamente. O jogador terá três tentativas para adivinhar a palavra. Ao
# final a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou
# perdeu o jogo.
# 🦜 Para embaralhar uma palavra faça: scrambled_word = "".join(random.sample(
# word, len(word)))
# 🦜 O sorteio de uma palavra aleatória pode ser feito utilizando o método
# choice: random.choice(["word1", "word2", "word3"]) -> "word2" .

from random import sample, choice

PALAVRAS = ["banana", "maçã", "carro", "casa", "python", "HTML/CSS", "Marte"]
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
