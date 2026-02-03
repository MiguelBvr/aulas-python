notas = input('Escreva 5 notas para fazer uma média: ')

notas_texto = notas.split()

soma = 0

for n in notas_texto:
    soma = soma + float(n)

    quantidade_notas = len(notas_texto)

    media = soma / quantidade_notas

print(f'A média dessas notas é de {media} pontos')
