anterior = 1
atual = 1

for n in range(1, 10):

    print(anterior)
    anterior, atual = atual, atual + anterior

