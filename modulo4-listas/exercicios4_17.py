notas = [1.5, 4.8, 8, 7.3, 9.4, 2.4]
notas_altas = 0

for nota in notas:
    if nota > 7:
        notas_altas += 1

print(notas_altas)
