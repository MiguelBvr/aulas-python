notas = []

nota = str(input("Digite a primeira nota: (enter para parar) "))

while nota != "":
    nota = float(nota)
    notas.append(nota)

    nota = str(input("Digite mais uma nota: "))

total = sum(notas)
media = total / len(notas)
# Média feita


maior_nota = notas[0]

for n in notas:
    if n > maior_nota:
        maior_nota = n
# Maior número feito

menor_nota = notas[0]

for n in notas:
    if n < menor_nota:
        menor_nota = n
# Menor número feito

abaixo_media = []

for n in notas:
    if n < media:
        abaixo_media.append(n)

qtd_abaixo_media = len(abaixo_media)

print(f"A média de notas foi de {media}. A maior nota foi: {maior_nota}, "
      f"a menor foi {menor_nota}. {qtd_abaixo_media} notas ficaram abaixo da média.")

