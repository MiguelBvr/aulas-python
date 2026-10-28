# Módulo 12 — List Comprehensions e Funções Úteis

## 1. Introdução Teórica e Prática

Você já sabe criar listas com `for`, filtrar com `if` e ordenar de várias formas. Agora vem o **atalho dos atalhos**: fazer em **uma linha** o que antes levava quatro. É como o **modo rápido do jogo**: você já sabe o caminho longo, e agora aprende o teleporte. Junto com ele, vamos conhecer funções prontas do Python que resolvem problemas comuns (`sorted`, `zip`, `enumerate`, `any`, `all`...).

Por que isso é útil?
- Código mais curto e fácil de ler (quando bem usado).
- Resolve filtros, transformações e contagens de forma direta.
- É o estilo que quase todo programador Python usa no dia a dia.
- Combina com tudo o que você já viu: loops, `if`, listas, dicionários, funções, strings, conjuntos, arquivos e módulos.

Regra de ouro: **sempre aprenda o jeito tradicional primeiro**. A comprehension é só um jeito mais curto de escrever o mesmo `for`. Se ficar difícil de ler, volte para o `for` normal.

### List comprehension: do `for` tradicional ao atalho

```python
numeros = [1, 2, 3, 4, 5]

# jeito tradicional
dobros = []
for n in numeros:
    dobros.append(n * 2)

# atalho: [o que fazer   for item in lista]
dobros = [n * 2 for n in numeros]
```

### Com filtro (if no final)

```python
# tradicional
pares = []
for n in range(1, 11):
    if n % 2 == 0:
        pares.append(n)

# atalho: o 'if' filtra quem entra na lista
pares = [n for n in range(1, 11) if n % 2 == 0]
```

### Com if/else (vai no começo!)

```python
# aqui o if/else TRANSFORMA o valor, não filtra
notas = [8, 4, 6, 9]
situacoes = ['Aprovado' if nota >= 7 else 'Estudar mais' for nota in notas]
```

### Dicionários e conjuntos também têm atalho

```python
nomes = ['Ana', 'Beto', 'Alice']

# dict comprehension: {chave: valor for ...}
tamanhos = {nome: len(nome) for nome in nomes}   # {'Ana': 3, 'Beto': 4, 'Alice': 5}

# set comprehension: {valor for ...} (sem repetidos)
iniciais = {nome[0] for nome in nomes}           # {'A', 'B'}
```

### enumerate: item e posição juntos

```python
herois = ['Naruto', 'Goku', 'Luffy']

# start=1 faz a contagem começar do 1 em vez do 0
for posicao, heroi in enumerate(herois, start=1):
    print(f'{posicao}º {heroi}')
```

### zip: juntando listas "lado a lado"

```python
nomes = ['Ana', 'Beto', 'Cris']
notas = [8, 6, 9]

for nome, nota in zip(nomes, notas):
    print(nome, nota)

notas_por_aluno = dict(zip(nomes, notas))   # {'Ana': 8, 'Beto': 6, 'Cris': 9}
```

### sorted, min e max com key

```python
palavras = ['python', 'if', 'for', 'dicionario']

print(sorted(palavras))                  # ordem alfabética (a original não muda)
print(sorted(palavras, reverse=True))    # ordem inversa

# key diz "o que olhar" ao comparar; lambda é uma função de uma linha, sem nome
print(sorted(palavras, key=len))                    # do menor para o maior tamanho
print(max(palavras, key=len))                       # 'dicionario'
print(min(palavras, key=lambda p: p[-1]))           # menor pela última letra

# ordenar por duas regras: use uma tupla (o sinal - inverte números)
alunos = [('Ana', 8), ('Beto', 9), ('Cris', 8)]
print(sorted(alunos, key=lambda a: (-a[1], a[0])))  # nota maior primeiro, depois nome
```

### any e all: perguntas de sim ou não sobre a lista

```python
notas = [8, 4, 6, 9]

print(any(n < 5 for n in notas))    # True -> ALGUMA nota é menor que 5?
print(all(n >= 4 for n in notas))   # True -> TODAS são maiores ou iguais a 4?
print(sum(1 for n in notas if n >= 7))   # conta quantos passam: 2
```

### map e filter (a versão "de funções")

```python
numeros = [1, 2, 3, 4, 5, 6]

quadrados = list(map(lambda n: n ** 2, numeros))        # aplica em todos
pares = list(filter(lambda n: n % 2 == 0, numeros))     # fica quem retorna True
# mesma coisa, mais legível: [n ** 2 for n in numeros] e [n for n in numeros if n % 2 == 0]
```

Dica: não coloque lógica demais em uma única linha. Se a comprehension passar de uns 80 caracteres ou tiver `if` dentro de `if`, vale voltar ao `for`.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas, Dicionários, Funções, Strings, Tuplas e Conjuntos, Arquivos, Tratamento de Erros e Módulos. Resolva primeiro com `for` tradicional quando tiver dúvida e depois reescreva com os atalhos.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Crie a lista dos quadrados de 1 a 10 primeiro com `for` e `append()` e depois com list comprehension.
2. Dobre cada número da lista `[1, 2, 3, 4, 5]` com uma list comprehension.
3. Crie uma lista só com os números pares de 1 a 20 (`range` e `if`).
4. Dada uma lista de palavras, crie duas listas: uma com as palavras em maiúsculas e outra com o tamanho de cada palavra.
5. Dada a lista de notas `[8, 4, 6.5, 9, 3]`, crie uma lista só com as notas maiores ou iguais a 7.
6. Crie uma lista de `'par'` ou `'ímpar'` para os números de 1 a 6, usando `if`/`else` dentro da comprehension.
7. Crie o dicionário `{n: n ** 2}` para os números de 1 a 5 com uma dict comprehension.
8. Dada a lista `['Ana', 'Alice', 'Beto', 'Bia']`, crie um conjunto com as iniciais dos nomes (set comprehension).
9. Mostre cada item de uma lista com sua posição, começando do 1, usando `enumerate`.
10. Junte as listas `nomes` e `notas` com `zip` e mostre cada par.
11. Ordene `[5, 2, 9, 1]` do menor para o maior e do maior para o menor com `sorted()`, sem alterar a lista original.
12. Ordene uma lista de palavras pelo tamanho usando `sorted(..., key=len)`.
13. Mostre a palavra mais longa e a mais curta de uma lista com `max()` e `min()` usando `key=len`.
14. Dada uma lista de notas, descubra com `any()` se existe alguma nota abaixo de 5 e com `all()` se todas são maiores ou iguais a 5.
15. Use `map()` com `lambda` para elevar ao cubo os números de uma lista e `filter()` com `lambda` para manter só os ímpares. Converta os resultados com `list()`.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use comprehensions e funções úteis junto com `for`/`while`, `if`/`else`, listas, dicionários, funções, strings, tuplas, conjuntos, arquivos, tratamento de erros e módulos.

16. (Notas da escola) Dado `notas = {'Ana': 8.5, 'Beto': 6.0, 'Cris': 9.0, 'Davi': 4.5}`, crie com comprehensions: o dicionário só com os aprovados (nota >= 7), o dicionário `{nome: situação}` (`Aprovado` ou `Recuperação`) e a quantidade de aprovados.
17. (Inventário RPG) Dada uma lista de dicionários `{'nome', 'preco', 'qtd'}`, calcule o valor total do inventário com `sum()` e uma comprehension, liste os nomes dos itens com preço acima de 100 e mostre os itens ordenados do mais caro para o mais barato.
18. (Nomes bagunçados) Dada a lista `['  ana ', 'BETO', 'cRiS', 'ana', ' beto']`, limpe cada nome com `strip()` e `title()`, remova os repetidos com uma set comprehension e mostre o resultado ordenado.
19. (Frases) Dada uma frase, crie a lista das palavras com mais de 4 letras e um dicionário `{palavra: quantidade de vogais}` usando comprehensions.
20. (Tabuada) Crie com comprehensions aninhadas a tabuada de 1 a 5 como lista de listas (`[[1, 2, 3, ...], [2, 4, 6, ...], ...]`) e mostre cada linha formatada.
21. (Ranking) Dado `pontos = {'Ana': 120, 'Beto': 90, 'Cris': 150, 'Davi': 110}`, mostre o top 3 com `sorted(pontos.items(), key=lambda ...)` e `enumerate(..., start=1)` no formato `1º Cris - 150`.
22. (Campeonato com zip) Dadas as listas `jogadores` e `pontos`, monte um dicionário com `zip`, descubra o campeão com `max(..., key=...)` e use `any()` para avisar se algum jogador tem zero pontos.
23. (Senha forte) Crie `senha_forte(senha)` que usa `any()` para exigir pelo menos um número (`isdigit()`), uma letra maiúscula (`isupper()`) e uma minúscula (`islower()`), além de 8 caracteres ou mais. Use uma list comprehension para filtrar as senhas fortes de uma lista.
24. (CSV com comprehension) O arquivo `notas.csv` tem este conteúdo:
    ```
    Ana,8.5
    Beto,6
    Cris,9
    Davi,4.5
    ```
    Leia o arquivo e transforme-o em uma lista de tuplas `(nome, nota)` com uma comprehension. Mostre os 2 melhores alunos e a média da turma (módulo `statistics`). Trate o caso de o arquivo não existir.
25. (Agrupando por tamanho) Dada uma lista de palavras, crie com uma dict comprehension (e uma set comprehension para os tamanhos) o dicionário `{tamanho: [palavras com esse tamanho]}`.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários, funções, strings, tuplas, conjuntos, arquivos, tratamento de erros, módulos e comprehensions. O Input e o Output esperados estão descritos.

26. (Relatório do Inventário) Dada a lista abaixo, use comprehensions, `sum`, `max`, `sorted` e `lambda` para gerar o relatório. O preço médio é a média dos preços dos itens (sem considerar a quantidade). Os itens acima da média ficam na ordem original da lista.
    Input (já definido no programa):
    ```python
    itens = [
        {'nome': 'Poção', 'tipo': 'consumivel', 'preco': 10, 'qtd': 5},
        {'nome': 'Espada', 'tipo': 'arma', 'preco': 120, 'qtd': 1},
        {'nome': 'Escudo', 'tipo': 'armadura', 'preco': 80, 'qtd': 2},
        {'nome': 'Elixir', 'tipo': 'consumivel', 'preco': 45, 'qtd': 3},
        {'nome': 'Arco', 'tipo': 'arma', 'preco': 95, 'qtd': 1},
    ]
    ```
    Output:
    ```
    Valor total: 560
    Valor por tipo:
    arma: 215
    consumivel: 185
    armadura: 160
    Mais caro: Espada (120)
    Acima do preço médio (70.0): Espada, Escudo, Arco
    ```

27. (Analisador do Chat) O programa lê mensagens no formato `usuario: texto` até `FIM`. Mostre quantas mensagens cada usuário enviou, o usuário mais ativo e as 3 palavras mais usadas (em caso de empate, vale a ordem em que a palavra apareceu primeiro). Use dicionários, `sorted`, `max` e comprehensions.
    Input:
    ```
    Ana: oi pessoal vamos jogar
    Beto: vamos jogar agora
    Ana: bora jogar
    Cris: oi
    FIM
    ```
    Output:
    ```
    Mensagens por usuário: {'Ana': 2, 'Beto': 1, 'Cris': 1}
    Mais ativo: Ana (2)
    Palavras mais usadas: jogar (3), oi (2), vamos (2)
    ```

28. (Boletim Completo em CSV) O arquivo `turma.csv` tem este conteúdo:
    ```
    nome,mat,port,hist
    Ana,8,9,7
    Beto,4,5,3
    Cris,6,7,5
    Davi,10,9,9
    ```
    Leia o arquivo (ignorando o cabeçalho) e use comprehensions, `zip`, `sum`, `max`, `min` e `sorted` para calcular as médias dos alunos, as médias das disciplinas, o melhor aluno, a lista de aprovados (média >= 7) e a disciplina mais difícil (menor média). Todas as médias são mostradas com 1 casa decimal.
    Input: o arquivo `turma.csv` descrito acima.
    Output:
    ```
    Médias dos alunos: Ana 8.0, Beto 4.0, Cris 6.0, Davi 9.3
    Médias das disciplinas: mat 7.0, port 7.5, hist 6.0
    Melhor aluno: Davi (9.3)
    Aprovados (média >= 7): Ana, Davi
    Disciplina mais difícil: hist (6.0)
    ```

29. (Estatísticas do Campeonato) Dadas as listas abaixo, use `zip`, `enumerate`, `sum`, `max`, `any`, `all` e `sorted` para mostrar o ranking pelo total de pontos (em caso de empate, vale a ordem da lista), o jogador com a maior pontuação em uma única partida, quem teve alguma partida zerada e quem manteve todas as partidas acima de 20 pontos.
    Input (já definido no programa):
    ```python
    jogadores = ['Ana', 'Beto', 'Cris', 'Davi']
    partidas = [[10, 20, 15], [30, 5, 10], [25, 25, 25], [0, 40, 10]]
    ```
    Output:
    ```
    1º Cris - 75
    2º Davi - 50
    3º Ana - 45
    4º Beto - 45
    Melhor partida: Davi (40)
    Alguma partida zerada: Davi
    Todas as partidas acima de 20: Cris
    ```

30. (Mini-projeto: Catálogo de Séries) O arquivo `series.csv` tem este conteúdo:
    ```
    titulo,genero,nota,episodios
    Naruto,anime,8.3,220
    Attack on Titan,anime,9.0,87
    Stranger Things,ficcao,8.7,34
    Death Note,anime,9.0,37
    The Witcher,fantasia,8.0,24
    ```
    Carregue o arquivo em uma lista de dicionários com uma comprehension (trate o arquivo inexistente). O programa lê comandos até `SAIR`: `GENERO g` (séries do gênero, da maior nota para a menor e, em caso de empate, em ordem alfabética), `TOP n` (as `n` melhores com a mesma regra de ordenação), `TOTAL` (total de episódios), `MEDIA g` (média das notas do gênero) e `BUSCA texto` (títulos que contêm o texto, sem diferenciar maiúsculas e minúsculas). Trate gênero inexistente e `n` que não é número inteiro.
    Input:
    ```
    GENERO anime
    TOP 2
    TOTAL
    MEDIA ficcao
    BUSCA the
    MEDIA terror
    TOP abc
    SAIR
    ```
    Output:
    ```
    Attack on Titan - 9.0
    Death Note - 9.0
    Naruto - 8.3
    1º Attack on Titan - 9.0
    2º Death Note - 9.0
    Total de episódios: 402
    Média de ficcao: 8.7
    The Witcher
    Erro: gênero 'terror' não encontrado
    Erro: digite um número inteiro
    ```
