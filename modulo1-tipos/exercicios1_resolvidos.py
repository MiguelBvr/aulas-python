idade = 14
print(idade)

altura = 1.95
print(altura)

nome = 'Miguel'
print(nome)

print(type(idade))
print(type(altura))
print(type(nome))

numero1 = 15
numero2 = 5
soma = numero1 + numero2
print(soma)

preco_produto = 15.99
quantidade_comprada = 3
valor_total = preco_produto * quantidade_comprada
print(valor_total)

saudacao = 'Olá'
nome_usuario = 'Miguel'
mensagem = saudacao + ' ' + nome_usuario
print(mensagem)

pontos = 100
pontos_flutuantes = float(pontos)
print(pontos_flutuantes, type(pontos_flutuantes))

# 9
temperatura = 27.8
temperatura_inteira = int(temperatura)
print(temperatura_inteira, type(temperatura_inteira))

# 10. Conversão de Tipos (String para Int):
# Crie uma variável idade_texto com o valor '25' (string). Converta idade_texto para um tipo inteiro e guarde o resultado em idade_numero. Imprima idade_numero e seu tipo. (Dica: use int()).
idade_texto = '25'
idade_numero = int(idade_texto)
print(idade_numero, type(idade_numero))

# 11. Conversão de Tipos (String para Float):
# Crie uma variável nota_texto com o valor '8.5' (string). Converta nota_texto para um tipo float e guarde o resultado em nota_numero. Imprima nota_numero e seu tipo. (Dica: use float()).
nota_texto = '8.5'
nota_numero = float(nota_texto)
print(nota_numero, type(nota_numero))

# 12. Entrada de Usuário (Input):
# Peça ao usuário para digitar o seu nome usando a função input(). Guarde o nome digitado em uma variável e imprima uma mensagem de boas-vindas usando esse nome. Exemplo: input("Qual é o seu nome? ").
nome = input('Qual é o seu nome? ')
print(nome, type(nome))

# 13. Entrada de Usuário e Cálculo (Inteiros):
# Peça ao usuário para digitar dois números inteiros. Some esses dois números e imprima o resultado. (Lembre-se que input() sempre retorna uma string, então você precisará converter para int!).
numero1_int = int(input('Digite um número inteiro '))
numero2_int = int(input('Digite um número inteiro '))
soma_int = numero1_int + numero2_int
print(soma_int, type(soma_int))

# 14. Entrada de Usuário e Cálculo (Floats):
# Peça ao usuário para digitar o preço de um item e a quantidade comprada. Calcule o valor total (preço * quantidade) e imprima o resultado. (Você provavelmente precisará converter para float!).
preço_item = float(input('Digite o preço de algum item. '))
quantidade_item = int(input('Quantos desse item você comprou? '))
valor_total_item = preço_item * quantidade_item
print(valor_total_item, type(valor_total_item))

# 15. Formatação de Strings (f-strings):
# Crie variáveis para produto (string, ex: "Livro"), preco (float, ex: 35.50) e desconto (float, ex: 0.10 para 10%). Calcule o preço com desconto. Use uma f-string para imprimir uma frase formatada, como: "O Livro custa R$35.50 e, com 10% de desconto, fica por R$31.95."
produto = 'Livro'
preco = 85.90
desconto = 0.35
preco_com_desconto = preco - (preco * desconto)
print(f'O {produto} custa R${preco} e, com {int(desconto * 100)}% de desconto, fica por R${preco_com_desconto}.')

# 16. Média de Notas:
# Peça ao usuário para digitar três notas de um aluno (podem ser números com decimais). Calcule a média dessas notas e imprima o resultado formatado com duas casas decimais.

nota1 = float(input('Digite a sua primeira nota ecolar '))
nota2 = float(input('Digite a sua segunda nota ecolar '))
nota3 = float(input('Digite a sua terceira nota ecolar '))
soma_nota = (nota1 + nota2 + nota3) / 3
print(f'A sua média escolar foi de {soma_nota}')

# 17
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura * altura)
print(round(imc, 2))

# 18
numero_int = int(input('Digite um número inteiro de 3 digitos: '))
numero_str = str(numero_int)
numero_invert = numero_str[::-1]
print(numero_invert)

# 19
frase = input('Digite uma frase qualquer. ')
caracteres = len(frase)
palavras = frase.split()
print(palavras)
total_palavras = len(palavras)
print(caracteres)
print(total_palavras)

# 20
num_str = '15'
num_int = 5
num_float = 5.5
soma1 = num_int + num_float
soma2 = int(num_str) * num_float
soma3 = num_int / int(num_str)
soma4 = str(num_int) + num_str
print(soma1)
print(type(soma1))
print(soma2)
print(type(soma2))
print(soma3)
print(type(soma3))
print(soma4)
print(type(soma4))
