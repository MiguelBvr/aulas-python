contatos = {
    'Ana': '3190000-0001',
    'Bruno': '3190000-0002',
    'Carlos': '3190000-0003',
    'Daniela': '3190000-0004',
    'Eduardo': '3190000-0005',
    'Fernanda': '3190000-0006',
    'Gabriel': '3190000-0007',
    'Isabela': '3190000-0008',
    'João': '3190000-0009',
    'Mariana': '3190000-0010'
}

busca_contato = input('Digite o nome da pessoa que deseja buscar o contato: ')

for contato in contatos:
    if busca_contato == contato:
        print(f'O contato de {contato} é {contatos[contato]} ')
        break

else:
    print('Esse contato não existe')