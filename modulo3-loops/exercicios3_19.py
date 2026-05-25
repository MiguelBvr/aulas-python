numero_fatorial = int(input('Escreva um número que você queira saber o fatorial: '))

resultado = 1

for numero in range(1, numero_fatorial + 1):

    resultado = resultado * numero 

print(f'O resultado de {numero_fatorial}! é igual a {resultado}.')
