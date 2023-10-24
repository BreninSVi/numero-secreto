from random import randint
from time import sleep


def linha():
    print('=-=' * 18)


def apresentacao():
    linha()
    print('Oi eu sou a IA, seu computador...\n'
          'Vou pensar em um número entre 0 e 10. Tente adivinhar!')
    linha()


def adivinhacao():
    palpites = 1
    computador = randint(0, 10)
    jogador = int(input('Qual é o seu palpite? '))

    sleep(0.5)

    while True:
        if computador > jogador:
            print('Mais... Tente mais uma vez.')
            jogador = int(input('Qual é o seu palpite? '))
            sleep(0.5)
            palpites += 1

        elif computador < jogador:
            print('Menos... Tente mais uma vez.')
            jogador = int(input('Qual é o seu palpite? '))
            sleep(0.5)
            palpites += 1

        else:
            if palpites <= 3:
                return f'PARABÉNS! Você conseguiu vencer com {palpites} tentativas!'
            else:
                return 'Que pena, você perdeu pois precisou de mais de 3 tentativas para acertar.'


apresentacao()

variavel = adivinhacao()
print(variavel)
