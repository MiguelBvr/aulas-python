palavra = 'geladeira'
contador = {}

for letra in palavra:
    if letra in contador:
        contador[letra] += 1
    
    else:
        contador[letra] = 1

print(contador)