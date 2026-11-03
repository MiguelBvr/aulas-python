notas = {'Ana': 8.5, 'Beto': 6.0, 'Cris': 9.0, 'Davi': 5.5}
soma_total = 0

for nota in notas:
    soma_total += notas[nota]

media = soma_total / len(notas)

print(media)