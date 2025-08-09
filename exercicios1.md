## Parte 1: Exercícios Básicos

### 1. Declaração de Inteiro:
Crie uma variável chamada idade e atribua a ela a sua idade (como um número inteiro). Em seguida, imprima o valor da variável.

### 2. Declaração de Float:
Crie uma variável chamada altura e atribua a ela a sua altura (como um número com casas decimais, por exemplo, 1.75). Em seguida, imprima o valor da variável.

### 3. Declaração de String:
Crie uma variável chamada nome e atribua a ela o seu nome (como texto). Em seguida, imprima o valor da variável.

### 4. Verificando o Tipo (Função type()):
Use a função type() para descobrir e imprimir o tipo das variáveis idade, altura e nome que você criou nos exercícios anteriores. Exemplo: print(type(minha_variavel)).

### 5. Cálculo com Inteiros:
Crie duas variáveis, numero1 e numero2, e atribua a elas dois números inteiros diferentes. Calcule a soma desses dois números e guarde o resultado em uma nova variável chamada soma. Imprima o valor de soma.

### 6. Cálculo com Floats:
Crie duas variáveis, preco_produto e quantidade_comprada, e atribua a elas um preço com casas decimais (ex: 15.99) e uma quantidade inteira (ex: 3). Calcule o valor total da compra e guarde o resultado em valor_total. Imprima valor_total.

### 7. Concatenação de Strings:
Crie duas variáveis, saudacao com o valor 'Olá' e nome_usuario com o seu nome. Use o operador + para juntar (concatenar) as duas strings e criar uma frase completa, guardando-a em mensagem. Imprima mensagem.
___

## Parte 2: Exercícios Moderados

### 8. Conversão de Tipos (Int para Float):
Crie uma variável pontos com o valor inteiro 100. Converta pontos para um tipo float e guarde o resultado em pontos_flutuantes. Imprima pontos_flutuantes e seu tipo. (Dica: use float()).

### 9. Conversão de Tipos (Float para Int):
Crie uma variável temperatura com o valor 27.8. Converta temperatura para um tipo inteiro e guarde o resultado em temperatura_inteira. Imprima temperatura_inteira e seu tipo. O que acontece com a parte decimal? (Dica: use int()).

### 10. Conversão de Tipos (String para Int):
Crie uma variável idade_texto com o valor '25' (string). Converta idade_texto para um tipo inteiro e guarde o resultado em idade_numero. Imprima idade_numero e seu tipo. (Dica: use int()).

### 11. Conversão de Tipos (String para Float):
Crie uma variável nota_texto com o valor '8.5' (string). Converta nota_texto para um tipo float e guarde o resultado em nota_numero. Imprima nota_numero e seu tipo. (Dica: use float()).

### 12. Entrada de Usuário (Input):
Peça ao usuário para digitar o seu nome usando a função input(). Guarde o nome digitado em uma variável e imprima uma mensagem de boas-vindas usando esse nome. Exemplo: input("Qual é o seu nome? ").

### 13. Entrada de Usuário e Cálculo (Inteiros):
Peça ao usuário para digitar dois números inteiros. Some esses dois números e imprima o resultado. (Lembre-se que input() sempre retorna uma string, então você precisará converter para int!).

### 14. Entrada de Usuário e Cálculo (Floats):
Peça ao usuário para digitar o preço de um item e a quantidade comprada. Calcule o valor total (preço * quantidade) e imprima o resultado. (Você provavelmente precisará converter para float!).

### 15. Formatação de Strings (f-strings):
Crie variáveis para produto (string, ex: "Livro"), preco (float, ex: 35.50) e desconto (float, ex: 0.10 para 10%). Calcule o preço com desconto. Use uma f-string para imprimir uma frase formatada, como: "O Livro custa R$35.50 e, com 10% de desconto, fica por R$31.95."
___

## Parte 3: Desafios

### 16. Média de Notas:
Peça ao usuário para digitar três notas de um aluno (podem ser números com decimais). Calcule a média dessas notas e imprima o resultado formatado com duas casas decimais.

### 17. Cálculo de IMC (Índice de Massa Corporal):
Peça ao usuário para digitar seu peso (em kg) e sua altura (em metros). Calcule o IMC usando a fórmula: IMC = peso / (altura * altura). Imprima o IMC com duas casas decimais.

### 18. Número Invertido (String e Int):
Peça ao usuário para digitar um número inteiro de 3 dígitos (ex: 123). Converta esse número para string, inverta a string (pesquise como inverter strings em Python!), e depois converta a string invertida de volta para um inteiro. Imprima o número invertido. Ex: se digitar 123, deve imprimir 321.

### 19. Contagem de Caracteres e Palavras:
Peça ao usuário para digitar uma frase. Imprima:

- O número total de caracteres na frase (incluindo espaços).
- O número de palavras na frase (dica: use o método .split() de strings).

### 20. Operações Diversas:
Crie uma variável num_str com o valor '15'. Crie uma variável num_int com o valor 10. Crie uma variável num_float com o valor 5.5.
Realize as seguintes operações e imprima o resultado de cada uma, junto com o tipo do resultado:

- num_int + num_float
- int(num_str) * num_float
- num_int / int(num_str)
- str(num_int) + num_str
