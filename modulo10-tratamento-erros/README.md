# Módulo 10 — Tratamento de Erros

## 1. Introdução Teórica e Prática

Você já deve ter visto aquela mensagem vermelha cheia de letrinhas quando algo dá errado no código. Em Python, isso se chama **exceção**. Sem tratamento, o programa **trava na hora**, como um jogo que fecha sozinho no meio da partida. Com o tratamento de erros, você coloca uma **rede de proteção**: se algo der errado, o programa avisa o jogador e continua.

Por que isso é útil?
- Evita que o programa quebre quando o usuário digita algo inesperado (`abc` onde era um número).
- Lida com situações fora do seu controle: arquivo que não existe, divisão por zero, item que não está no inventário.
- Deixa as mensagens de erro claras e amigáveis.
- Combina com tudo o que você já viu: loops, `if`, listas, dicionários, funções, strings, conjuntos e arquivos.

### O erro acontecendo

```python
idade = int('abc')   # ValueError: não dá para transformar 'abc' em número
```

### try / except: a rede de proteção

```python
# o Python tenta rodar o bloco 'try'; se der erro, pula para o 'except'
try:
    idade = int(input('Quantos anos você tem? '))
    print('Ano que vem você terá', idade + 1)
except ValueError:
    print('Digite apenas números!')

print('O programa continua rodando!')
```

### Erros mais comuns

| Erro | Quando acontece |
|------|-----------------|
| `ValueError` | valor com formato errado: `int('abc')` |
| `ZeroDivisionError` | divisão por zero: `10 / 0` |
| `IndexError` | posição que não existe na lista: `lista[99]` |
| `KeyError` | chave que não existe no dicionário: `dic['x']` |
| `TypeError` | tipos incompatíveis: `'2' + 3` |
| `FileNotFoundError` | arquivo que não existe: `open('nada.txt')` |

### Vários except e o objeto do erro

```python
try:
    resultado = 10 / int(input('Dividir 10 por: '))
    print(resultado)
except ValueError:
    print('Isso não é um número inteiro.')
except ZeroDivisionError:
    print('Não dá para dividir por zero!')
except (IndexError, KeyError):   # vários tipos no mesmo bloco, em uma tupla
    print('Item não encontrado.')

# 'as erro' guarda a mensagem original do Python
try:
    numero = int('abc')
except ValueError as erro:
    print('Deu ruim:', erro)
    print('Tipo do erro:', type(erro).__name__)   # ValueError
```

### else e finally

```python
try:
    numero = int(input('Número: '))
except ValueError:
    print('Valor inválido.')
else:
    # só roda se NÃO houve erro no try
    print('Você digitou', numero)
finally:
    # roda SEMPRE, com erro ou sem erro (ótimo para "arrumar a casa")
    print('Fim da tentativa.')
```

### Repetindo até dar certo

```python
# o padrão mais usado: while True + try
while True:
    try:
        idade = int(input('Idade: '))
        break              # deu certo, sai do loop
    except ValueError:
        print('Tente de novo, só números.')
```

### Criando o seu próprio erro com raise

```python
def sacar(saldo, valor):
    if valor > saldo:
        # você levanta o erro quando a regra do seu programa é quebrada
        raise ValueError('Saldo insuficiente!')
    return saldo - valor

try:
    novo_saldo = sacar(50, 80)
except ValueError as erro:
    print('Erro:', erro)   # Erro: Saldo insuficiente!
```

### Arquivos que não existem

```python
try:
    with open('save.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print('Nenhum save encontrado, começando jogo novo.')
```

Dica: coloque no `try` **só o trecho que pode dar erro** e use o tipo de erro mais específico possível. Evite `except:` solto, porque ele esconde bugs de verdade.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas, Dicionários, Funções, Strings, Tuplas e Conjuntos, e Arquivos. Quando o enunciado falar de um arquivo de entrada, crie-o manualmente com o conteúdo indicado.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Execute `int('abc')` sem tratamento, observe a mensagem de erro e escreva em um comentário o nome do erro.
2. Leia um número com `input()` dentro de um `try` e mostre `Digite apenas números!` se der `ValueError`.
3. Divida `10` por um número digitado e trate o `ZeroDivisionError`.
4. Tente acessar a posição `10` de uma lista de 3 itens e trate o `IndexError`.
5. Tente acessar uma chave que não existe em um dicionário e trate o `KeyError`. Depois mostre como o `.get()` evitaria o erro.
6. Tente abrir `fantasma.txt` para leitura e trate o `FileNotFoundError`.
7. Use `except ValueError as erro` para mostrar a mensagem original do Python.
8. Escreva um `try` com dois `except`: um para `ValueError` e outro para `ZeroDivisionError`.
9. Trate `ValueError` e `TypeError` juntos em um único `except`, usando uma tupla.
10. Use o bloco `else` para mostrar `Deu tudo certo!` somente quando nenhum erro acontecer.
11. Use o bloco `finally` para mostrar `Fim!` com e sem erro.
12. Provoque um `TypeError` somando `'2' + 3` e trate-o.
13. Use `raise ValueError('Mensagem')` dentro de um `if` e capture o erro com `try`/`except`.
14. Crie uma função `dividir(a, b)` que devolve `None` quando `b` for zero, usando `try`/`except`.
15. Dada a lista de operações `['int("x")', '10 / 0', '[1][5]', '{}["a"]']`, execute cada uma em `eval()` dentro de um `try` e mostre o nome do erro com `type(erro).__name__`.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use tratamento de erros junto com `for`/`while`, `if`/`else`, listas, dicionários, funções, strings, tuplas, conjuntos e arquivos.

16. (Calculadora segura) Leia dois números e uma operação (`+`, `-`, `*`, `/`). Se o usuário digitar algo inválido, avise e peça de novo (loop). Trate também a divisão por zero.
17. (Idade válida) Crie `ler_inteiro(mensagem, minimo, maximo)` que repete a pergunta até o usuário digitar um inteiro dentro do intervalo. Se o valor estiver fora, use `raise ValueError` com uma mensagem clara e trate-a.
18. (Notas bagunçadas) Dada a lista `['8.5', 'abc', '7', '', '9,5']`, converta cada item para `float` com `try`/`except`. Mostre a média das notas válidas e a lista dos itens que não puderam ser convertidos.
19. (Pedidos da loja) Dado `precos = {'pocao': 10, 'espada': 50}` e a lista de pedidos `['pocao', 'escudo', 'espada']`, calcule o total. Itens que não existem na loja devem ser avisados (trate o `KeyError`) e ignorados.
20. (Leitor de arquivo) Crie `ler_linhas(nome_arquivo)` que devolve a lista de linhas do arquivo. Se ele não existir, avise e devolva uma lista vazia.
21. (Mochila) Dada uma lista `mochila` com 4 itens, leia um índice digitado e mostre o item. Trate índice que não é número, índice fora da lista e também recuse índices negativos com `raise IndexError`.
22. (Senha com motivos) Crie `validar_senha(senha)` que levanta `ValueError` com uma mensagem específica para cada regra quebrada: menos de 8 caracteres, sem número, sem letra maiúscula. Teste com uma lista de senhas e mostre o motivo de cada recusa.
23. (Conversor de moeda) Dado `taxas = {'USD': 5.0, 'EUR': 5.5}`, leia um valor em reais e o código da moeda. Valor não numérico ou negativo (`raise ValueError`) e moeda inexistente (`KeyError`) devem mostrar mensagens diferentes.
24. (CSV com linhas ruins) O arquivo `notas.csv` tem este conteúdo:
    ```
    Ana,8
    Beto,abc
    Cris
    Davi,6.5
    ```
    Monte um dicionário `{nome: nota}` com as linhas válidas e conte as linhas que precisaram ser ignoradas (trate `IndexError` e `ValueError`).
25. (Rodadas com finally) Faça 3 rodadas de um jogo. Em cada uma, peça um número de 1 a 5; se for inválido, avise. Independente do resultado, use `finally` para mostrar `Fim da rodada N`.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários, funções, strings, tuplas, conjuntos, arquivos e tratamento de erros. O Input e o Output esperados estão descritos.

26. (Calculadora Robusta) O programa lê expressões no formato `número operador número` até `FIM`. Os operadores aceitos são `+`, `-`, `*` e `/`. Nenhuma entrada errada pode travar o programa. No final, mostre quantas contas deram certo e quantos erros aconteceram.
    Input:
    ```
    10 + 5
    8 / 0
    7 x 2
    abc * 3
    4 *
    FIM
    ```
    Output:
    ```
    10 + 5 = 15.0
    Erro: divisão por zero
    Erro: operador 'x' desconhecido
    Erro: 'abc' não é um número
    Erro: formato inválido (use: número operador número)
    Resumo: 1 conta(s) certa(s), 4 erro(s)
    ```

27. (Banco Seguro) As contas começam como `{'Ana': 100, 'Beto': 50}`. O programa lê comandos até `FIM`: `SALDO nome`, `SACAR nome valor` e `DEPOSITAR nome valor`. Trate conta inexistente, valor que não é número, valor negativo ou zero e saldo insuficiente, cada um com uma mensagem própria. Use funções que levantam erros com `raise`.
    Input:
    ```
    SALDO Ana
    SACAR Ana 30
    SACAR Beto 80
    DEPOSITAR Cris 10
    DEPOSITAR Ana abc
    DEPOSITAR Ana -5
    SALDO Ana
    FIM
    ```
    Output:
    ```
    Saldo de Ana: 100.00
    Saque realizado. Novo saldo de Ana: 70.00
    Erro: saldo insuficiente (disponível: 50.00)
    Erro: conta 'Cris' não existe
    Erro: valor inválido
    Erro: o valor deve ser positivo
    Saldo de Ana: 70.00
    ```

28. (Carregador de Save Tolerante) Crie `carregar_jogo(nome_arquivo)`, que lê um arquivo de save com linhas `chave=valor` e devolve um dicionário. Os valores padrão são `{'nome': 'Jogador', 'nivel': 1, 'vida': 100, 'ouro': 0}`. Se o arquivo não existir, devolva os padrões. Se uma linha não tiver `=`, ignore-a com um aviso. Se um valor numérico for inválido, use o padrão e avise. `nome` é texto; `nivel`, `vida` e `ouro` são inteiros.
    Input (primeira execução, `save.txt` com este conteúdo):
    ```
    nome=Miguel
    nivel=cinco
    vida=80
    ouro
    ```
    Output:
    ```
    Aviso: valor inválido para 'nivel' (usando padrão 1)
    Aviso: linha inválida ignorada: ouro
    Jogo carregado: Miguel, nível 1, vida 80, ouro 0
    ```
    Input (segunda execução, sem o arquivo `save.txt`):
    ```
    (nenhum arquivo)
    ```
    Output:
    ```
    Arquivo save.txt não encontrado. Começando jogo novo.
    Jogo carregado: Jogador, nível 1, vida 100, ouro 0
    ```

29. (Quiz à Prova de Erros) Monte uma lista de tuplas `(pergunta, opcoes, indice_correto)` com 3 perguntas, cada uma com 3 opções numeradas de 1 a 3. Para cada pergunta, repita a leitura da resposta até receber um número válido (texto que não é número e número fora de 1 a 3 não gastam a pergunta). No final, mostre a pontuação e grave em `placar.txt`, tratando um possível erro ao gravar o arquivo. As perguntas e as opções também aparecem na tela, mas abaixo só estão as mensagens de feedback.
    Perguntas:
    ```
    1. Qual a capital do Brasil? (1-Rio, 2-Brasília, 3-São Paulo)  -> certa: 2
    2. Quanto é 2 + 2?          (1-3, 2-4, 3-5)                    -> certa: 2
    3. Que linguagem estamos aprendendo? (1-Java, 2-C, 3-Python)   -> certa: 3
    ```
    Input (respostas digitadas):
    ```
    2
    abc
    4
    2
    1
    ```
    Output:
    ```
    Correto!
    Digite apenas números.
    Escolha entre 1 e 3.
    Correto!
    Errado! A resposta era 3 - Python
    Pontuação: 2/3
    Placar salvo em placar.txt
    ```

30. (Mini-projeto: Gerenciador de Notas à Prova de Erros) Ao iniciar, carregue o arquivo `alunos.csv` (linhas `nome,nota`) em um dicionário. Se o arquivo não existir, comece vazio e avise. O programa lê comandos até `SAIR`: `ADICIONAR nome nota` (a nota deve ser um número entre 0 e 10 e o nome não pode já existir), `REMOVER nome`, `MEDIA` e `SALVAR` (grava o arquivo de volta). Comandos desconhecidos também devem ser tratados. Organize o código em funções que levantam erros com `raise`.
    Arquivo `alunos.csv` inicial:
    ```
    Ana,8.5
    Beto,6
    ```
    Input:
    ```
    ADICIONAR Cris 9
    ADICIONAR Davi onze
    ADICIONAR Eva 11
    ADICIONAR Ana 7
    REMOVER Zeca
    MEDIA
    SALVAR
    COMANDO_X
    SAIR
    ```
    Output:
    ```
    Nota registrada: Cris = 9.0
    Erro: 'onze' não é uma nota válida
    Erro: a nota deve estar entre 0 e 10
    Erro: Ana já existe
    Erro: Zeca não encontrado
    Média da turma: 7.8
    alunos.csv salvo (3 alunos)
    Erro: comando desconhecido
    Encerrando.
    ```
