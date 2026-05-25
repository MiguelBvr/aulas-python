# Exercícios 3 - Loops (Laços de Repetição)

## O que são Loops?

Um **loop** (ou laço) é como fazer a mesma coisa várias vezes seguidas. Imagine que você precisa escrever seu nome 10 vezes - em vez de escrever um por um, você pode usar um loop para fazer isso automaticamente!

## Loop FOR - "Para cada item, faça isso"

O loop `for` é usado quando você sabe **quantas vezes** quer repetir algo.

```python
# Exemplo básico: contar de 1 a 5
for numero in range(1, 6):
    print(f"Contando: {numero}")
```

### Como funciona o range():
- `range(5)` = números de 0 a 4 (5 números no total)
- `range(1, 6)` = números de 1 a 5
- `range(0, 10, 2)` = números de 0 a 8, pulando de 2 em 2 (0, 2, 4, 6, 8)

## Loop WHILE - "Enquanto isso for verdade, continue fazendo"

O loop `while` é usado quando você **não sabe exatamente** quantas vezes vai repetir, mas sabe a condição para parar.

```python
# Exemplo: contar até chegar em 5
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador = contador + 1  # MUITO IMPORTANTE: sempre mude a variável!
```

⚠️ **CUIDADO**: Se você esquecer de mudar a variável no `while`, o programa vai rodar para sempre!

---

## EXERCÍCIOS FÁCEIS (1-15)

### 1. Primeiros Passos
Crie um programa que imprime os números de 1 a 10 usando um loop `for`.

### 2. Contagem Regressiva
Faça uma contagem regressiva de 10 até 1 usando um loop `for`.

### 3. Tabuada do 2
Crie um programa que mostra a tabuada do 2 (2x1, 2x2, 2x3... até 2x10).

### 4. Seu Nome 5 Vezes
Use um loop `for` para imprimir seu nome 5 vezes.

### 5. Números Pares
Imprima todos os números pares de 0 a 20 usando um loop `for`.

### 6. Números Ímpares
Imprima todos os números ímpares de 1 a 19 usando um loop `for`.

### 7. Soma Simples
Use um loop `for` para somar todos os números de 1 a 10 e mostre o resultado.

### 8. Contador com While
Use um loop `while` para contar de 1 a 5.

### 9. Dobro dos Números
Para cada número de 1 a 5, imprima o número e seu dobro.

### 10. Contando de 3 em 3
Conte de 3 a 30, pulando de 3 em 3 (3, 6, 9, 12...).

### 11. Asteriscos
Imprima 8 asteriscos (*) em linha, um por vez, usando um loop.

### 12. Quadrados
Para cada número de 1 a 5, imprima o número e seu quadrado (número × número).

### 13. Palavras Repetidas
Peça ao usuário uma palavra e um número, depois imprima a palavra esse número de vezes.

### 14. Contagem Até o Usuário Decidir
Use `while` para contar de 1 até um número que o usuário escolher.

### 15. Múltiplos de 5
Imprima todos os múltiplos de 5 entre 0 e 50.

---

## EXERCÍCIOS MÉDIOS (16-25)

### 16. Calculadora de Média
Peça 5 notas ao usuário (usando um loop) e calcule a média.

### 17. Maior Número
Peça ao usuário 5 números e encontre qual é o maior.

### 18. Contador de Positivos
Peça 10 números ao usuário e conte quantos são positivos (maiores que 0).

### 19. Fatorial
Calcule o fatorial de um número (exemplo: 5! = 5×4×3×2×1 = 120).

### 20. Pirâmide de Asteriscos
Crie uma pirâmide como esta:
```
*
**
***
****
*****
```

### 21. Tabuada Completa
Peça um número ao usuário e mostre sua tabuada completa (de 1 a 10).

### 22. Números Primos
Encontre todos os números primos entre 1 e 30.

### 23. Jogo de Adivinhação
O computador "pensa" em um número de 1 a 10. O usuário tem que adivinhar. Use `while` para continuar até acertar.

### 24. Sequência Fibonacci
Gere os primeiros 10 números da sequência Fibonacci (1, 1, 2, 3, 5, 8, 13...).

### 25. Validação de Entrada
Peça ao usuário um número entre 1 e 100. Use `while` para continuar pedindo até ele digitar um número válido.

---

## EXERCÍCIOS DIFÍCEIS (26-30)

### 26. Menu Interativo
Crie um menu que mostra opções e só para quando o usuário escolher "sair":
```
1. Calculadora
2. Conversor de temperatura
3. Sair
Escolha uma opção:
```

### 27. Jogo da Velha - Tabuleiro
Crie um tabuleiro 3x3 usando loops aninhados (um loop dentro do outro).

### 28. Análise de Texto
Peça uma frase ao usuário e conte:
- Quantas vogais tem
- Quantas consoantes tem
- Quantos espaços tem

### 29. Calculadora Avançada
Crie uma calculadora que:
- Mostra um menu de operações
- Realiza a operação escolhida
- Pergunta se quer fazer outro cálculo
- Só para quando o usuário escolher "não"

### 30. Padrão de Números
Crie este padrão usando loops:
```
1
12
123
1234
12345
```

---

## PROJETO FINAL: Sistema de Notas da Turma

Crie um programa completo que:

### Funcionalidades:
1. **Cadastro de Alunos**: Permita adicionar o nome e 4 notas de cada aluno
2. **Cálculo de Médias**: Calcule automaticamente a média de cada aluno
3. **Situação do Aluno**: Mostre se está aprovado (média ≥ 7), recuperação (5 ≤ média < 7) ou reprovado (média < 5)
4. **Relatório da Turma**: Mostre estatísticas gerais:
   - Quantos alunos estão aprovados
   - Quantos estão em recuperação
   - Quantos estão reprovados
   - Média geral da turma
   - Maior e menor nota individual

### Requisitos Técnicos:
- Use loops `for` para processar listas de alunos
- Use loops `while` para menus e validações
- Use condicionais para determinar a situação dos alunos
- Organize o código com funções (se já souber)
- Trate entradas inválidas do usuário

### Menu Principal:
```
=== SISTEMA DE NOTAS ===
1. Adicionar aluno
2. Ver todos os alunos
3. Relatório da turma
4. Sair
Escolha uma opção:
```

### Exemplo de Saída:
```
=== ALUNOS CADASTRADOS ===
João Silva - Notas: [8.5, 7.0, 9.0, 8.0] - Média: 8.1 - APROVADO
Maria Santos - Notas: [6.0, 5.5, 7.0, 6.5] - Média: 6.3 - RECUPERAÇÃO
Pedro Costa - Notas: [4.0, 5.0, 3.5, 4.5] - Média: 4.3 - REPROVADO

=== RELATÓRIO DA TURMA ===
Total de alunos: 3
Aprovados: 1 (33.3%)
Recuperação: 1 (33.3%)
Reprovados: 1 (33.3%)
Média da turma: 6.2
Maior nota individual: 9.0
Menor nota individual: 3.5
```

---

## Dicas para Resolver os Exercícios

### 🎯 **Estratégia Geral**
1. **Leia o exercício 2 vezes** antes de começar
2. **Pense no passo a passo** antes de escrever código
3. **Teste com números pequenos** primeiro
4. **Use nomes de variáveis claros** (contador, numero, soma...)

### 🔧 **Dicas Técnicas**
- **Para somar números**: sempre comece a variável soma com 0
- **Para encontrar o maior**: comece com o primeiro número da lista
- **Para loops infinitos**: sempre verifique se a condição do `while` vai mudar
- **Para entrada do usuário**: sempre converta `input()` para `int()` quando necessário

### 🐛 **Debugging (Encontrar Erros)**
- **Use `print()` para ver** o que está acontecendo dentro do loop
- **Conte quantas vezes** o loop está rodando
- **Verifique se as variáveis** estão mudando como esperado

### 📚 **Conceitos Importantes**
- **Range**: `range(start, stop, step)`
- **Variável acumuladora**: guarda um resultado que cresce a cada volta do loop
- **Variável contador**: conta quantas vezes algo aconteceu
- **Condição de parada**: o que faz o `while` parar de rodar

**Boa sorte com os exercícios! Lembre-se: a prática leva à perfeição! 🚀**
