# 28.
frase = input('Escreva uma frase: ')

vogais = 0
consoantes = 0
espaços = 0

for letra in frase:

    if letra.lower() in 'aeiou':
        vogais = vogais + 1

    elif letra == ' ':
        espaços = espaços + 1        
    
    elif letra.isalpha():
        consoantes = consoantes + 1

print(f'Sua frase tem {vogais} vogais, {consoantes} consoantes e {espaços} espaços')
