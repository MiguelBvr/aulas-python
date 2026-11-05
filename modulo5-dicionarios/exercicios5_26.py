nome = None
boletim = {}

while nome != 'fim' and nome != 'FIM':
    nome = input('================\nDigite seu nome: ')

    if nome.lower() == 'fim':
        break

    notas = []
 
    for nota in range(3):
        nota = float(input('Digite uma nota: '))
        notas.append(nota)
    # fim do input de nome e nota

    boletim[nome] = notas

for aluno in boletim:
    media = sum(boletim[aluno]) / len(boletim[aluno])

    if media >= 7:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    print(f'----------------------------------\n{aluno}: média {round(media, 2)} - {situacao}')
