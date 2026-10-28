# Módulo 8 — Tuplas e Conjuntos (set)

## 1. Introdução Teórica e Prática

Você já conhece listas e dicionários. Agora vão entrar mais duas estruturas, cada uma com um superpoder:

- **Tupla**: parece uma lista, mas **não pode ser alterada**. Pense nas coordenadas de um mapa de jogo `(x, y)` ou nas cores RGB `(255, 0, 0)`: o par pertence junto e não faz sentido mudar só um pedaço.
- **Conjunto (`set`)**: uma coleção **sem itens repetidos** e **sem ordem**. Pense nos seguidores de uma conta: cada pessoa aparece uma vez só, e dá para perguntar "quem segue as duas contas?".

Por que isso é útil?
- Tuplas protegem dados que não devem mudar e permitem devolver vários valores de uma função.
- Conjuntos removem repetidos em um passo e fazem buscas muito rápidas.
- Conjuntos respondem perguntas como "o que temos em comum?" e "o que falta?" sem precisar de loops.
- Combinam com tudo que você já viu: loops, `if`, listas, dicionários, funções e strings.

### Tuplas: criando e acessando

```python
# parênteses e vírgulas; a ordem importa
posicao = (3, 7)
cores = ('azul', 'verde', 'vermelho')

print(posicao[0])    # 3 -> índices funcionam como nas listas
print(cores[-1])     # 'vermelho'
print(cores[0:2])    # ('azul', 'verde') -> fatiamento também

# posicao[0] = 10    # ERRO! tuplas são imutáveis

# tupla de um item só precisa da vírgula
sozinho = ('ouro',)
print(type(sozinho))  # <class 'tuple'>
```

### Desempacotando: abrindo a tupla em variáveis

```python
posicao = (3, 7)
x, y = posicao        # x vale 3 e y vale 7
print(f'x={x}, y={y}')
```

### Funções que devolvem vários valores

```python
# na verdade a função devolve UMA tupla, e você a desempacota
def menor_e_maior(numeros):
    return min(numeros), max(numeros)

menor, maior = menor_e_maior([5, 2, 9, 1])
print(menor, maior)  # 1 9
```

### Lista de tuplas e tupla como chave de dicionário

```python
# cada tupla é um "registro" fixo: (nome, nota)
alunos = [('Ana', 8.5), ('Beto', 6.0)]

for nome, nota in alunos:     # desempacota direto no for
    print(nome, nota)

# como a tupla não muda, ela pode ser chave de dicionário
tabuleiro = {(0, 0): 'X', (1, 1): 'O'}
print(tabuleiro[(1, 1)])      # 'O'
```

### Conjuntos: criando e alterando

```python
# repetidos desaparecem automaticamente
seguidores = {'Ana', 'Beto', 'Ana', 'Cris'}
print(len(seguidores))        # 3

seguidores.add('Davi')        # adiciona
seguidores.discard('Zé')      # remove sem dar erro se não existir
seguidores.remove('Beto')     # remove, mas dá erro se não existir

# atenção: {} vazio é um dicionário! Para conjunto vazio, use set()
vazio = set()

# 'in' em conjunto é rápido
if 'Ana' in seguidores:
    print('Ana segue!')
```

### Removendo repetidos de uma lista

```python
votos = ['Ana', 'Beto', 'Ana', 'Cris', 'Beto']
unicos = set(votos)           # {'Ana', 'Beto', 'Cris'}
lista_unica = list(unicos)    # volta para lista, se precisar
```

### Operações entre conjuntos

```python
amigos_ana = {'Beto', 'Cris', 'Davi'}
amigos_beto = {'Ana', 'Cris', 'Eva'}

print(amigos_ana | amigos_beto)  # união: todo mundo (sem repetir)
print(amigos_ana & amigos_beto)  # interseção: {'Cris'} -> em comum
print(amigos_ana - amigos_beto)  # diferença: só da Ana -> {'Beto', 'Davi'}
print(amigos_ana ^ amigos_beto)  # só em um dos dois (sem os comuns)
```

### Conjuntos não têm ordem

```python
# print(seguidores[0])  # ERRO! não existe "primeiro item" em um set
# para mostrar em ordem, use sorted(), que devolve uma LISTA ordenada
print(sorted(seguidores))
```

Dica: use **tupla** quando os dados formam um registro fixo, **lista** quando a coleção vai mudar e a ordem importa, **conjunto** quando só interessa "tem ou não tem" e sem repetidos.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas, Dicionários, Funções e Strings.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Crie uma tupla `cores` com 3 cores e imprima-a.
2. Mostre o primeiro e o último item da tupla `posicao = (10, 20, 30)`.
3. Tente alterar um item de uma tupla, observe o erro e escreva em um comentário por que ele acontece.
4. Crie uma tupla com um único item e confira seu tipo com `type()`.
5. Desempacote `ponto = (3, 7)` nas variáveis `x` e `y` e mostre cada uma.
6. Dada a tupla `numeros = (4, 2, 4, 9, 4)`, mostre o tamanho com `len()`, quantos `4` existem com `count()` e a posição do `9` com `index()`.
7. Use fatiamento para mostrar os 3 primeiros itens de uma tupla de 5 itens.
8. Converta uma lista em tupla e depois a tupla de volta em lista.
9. Crie um conjunto `frutas` com itens repetidos e imprima. O que aconteceu com os repetidos?
10. Crie um conjunto vazio com `set()` e adicione 3 itens com `add()`.
11. Remova um item que existe com `remove()` e tente remover um que não existe com `discard()`. Depois troque por `remove()` e veja o erro.
12. Verifique, com `in`, se `'Ana'` está em um conjunto de nomes.
13. Converta a lista `[1, 2, 2, 3, 3, 3]` em conjunto e mostre quantos valores únicos existem.
14. Dados dois conjuntos `a` e `b`, mostre a união e a interseção.
15. Dados os mesmos conjuntos, mostre a diferença (`a - b`) e a diferença simétrica (`a ^ b`).

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use tuplas e conjuntos junto com `for`/`while`, `if`/`else`, listas, dicionários, funções e strings.

16. (Mapa do jogo) Dada a lista de posições `[(0, 0), (2, 3), (5, 1), (2, 3), (4, 4)]`, use um loop com desempacotamento para mostrar `x=.., y=..` apenas das posições em que `x` é maior que 1.
17. (Estatísticas) Crie `resumo(notas)` que retorna uma tupla com a menor nota, a maior nota e a média. Receba o resultado em três variáveis e mostre a média com 1 casa decimal.
18. (Boletim) Dada a lista `alunos = [('Ana', 8.5), ('Beto', 6.0), ('Cris', 9.0), ('Davi', 5.5)]`, crie uma lista só com os nomes dos aprovados (nota >= 7.0) e mostre quem tirou a maior nota.
19. (Lista de convidados) Receba nomes até o usuário digitar `FIM`. Mostre quantos nomes únicos foram digitados e a lista deles em ordem alfabética, ignorando diferenças entre maiúsculas e minúsculas.
20. (Amigos em comum) Dados `amigos_ana` e `amigos_beto` como conjuntos, mostre quem é amigo dos dois, quem é amigo só da Ana e a lista completa de amigos. Depois leia um nome e diga se ele é amigo de pelo menos um dos dois.
21. (Letras repetidas) Crie `tem_letra_repetida(palavra)` que compara o tamanho da palavra com o tamanho do conjunto das suas letras. Teste com uma lista de palavras e mostre também quantas letras diferentes cada uma tem.
22. (Pangrama) Crie `eh_pangrama(frase)` que retorna `True` se a frase usa todas as 26 letras do alfabeto. Use um conjunto, ignore espaços e maiúsculas. Teste com `'the quick brown fox jumps over the lazy dog'`.
23. (Tabuleiro com coordenadas) Crie o dicionário `tabuleiro = {(0, 0): 'X', (1, 1): 'O', (2, 2): 'X'}`. Leia uma coordenada no formato `linha coluna`, converta para uma tupla de inteiros e mostre a peça daquela posição ou `'vazio'`.
24. (Missão do RPG) Dados o conjunto `itens_missao = {'mapa', 'chave', 'tocha', 'corda'}` e o conjunto `mochila` do jogador, mostre o que está faltando e o que está sobrando. Se não faltar nada, mostre `'Missão liberada!'`.
25. (Ranking com tuplas) Dado `pontos = {'Ana': 120, 'Beto': 90, 'Cris': 150, 'Davi': 110}`, monte uma lista de tuplas `(pontos, nome)` com um loop, ordene do maior para o menor com `sort(reverse=True)` e mostre o top 3 no formato `1º Cris - 150`.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários, funções, strings, tuplas e conjuntos. O Input e o Output esperados estão descritos.

26. (Controle de Sala de Voz) Use um conjunto para controlar quem está em uma sala de voz. O programa lê comandos até `FIM`. `ENTRAR nome` coloca a pessoa na sala (avise se já estiver lá), `DEIXAR nome` tira a pessoa (avise se não estiver) e `LISTAR` mostra quantas pessoas estão na sala, em ordem alfabética.
    Input:
    ```
    ENTRAR Ana
    ENTRAR Beto
    ENTRAR Ana
    DEIXAR Cris
    DEIXAR Beto
    LISTAR
    FIM
    ```
    Output:
    ```
    Ana entrou na sala
    Beto entrou na sala
    Ana já está na sala
    Cris não está na sala
    Beto saiu da sala
    Na sala (1): Ana
    ```

27. (Combinador de Gostos) Dado `gostos = {'Ana': {'anime', 'terror', 'ficcao'}, 'Beto': {'anime', 'ficcao', 'comedia'}, 'Cris': {'comedia', 'romance'}}`, compare todas as duplas de pessoas (sem repetir a mesma dupla nem comparar alguém com ele mesmo) e mostre os gêneros em comum de cada uma, em ordem alfabética. No final, mostre a dupla com mais gêneros em comum.
    Input: o dicionário já está definido no programa.
    Output:
    ```
    Ana e Beto: ['anime', 'ficcao']
    Ana e Cris: []
    Beto e Cris: ['comedia']
    Melhor dupla: Ana e Beto (2 em comum)
    ```

28. (Batalha Naval Simplificada) Os navios ocupam as posições `{(1, 1), (1, 2), (3, 4)}` (conjunto de tuplas). O jogador digita palpites no formato `linha coluna`. Responda `Acertou!` ou `Água.`; se a posição já foi tentada, responda `Você já tentou essa posição.` (palpite repetido não conta como tentativa). O jogo termina quando todos os navios forem afundados.
    Input:
    ```
    1 1
    0 0
    1 1
    1 2
    3 4
    ```
    Output:
    ```
    Acertou!
    Água.
    Você já tentou essa posição.
    Acertou!
    Acertou!
    Você afundou todos os navios em 4 tentativas.
    ```

29. (Comparador de Textos) Receba duas frases e compare as palavras de cada uma usando conjuntos (tudo em minúsculas). Mostre as palavras em comum, as que só aparecem na primeira, as que só aparecem na segunda (todas em ordem alfabética) e a similaridade em porcentagem, calculada como `palavras em comum / total de palavras diferentes das duas frases * 100`, com 1 casa decimal.
    Input:
    ```
    o gato subiu no telhado
    o gato desceu do telhado
    ```
    Output:
    ```
    Palavras em comum: ['gato', 'o', 'telhado']
    Só na primeira: ['no', 'subiu']
    Só na segunda: ['desceu', 'do']
    Similaridade: 42.9%
    ```

30. (Mini-projeto: Matrículas dos Cursos) Use um dicionário `{curso: conjunto de alunos}`. O programa lê comandos até `FIM`: `MATRICULAR aluno curso`, `CANCELAR aluno curso`, `AMBOS curso1 curso2` (alunos matriculados nos dois cursos) e `LISTAR curso`. Guarde cada `MATRICULAR` e `CANCELAR` em uma lista de históricos como uma tupla `(acao, aluno, curso)` e mostre o total de operações registradas no final.
    Input:
    ```
    MATRICULAR Ana Python
    MATRICULAR Beto Python
    MATRICULAR Ana Games
    MATRICULAR Cris Games
    AMBOS Python Games
    CANCELAR Beto Python
    LISTAR Python
    FIM
    ```
    Output:
    ```
    Matrícula feita: Ana -> Python
    Matrícula feita: Beto -> Python
    Matrícula feita: Ana -> Games
    Matrícula feita: Cris -> Games
    Em ambos (Python e Games): ['Ana']
    Matrícula cancelada: Beto -> Python
    Python: ['Ana']
    Operações registradas: 5
    ```
