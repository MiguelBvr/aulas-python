# Variáveis do menu e da lista
inventario = {} 
opcao = 0 


def add_nome_qtd(item, qtd_add, lista):
    if item not in lista:
        lista[item] = qtd_add 
        # Adciona uma string e o valor a ela

    else:
        return "Seu ítem já existe na lísta"


def remove_nome_qtd(item, qtd_remover, lista):
    if item in lista:

       if qtd_remover >= lista[item]:
           del lista[item]   # O objeto será removido da lista
           
       else:
           lista[item] -= qtd_remover
            # Só remove uma quantidade sem remover o objeto
    else:
        return "Seu ítem não foi encontrado na lista"
    

while opcao != 4:

    print("\n------ MENU -------")
    opcao = int(input("1. Adcionar Nome/Qtd à lista\n" \
                  "2. Remover Nome/Qtd à lista\n" \
                  "3. Ver a lista\n" \
                  "4. Sair\n" \
                  "Digite sua opção: "))

    if opcao == 1:

        adicionar_nome_lista = input("Digite o nome do item para adicionar ao inventário: ")
        adicionar_qtd_lista = int(input(f"Digite a quantidade de {adicionar_nome_lista}(s) você quer adicionar à lista: "))
        add_nome_qtd(adicionar_nome_lista, adicionar_qtd_lista, inventario)
        # Só usei o input para adicionar à função criada

    elif opcao == 2:

        remover_nome_lista = input("Digite o item que você quer remover: ")
        remover_qtd_lista = int(input(f"Digite a quantidade de {remover_nome_lista}(s) que você quer remover: "))
        remove_nome_qtd(remover_nome_lista, remover_qtd_lista, inventario)
        

    elif opcao == 3:
        print(inventario)

    elif opcao > 4:
        print("opção inválida, tente novamente.")
        
