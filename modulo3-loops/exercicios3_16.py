print('Média de notas')

lista_notas = []

for n in range(5):

    nota = float(input(f'Escreva a {n + 1}ª nota: '))

    lista_notas.append(nota)

    soma = sum(lista_notas)

quantidade_nota = len(lista_notas)

media = soma / quantidade_nota

print(f'A média dessas notas é de {media} pontos')
