# 1.
# print(10 > 5)
# O resultado será "True"

# 2.
# print(3 == 3)
# O resultado será "True"

# 3.
# print(12 < 8)
# O resultado será "False"

# 4.
# print('hello' != 'world')
# Retorna "True"

# 5.
# print('Python' == 'python')
# O resultado é "False"

# 6.
# print(True and True)
# Retorna True

# 7.
# print(True and False)
# Retorna False

# 8.
# print(False and False)
# Retorna False

# 9.
# print(False or False)
# Resultado False

# 10.
# print(not True)
# É False

# 11.
# print(not (5 > 10))
# Retorna True (Porque nega que 5 é maior que 10)

# 12.
# print((10 >= 10) and (5 < 5))
# False (pois uma das afirmativas está errada)

# 13.
# Vai ser True e True

# 14.
# Vai ser True

# 15.
# Vai dar False (porque "a" não é igual a "A" e 10 é igual a 10 também)

# 16.
# False

# 17.
# True

# 18.
# False

# 19.
chove = True
vento = False
print(chove == True and vento == False)
# Resultado é True

# 20.
num = 20
print(num > 10 and num % 2 == 0)
# Resultado = True


# 21.
idade = 17
print(idade > 13 and idade < 19)
# Resultado = True

# 22.
produto = 'leite'
estoque = 5
print(produto == 'leite' and estoque > 0)
# Resultado = True

# 23.
print(not ('banana' in 'morango'))
# O resultado é True, não sei o porquê

# 24.
a = 5
b = 10
print(not (a > b) and (a != b))
# Resultado = True

# 25.
nota_final = 75
frequencia = 80
frequencia_total = 100
porcentagem_frequencia = frequencia / frequencia_total
print(nota_final >= 70 and porcentagem_frequencia >= 0.75)

# 26.
print(True and False)
print(True and not False)
# A primeira é False e a segunda é True

# 27.
valor_compra = 95
cliente_vip = True
frete_gratis = valor_compra > 100 or cliente_vip == True
print(frete_gratis)
# O resultado dá True por causa do VIP

# 28.
print(not (10 > 5 and 20 != 20) or (5 == 5))
# o resultado da True porque pelo menos umas das afirmações está correta

# 29.
ano = 2000
ano_bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
print(ano_bissexto)
# O resultado é = True porque uma das condicionais está sendo cumprida

# 30.
idade = 18
print(idade > 13 and idade < 17 or idade == 18 or idade == 65)
# O resultado vai ser True pois a segunda condicional está sendo cumprida
