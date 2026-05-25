from random import randint

print('Digite o mesmo número que o computador de 1 a 100')

numero_jogador = int(input('Digite seu número: '))

numero_maquina = randint(1, 100)

# print(numero_maquina)   # usei pra verificar a funcionalidade do código

while numero_jogador != numero_maquina:

    numero_jogador = int(input('Tente novamente: '))

    if numero_jogador == numero_maquina:

        print(f'Você acertou o número, que era {numero_maquina}')
