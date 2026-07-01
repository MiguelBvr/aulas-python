itens = [{'Miguel':'pocao','qtd':3},{'Rafael':'espada','qtd':1}]

total_itens = 0

for item in itens:
    if 'qtd' in item:
        total_itens += item['qtd']

print(total_itens)
