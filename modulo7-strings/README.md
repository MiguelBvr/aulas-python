# Módulo 7 — Strings (Manipulação de Texto)

## 1. Introdução Teórica e Prática

Uma string é um **texto**: uma sequência de caracteres, como uma fila de letrinhas. Pense em um **colar de contas**, em que cada conta é um caractere e tem uma posição. Tudo o que envolve texto usa strings: nome de usuário, mensagem no chat, legenda de post, senha, comentário de vídeo.

Por que isso é útil?
- Limpar e padronizar o que o usuário digita (espaços sobrando, maiúsculas e minúsculas).
- Validar dados: e-mail, senha, nome de usuário.
- Filtrar e transformar mensagens (censurar palavras, achar hashtags).
- Montar textos bonitos para mostrar na tela.
- Combina com tudo o que você já viu: loops, `if`, listas, dicionários e funções.

### Posição e tamanho

```python
usuario = 'miguel'

print(len(usuario))   # 6 -> quantos caracteres
print(usuario[0])     # 'm' -> a contagem começa no zero
print(usuario[-1])    # 'l' -> índice negativo conta de trás para frente
```

### Fatiamento (slice)

```python
palavra = 'videogame'

print(palavra[0:5])   # 'video' -> do índice 0 até o 4 (o 5 não entra)
print(palavra[5:])    # 'game' -> do 5 até o fim
print(palavra[:5])    # 'video' -> do começo até o 4
print(palavra[::-1])  # 'emagoediv' -> o texto invertido
```

### Strings não podem ser alteradas "por dentro"

```python
nome = 'Ana'
# nome[0] = 'E'   # ERRO! strings são imutáveis
nome = 'E' + nome[1:]  # o jeito certo: criar uma string nova -> 'Ena'
```

### Métodos úteis

```python
mensagem = '   Oi, Mundo!   '

print(mensagem.strip())     # 'Oi, Mundo!' -> tira espaços das pontas
print(mensagem.upper())     # tudo em maiúsculas
print(mensagem.lower())     # tudo em minúsculas
print('python legal'.title())              # 'Python Legal'
print('gato feio'.replace('feio', 'fofo'))  # 'gato fofo'
print('banana'.count('a'))                  # 3
print('banana'.find('n'))                   # 2 (posição); -1 se não achar
print('foto.png'.endswith('.png'))          # True
print('foto.png'.startswith('video'))       # False
```

### Verificando conteúdo

```python
print('gato' in 'o gato subiu')   # True -> 'in' procura um pedaço do texto
print('123'.isdigit())            # True -> só tem números
print('abc'.isalpha())            # True -> só tem letras
```

### Percorrendo com for

```python
# a string é percorrida caractere por caractere
for letra in 'ola':
    print(letra)
```

### split e join: de texto para lista e de volta

```python
frase = 'eu amo python'

palavras = frase.split()          # ['eu', 'amo', 'python']
print('-'.join(palavras))         # 'eu-amo-python'
print('a,b,c'.split(','))         # ['a', 'b', 'c'] -> separando por vírgula
```

### f-strings: montando textos sem dor de cabeça

```python
nome = 'Miguel'
nivel = 12
preco = 9.5

print(f'{nome} está no nível {nivel}')   # Miguel está no nível 12
print(f'Preço: R$ {preco:.2f}')          # 2 casas decimais -> R$ 9.50
print(f'{nome:<10}|{nivel:>5}')          # alinha à esquerda (10) e à direita (5)
```

Dica: ao comparar textos, deixe tudo em minúsculas antes (`texto.lower()`). Assim `'Sim'`, `'SIM'` e `'sim'` viram a mesma coisa.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas, Dicionários e Funções.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Guarde seu nome em uma variável `nome` e mostre quantos caracteres ele tem usando `len()`.
2. Mostre o primeiro e o último caractere da string `'python'`.
3. Dada a string `'videogame'`, use fatiamento para mostrar `'video'` e depois `'game'`.
4. Inverta a string `'amor'` usando fatiamento.
5. Mostre a string `'python legal'` em maiúsculas, em minúsculas e com `title()`.
6. Use `strip()` para remover os espaços das pontas de `'   oi   '`.
7. Troque `'feio'` por `'bonito'` na frase `'o dia está feio'` usando `replace()`.
8. Conte quantas vezes a letra `'a'` aparece em `'banana'`.
9. Use `find()` para mostrar a posição de `'o'` em `'mundo'` e o resultado ao procurar `'z'`.
10. Verifique se `'foto.png'` termina com `'.png'` e se começa com `'video'`.
11. Verifique, com `in`, se a palavra `'gato'` está em `'o gato subiu no telhado'`.
12. Una `'Mi'` e `'guel'` com `+` e repita `'ha'` três vezes com `*`.
13. Separe a frase `'eu amo programar'` em uma lista de palavras com `split()`.
14. Una a lista `['a', 'b', 'c']` em uma única string `'a-b-c'` usando `join()`.
15. Use uma f-string para mostrar `'Miguel tem 15 anos e 1.75 de altura'`, com a altura em 2 casas decimais.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use strings junto com `for`/`while`, `if`/`else`, listas, dicionários e funções.

16. (Rede social) Crie `limpar_usuario(texto)` que remove os espaços das pontas, deixa tudo em minúsculas e troca espaços do meio por `_`. Depois crie `usuario_valido(nome)`: ele deve ter de 3 a 15 caracteres e só pode conter letras, números e `_`. Teste com uma lista de nomes bagunçados.
17. (Palíndromo) Crie `eh_palindromo(frase)` que ignora espaços e maiúsculas. Ex.: `'Socorram me subi no onibus em Marrocos'` é um palíndromo.
18. (Vogais) Crie `contar_vogais(texto)` que usa um loop e um `if` para contar as vogais. Retorne um dicionário com a contagem de cada uma.
19. (Iniciais) Receba o nome completo e mostre as iniciais em maiúsculas. Ex.: `'miguel santos silva'` vira `'MSS'`.
20. (Chat moderado) Dada a lista `proibidas = ['feio', 'chato']`, crie `censurar(mensagem, proibidas)` que troca cada palavra proibida por asteriscos do mesmo tamanho, sem diferenciar maiúsculas e minúsculas na hora de comparar.
21. (Cifra de César) Crie `cifrar(texto, deslocamento)` que troca cada letra pela que está `deslocamento` posições à frente no alfabeto (volte ao início depois do `z`). Use a string `'abcdefghijklmnopqrstuvwxyz'` e `find()`. Mantenha espaços sem alterar.
22. (E-mail) Crie `email_valido(email)`: precisa ter exatamente um `@`, não ter espaços e ter um ponto depois do `@`. Teste com uma lista de e-mails certos e errados.
23. (Hashtags) Dado um post como `'Hoje foi dia de #python e #games com a galera'`, crie `extrair_hashtags(post)` que retorna uma lista com as palavras que começam com `#`.
24. (Agenda por inicial) Dada uma lista de nomes bagunçados, como `['  ana ', 'BETO', 'alice', ' bia']`, limpe cada nome com `strip()` e `title()` e monte um dicionário que agrupa os nomes pela primeira letra. Ex.: `{'A': ['Ana', 'Alice'], 'B': ['Beto', 'Bia']}`.
25. (Placar formatado) Dada uma lista de dicionários `{'nome': str, 'pontos': int}`, mostre uma tabela alinhada com f-strings: nome à esquerda (largura 10) e pontos à direita (largura 6).

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários, funções e strings. O Input e o Output esperados estão descritos.

26. (Chat Moderado) O programa lê mensagens no formato `usuario: texto` até o usuário digitar `SAIR`. As palavras proibidas são `feio` e `chato` (sem diferenciar maiúsculas e minúsculas). Mostre cada mensagem já censurada e, no final, quantas mensagens precisaram de censura.
    Input:
    ```
    Ana: oi pessoal
    Beto: que jogo chato
    Cris: eu sou feio mesmo
    SAIR
    ```
    Output:
    ```
    Ana: oi pessoal
    Beto: que jogo *****
    Cris: eu sou **** mesmo
    Mensagens censuradas: 2
    ```

27. (Tradutor de Código Morse) Crie um dicionário com pelo menos as letras `a`, `i`, `n`, `o` e `s` (`a` = `.-`, `i` = `..`, `n` = `-.`, `o` = `---`, `s` = `...`). O programa lê comandos até `FIM`. `CODIFICAR texto` converte o texto, com letras separadas por espaço e palavras separadas por ` / `. `DECODIFICAR codigo` faz o caminho de volta.
    Input:
    ```
    CODIFICAR sos
    DECODIFICAR ... --- ...
    CODIFICAR oi ana
    FIM
    ```
    Output:
    ```
    ... --- ...
    sos
    --- .. / .- -. .-
    ```

28. (Gerador de E-mails da Escola) O programa lê nomes completos até `FIM` e gera o e-mail no formato `primeironome.ultimosobrenome@escola.com`, tudo em minúsculas. Se o e-mail já tiver sido gerado, acrescente um número (`2`, `3`...) depois do sobrenome. Use um dicionário para controlar os repetidos.
    Input:
    ```
    Miguel Santos Silva
    Ana Paula Souza
    Ana Maria Souza
    FIM
    ```
    Output:
    ```
    miguel.silva@escola.com
    ana.souza@escola.com
    ana.souza2@escola.com
    ```

29. (Analisador de Texto) Receba uma frase. Passe tudo para minúsculas, remova a pontuação (`. , ! ?`) e ignore as palavras comuns `['o', 'a', 'de', 'e', 'que']`. Mostre o total de palavras restantes, o top 3 das mais frequentes (em caso de empate, vale a ordem em que apareceram) e a palavra mais longa.
    Input:
    ```
    O Miguel gosta de jogar! O Miguel gosta de programar, e o Miguel adora Python.
    ```
    Output:
    ```
    Total de palavras: 9
    Top 3: miguel (3), gosta (2), jogar (1)
    Mais longa: programar (9 letras)
    ```

30. (Mini-projeto: Jogo de Palavras) A palavra secreta é `livro`. A cada tentativa, o jogador digita uma palavra de 5 letras. Para cada letra da tentativa, mostre `V` se está na posição certa, `A` se existe na palavra secreta mas em outra posição e `X` se não existe. Palavras com tamanho errado não contam como tentativa. O jogo termina ao acertar ou após 6 tentativas. Organize o código em funções (por exemplo, `avaliar_tentativa(segredo, tentativa)`).
    Input:
    ```
    carro
    gato
    livro
    ```
    Output:
    ```
    carro -> XXAVV
    A palavra precisa ter 5 letras.
    livro -> VVVVV
    Parabéns! Você acertou em 2 tentativas.
    ```
