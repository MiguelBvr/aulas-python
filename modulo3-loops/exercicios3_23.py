from random import randint

print('Tente digitar o mesmo número que o computador')

numero = int(input('Digite seu número: '))

numero_computador = randint(1, 10)

if numero == numero_computador:
    print('Você escolheu o mesmo número que a maquina, parabéns!')

else:
    print('Você não colocou o mesmo número que a máquina, tente novamente')


def adivinha_numero():
    numero_computador = randint(1, 10)
    contador = 1

    numero_jogador = int(input('Digite seu número: '))

    while numero_jogador != numero_computador:
        print(f'{contador}ª tentativa: A máquina não escolheu {numero_jogador}, tente novamente')
        numero_jogador = int(input('Digite seu número: '))
        contador += 1

    print('Você escolheu o mesmo número que a maquina, parabéns!')


adivinha_numero()
