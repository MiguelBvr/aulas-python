precos = {'pocao': 10, 'espada': 50, 'escudo': 35}
lista_de_compras = ['pocao','espada','pocao']
total_comprado = 0

for item in lista_de_compras:
    total_comprado += precos[item]

print(total_comprado)
