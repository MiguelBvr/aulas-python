# No Python podemos escrever nomes de variáveis iniciados com letra ou "_".
# Números podem ser usados no nome da variável desde que não estejam no início.

# 1numero = 12 SyntaxError: invalid decimal literal
_numero_1 = 12
print(_numero_1)

# No Python temos 4 tipos de dados: str, int, float, bool
print(0.1 + 0.2)

# String
print('ada' + ' ' + 'lovelace')
print('lista\n 1 - carro\n2 - casa')

# Após o uso do operador especial para a quebra de linha dentro da string,
# caso haja um espaço, esse espaço será refletido na string/print.

nome = 'ada' + ' ' + 'lovelace'
print(nome.title())
print(nome.capitalize())
print(nome.upper())
print("AdA LoVeLaCe".lower())
