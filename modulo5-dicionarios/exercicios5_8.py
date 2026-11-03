personagem = {
    'nome' : 'Miguel',
    'mana' : 50,
    'defesa' : 35,
    'dinheiro' : 150,
    'arma' : 'glock'
}

if 'defesa' not in personagem:
    print(0)

else:
    print(personagem.get('defesa'))


