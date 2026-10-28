# Módulo 5 — Dicionários

## 1. Introdução Teórica e Prática

Dicionário é uma coleção de pares **chave → valor**. Pense na ficha de um personagem de RPG: em vez de procurar "o terceiro item da lista", você pergunta direto pelo nome da informação — `"vida"`, `"mana"`, `"nivel"`. Também funciona como a agenda de contatos do celular: você busca pelo **nome** (chave) e encontra o **telefone** (valor).

Por que isso é útil?
- Guardar informações que descrevem uma coisa só (um aluno, um jogador, um filme).
- Buscar dados pelo nome da informação, sem precisar lembrar a posição (índice) como nas listas.
- Contar coisas (quantas vezes cada letra aparece, quantos votos cada opção teve).
- Combinar com listas, loops e condicionais para organizar dados mais complexos.

### Criando e acessando

```python
# cada item é "chave: valor" — a chave é a etiqueta, o valor é o conteúdo
jogador = {
    'nome': 'Miguel',
    'nivel': 12,
    'vida': 85.5,
    'online': True
}

# acessar pelo nome da chave (não pela posição!)
print(jogador['nome'])  # Miguel

# .get() não quebra o programa se a chave não existir
print(jogador.get('mana', 0))  # 0 (valor padrão)
```

### Adicionando, alterando e removendo

```python
# chave nova -> adiciona
jogador['classe'] = 'Mago'

# chave existente -> altera o valor
jogador['nivel'] = 13

# remove uma chave e devolve o valor dela
removido = jogador.pop('online')

# apaga usando del
del jogador['classe']
```

### Verificando se uma chave existe

```python
# "in" olha as CHAVES (não os valores)
if 'vida' in jogador:
    print('O jogador tem vida registrada!')
```

### Percorrendo com for

```python
# percorrendo só as chaves
for chave in jogador:
    print(chave)

# percorrendo chave e valor juntos
for chave, valor in jogador.items():
    print(chave, '->', valor)

# só os valores
for valor in jogador.values():
    print(valor)
```

### Dicionário como contador

```python
frase = 'banana'
contagem = {}

for letra in frase:
    if letra in contagem:
        contagem[letra] += 1   # já vimos essa letra, soma 1
    else:
        contagem[letra] = 1    # primeira vez que aparece

print(contagem)  # {'b': 1, 'a': 3, 'n': 2}
```

### Dicionários dentro de listas

```python
# cada dicionário é um "cartão" de um aluno; a lista guarda todos os cartões
turma = [
    {'nome': 'Ana', 'nota': 8.5},
    {'nome': 'Beto', 'nota': 6.0}
]

for aluno in turma:
    if aluno['nota'] >= 7:
        print(aluno['nome'], 'passou!')
```

Dica: as chaves precisam ser únicas. Se você repetir uma chave, o último valor vence.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops e Listas.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Crie um dicionário `filme` com as chaves `titulo`, `ano` e `nota` e imprima-o.
2. Mostre apenas o valor da chave `titulo` do dicionário `filme`.
3. Adicione a chave `genero` ao dicionário `filme`.
4. Altere o valor da chave `nota` do dicionário `filme`.
5. Remova a chave `ano` do dicionário `filme` usando `del`.
6. Use `len()` para mostrar quantos pares existem em um dicionário `personagem`.
7. Verifique se a chave `'mana'` existe em `personagem` (use `in`).
8. Use `.get()` para buscar a chave `'defesa'` em `personagem` e mostre `0` caso ela não exista.
9. Mostre todas as chaves de `personagem` usando `.keys()`.
10. Mostre todos os valores de `personagem` usando `.values()`.
11. Use `.items()` para imprimir cada par no formato `chave: valor`.
12. Use `.pop()` para remover a chave `'nivel'` e guarde o valor removido em uma variável.
13. Junte dois dicionários, `a` e `b`, em um só usando `.update()`.
14. Limpe todos os itens de um dicionário `mochila` com `.clear()`.
15. Crie um dicionário a partir de duas listas, `chaves` e `valores`, usando um loop `for` com `range()` e `len()`.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use `for`/`while`, `if`/`else`, listas e os tipos de dados adequados junto com dicionários.

16. (Contador de letras) Receba uma palavra e mostre quantas vezes cada letra aparece.
17. (Votação do grêmio) Dada a lista `votos = ['Ana','Beto','Ana','Cris','Beto','Ana']`, conte os votos de cada candidato e mostre quem venceu.
18. (Agenda) Crie um dicionário de contatos (`nome: telefone`). Peça um nome ao usuário: se existir, mostre o telefone; senão, mostre `'Contato não encontrado'`.
19. (Notas da escola) Dado o dicionário `notas = {'Ana': 8.5, 'Beto': 6.0, 'Cris': 9.0, 'Davi': 5.5}`, mostre apenas os alunos aprovados (nota >= 7.0).
20. (Média da turma) Com o mesmo dicionário do exercício anterior, calcule a média das notas e mostre quem está acima dela.
21. (Loja do RPG) Dado `precos = {'pocao': 10, 'espada': 50, 'escudo': 35}` e uma lista de compras `['pocao','espada','pocao']`, calcule o total. Se um item não existir na loja, avise o jogador.
22. (Inventário) Dado `inventario = {'pocao': 3, 'flecha': 0, 'mapa': 1, 'chave': 0}`, crie uma nova lista só com os itens cuja quantidade é maior que zero.
23. (Palavras repetidas) Receba uma frase, separe as palavras com `.split()` e mostre quais palavras aparecem mais de uma vez.
24. (Troca de chave e valor) Dado um dicionário em que os valores não se repetem, crie outro com chaves e valores invertidos usando um loop.
25. (Lista de dicionários) Dada a lista `alunos = [{'nome':'Ana','idade':15},{'nome':'Beto','idade':17},{'nome':'Cris','idade':16}]`, mostre os nomes de quem tem 16 anos ou mais e calcule a idade média da turma.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas e dicionários. Para cada exercício, o Input e o Output esperados estão descritos.

26. (Boletim da Turma) Receba o nome de um aluno e suas 3 notas, repetindo até o usuário digitar `'FIM'` no nome. Guarde tudo em um dicionário `{nome: [nota1, nota2, nota3]}`. Ao final, mostre a média de cada aluno e a situação: `Aprovado` (média >= 7), `Recuperação` (média >= 5) ou `Reprovado`.
    Input:
    ```
    Ana
    8
    9
    7
    Beto
    4
    5
    3
    FIM
    ```
    Output:
    ```
    Ana: média 8.0 - Aprovado
    Beto: média 4.0 - Reprovado
    ```

27. (Loja Virtual do Jogo) Existe uma loja com estoque `{'pocao': 5, 'espada': 2, 'escudo': 1}` e preços `{'pocao': 10, 'espada': 50, 'escudo': 35}`. O jogador tem moedas e digita o item que quer comprar até digitar `'SAIR'`. Valide se o item existe, se há estoque e se há moedas suficientes. A cada compra, atualize estoque e moedas. Ao final, mostre o saldo e o que foi comprado.
    Input:
    ```
    Moedas iniciais: 70
    pocao
    espada
    escudo
    SAIR
    ```
    Output:
    ```
    Comprou: pocao (10 moedas)
    Comprou: espada (50 moedas)
    Moedas insuficientes para: escudo
    Saldo final: 10
    Itens comprados: {'pocao': 1, 'espada': 1}
    ```

28. (Analisador de Texto) Receba uma frase e mostre: a quantidade de palavras, a palavra mais frequente, e um dicionário que agrupa as palavras pelo tamanho. Ignore diferenças entre maiúsculas e minúsculas.
    Input:
    ```
    O gato viu o rato e o rato viu o gato
    ```
    Output:
    ```
    Total de palavras: 10
    Mais frequente: o (4 vezes)
    Por tamanho: {1: ['o', 'e'], 4: ['gato', 'rato'], 3: ['viu']}
    ```

29. (Ranking de Campeonato) Dada uma lista de partidas, onde cada partida é um dicionário `{'jogador': str, 'pontos': int}`, some os pontos de cada jogador em um dicionário e mostre o ranking do maior para o menor. Em caso de empate, mantenha a ordem em que o jogador apareceu primeiro.
    Input (já carregado no programa):
    ```python
    partidas = [
        {'jogador': 'Ana', 'pontos': 30},
        {'jogador': 'Beto', 'pontos': 20},
        {'jogador': 'Ana', 'pontos': 15},
        {'jogador': 'Cris', 'pontos': 60},
        {'jogador': 'Beto', 'pontos': 25}
    ]
    ```
    Output:
    ```
    1º Cris - 60 pontos
    2º Ana - 45 pontos
    3º Beto - 45 pontos
    ```

30. (Mini-projeto: Sistema de Biblioteca) Crie um programa com um dicionário `livros` no formato `{titulo: {'autor': str, 'disponivel': bool}}`. O usuário digita comandos até `SAIR`:
    - `ADICIONAR titulo;autor`: cadastra um livro novo (não permitir título repetido).
    - `EMPRESTAR titulo`: só funciona se o livro existir e estiver disponível.
    - `DEVOLVER titulo`: marca o livro como disponível novamente.
    - `LISTAR`: mostra todos os livros e a situação de cada um.
    Input:
    ```
    ADICIONAR Harry Potter;J.K. Rowling
    ADICIONAR Percy Jackson;Rick Riordan
    EMPRESTAR Harry Potter
    EMPRESTAR Harry Potter
    LISTAR
    SAIR
    ```
    Output:
    ```
    Livro cadastrado: Harry Potter
    Livro cadastrado: Percy Jackson
    Você pegou emprestado: Harry Potter
    Livro indisponível: Harry Potter
    Harry Potter (J.K. Rowling) - Emprestado
    Percy Jackson (Rick Riordan) - Disponível
    ```

---
