numero_inicial = int(input('Escreva um número para gerar a tabuada do mesmo: '))

numero_final = 0

for numero in range(1, 11):

    numero_final = numero_inicial * numero

    print(f'{numero_inicial} x {numero} é igual a {numero_final} ')
