def busca_item(lista, item_procurado):
    for psc in range(len(lista)):

        if lista[psc] == item_procurado:

            return psc

    return -1

item_procurado = input('Digite o item que deseja achar a posição: ')

meu_inventario = ['poção', 'escudo', 'espada', 'mapa']

item_achado = busca_item(meu_inventario, item_procurado)

if item_achado != -1:
    print(f'Seu item está na posição {item_achado}')

else:
    print('Sei item não está no inventário')
    
