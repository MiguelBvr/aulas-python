# 18 
# itere sobre cada um dos valores da lista, converta esse valor para inteiro. Verifique se ele é maior que 0, caso seja conte ele, após a iteração retorne a quantidade de numeros contados. 
numeros = input('Digite 10 numeros aleatorios ')
numeros = numeros.split()
for numero in numeros:
    numero = int(numero)

    if numero < 0:
        numero = 0
    else:
        numero = numero
print(len(numeros))
