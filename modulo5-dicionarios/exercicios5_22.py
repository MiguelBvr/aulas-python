inventario = {'pocao': 3, 'flecha': 0, 'mapa': 1, 'chave': 0}
maior_que_zero = []

for item in inventario:
    if inventario[item] > 0:
        maior_que_zero.append(item)

print(maior_que_zero)
