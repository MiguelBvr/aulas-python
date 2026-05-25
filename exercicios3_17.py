maior_numero = -1

lista_numeros = []

for numero in range(5):

    numeros = int(input(f'Escreva o {numero + 1}º numero: '))

    lista_numeros.append(numeros)

    if numeros > maior_numero:
        maior_numero = numeros

print(f'O maior número dentre os digitados é {maior_numero}')
