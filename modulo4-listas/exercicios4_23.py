numeros = ['42', '17', '89', '5', '73', '21', '94', '38', '66', '11']
numeros_int = []

for n in numeros:
    n = int(n)
    numeros_int.append(n)

media = sum(numeros_int) / len(numeros_int)
print(media)
