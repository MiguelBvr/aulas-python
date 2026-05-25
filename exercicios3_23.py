from random import randint

print('Tente digitar o mesmo número que o computador')

numero = int(input('Digite seu número: '))

numero_computador = randint(1, 10)

if numero == numero_computador:
    print('Você escolheu o mesmo número que a maquina, parabéns!')

else:
    print('Você não colocou o mesmo número que a máquina, tente novamente')
