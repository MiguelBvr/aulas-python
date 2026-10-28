# Módulo 6 — Funções

## 1. Introdução Teórica e Prática

Uma função é um **bloco de código com nome** que você escreve uma vez e usa quantas vezes quiser. Pense em um **combo especial de um personagem de jogo**: você aperta uma combinação de botões e o personagem executa vários golpes em sequência. Ou nos **atalhos do celular**: um toque e o aparelho faz várias coisas sozinho.

Por que isso é útil?
- Evita repetir o mesmo código várias vezes (menos copiar e colar, menos bugs).
- Deixa o programa organizado: cada função resolve um pedacinho do problema.
- Facilita testar e consertar: se algo der errado, você sabe onde procurar.
- Combina com tudo o que você já aprendeu: variáveis, `if`, loops, listas e dicionários.

### Criando e chamando uma função

```python
# "def" cria a função; o nome deve dizer o que ela faz
def saudacao():
    print('Fala, jogador!')

# a função só roda quando você a CHAMA (usa os parênteses)
saudacao()
saudacao()  # pode chamar quantas vezes quiser
```

### Parâmetros: dando "ingredientes" para a função

```python
# 'nome' é um parâmetro: um espaço reservado para o valor que vier de fora
def saudar(nome):
    print('Fala,', nome, '!')

saudar('Miguel')  # 'Miguel' é o argumento (o valor real enviado)
saudar('Ana')
```

### Return: a função devolve um resultado

```python
# return entrega um valor para quem chamou a função
def dobro(numero):
    return numero * 2

resultado = dobro(7)  # resultado guarda 14
print(resultado)
```

### print x return (cuidado com essa confusão!)

```python
def mostra_dobro(n):
    print(n * 2)       # só mostra na tela, não devolve nada

def calcula_dobro(n):
    return n * 2       # devolve o valor, que você pode guardar e reutilizar

x = mostra_dobro(5)    # x vale None (nada)
y = calcula_dobro(5)   # y vale 10
```

### Valor padrão

```python
# se ninguém informar o bônus, ele vale 0
def pontuacao_final(pontos, bonus=0):
    return pontos + bonus

print(pontuacao_final(100))      # 100
print(pontuacao_final(100, 50))  # 150
```

### Variáveis locais: o que acontece na função, fica na função

```python
def criar_item():
    item = 'espada'   # 'item' só existe dentro da função
    return item

espada = criar_item()  # para usar fora, devolva com return
```

### Funções com listas e dicionários

```python
# a função varre a lista com for e usa if para decidir
def contar_aprovados(notas):
    total = 0
    for nota in notas:
        if nota >= 7:
            total += 1
    return total

print(contar_aprovados([8, 5, 9.5, 6]))  # 2

# dicionário como parâmetro
def mostrar_ficha(jogador):
    for chave, valor in jogador.items():
        print(chave, '->', valor)
```

### Uma função chamando outra

```python
def eh_par(n):
    return n % 2 == 0

def contar_pares(lista):
    total = 0
    for n in lista:
        if eh_par(n):   # reaproveita a função que já existe
            total += 1
    return total
```

### Documentando com docstring

```python
def dobro(numero):
    """Devolve o dobro do número recebido."""
    return numero * 2
```

Dica: dê nomes que expliquem o que a função faz (`calcular_media` é melhor que `cm`). Uma função deve fazer **uma coisa só**.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas e Dicionários.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Crie uma função `ola_mundo()` que imprime `Olá, mundo!` e chame-a 3 vezes.
2. Crie uma função `cumprimentar(nome)` que imprime `Olá, <nome>!`.
3. Crie uma função `somar(a, b)` que imprime a soma de dois números.
4. Crie uma função `dobro(n)` que **retorna** o dobro de `n` e mostre o resultado com `print()`.
5. Crie uma função `eh_par(n)` que retorna `True` se `n` for par e `False` caso contrário.
6. Crie uma função `apresentar(nome, idade=15)` com valor padrão para a idade. Chame-a com e sem o segundo argumento.
7. Chame a função `somar(a, b)` usando argumentos nomeados, em ordem trocada: `somar(b=2, a=5)`.
8. Crie uma função `maior(a, b)` que retorna o maior dos dois números (sem usar `max()`).
9. Crie uma função que apenas imprime um valor (sem `return`), guarde a chamada em uma variável e mostre o que ela contém. O que apareceu?
10. Crie uma variável dentro de uma função e tente imprimi-la fora dela. Observe o erro e explique, em um comentário, por que ele acontece.
11. Crie uma função `mostrar_lista(lista)` que imprime cada item da lista, um por linha.
12. Crie uma função `somar_lista(lista)` que retorna a soma de todos os itens (sem usar `sum()`).
13. Crie uma função `mostrar_ficha(personagem)` que recebe um dicionário e imprime cada par no formato `chave: valor`.
14. Crie as funções `dobro(n)` e `quadruplo(n)`, sendo que `quadruplo` deve chamar `dobro` duas vezes.
15. Crie uma função com uma docstring de uma linha e use `help(nome_da_funcao)` para vê-la.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use funções junto com `for`/`while`, `if`/`else`, listas, dicionários e os tipos de dados adequados.

16. (Dano no jogo) Crie `calcular_dano(ataque, defesa)`: se o ataque for maior que a defesa, retorna a diferença; senão, retorna `1`. Use um loop para testar a lista de ataques `[15, 4, 9, 30]` contra uma defesa de `10`.
17. (Notas da escola) Crie `calcular_media(notas)` e `situacao(media)` (`Aprovado` se >= 7, `Recuperação` se >= 5, `Reprovado` caso contrário). Dado o dicionário `turma = {'Ana': [8, 9, 7], 'Beto': [4, 5, 3], 'Cris': [6, 7, 5]}`, mostre a média e a situação de cada aluno.
18. (Rede social) Crie `usuario_valido(nome)`: o nome precisa ter entre 3 e 15 caracteres e não pode conter espaços. Use a função para filtrar a lista `['ana', 'jo', 'miguel gamer', 'beto10', 'x']` e mostre só os válidos.
19. (Pares e ímpares) Crie `separar_pares(lista)` que retorna uma nova lista só com os números pares. Teste com os números de 1 a 20 gerados por `range()`.
20. (Conversor de temperatura) Crie `celsius_para_fahrenheit(c)` (fórmula: `c * 9 / 5 + 32`). Mostre uma tabela de 0 a 100 °C, de 10 em 10.
21. (Números primos) Crie `eh_primo(n)` e use-a para mostrar todos os primos de 1 a 50.
22. (Inventário RPG) Crie `adicionar_item(inventario, nome, qtd)` que recebe um dicionário: se o item já existe, soma a quantidade; senão, cria o item. Adicione `pocao`, `espada`, `pocao` e mostre o inventário.
23. (Contador de palavras) Crie `contar_palavras(frase)` que retorna um dicionário com quantas vezes cada palavra aparece (ignore maiúsculas e minúsculas).
24. (Loja virtual) Dado `precos = {'pocao': 10, 'espada': 50, 'escudo': 35}`, crie `calcular_total(carrinho, precos)` que recebe uma lista de itens e retorna o total. Itens que não existem na loja devem ser avisados e ignorados. Se o total passar de 100 moedas, aplique 10% de desconto.
25. (Entrada segura) Crie `ler_inteiro_positivo(mensagem)` que usa `while` para pedir um número até o usuário digitar um inteiro maior que zero (use `isdigit()` para checar). Depois use a função para ler a idade e a quantidade de vidas de um jogador.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários e funções. Divida o problema em funções pequenas, cada uma com uma única tarefa. O Input e o Output esperados estão descritos.

26. (Batalha de RPG) O herói tem `vida 50`, `ataque 12` e `defesa 3`. O monstro tem `vida 40`, `ataque 9` e `defesa 2`. Cada um é um dicionário. Crie as funções `calcular_dano(atacante, defensor)` (mínimo de 1), `atacar(atacante, defensor)` (reduz a vida do defensor, sem deixar abaixo de 0) e `esta_vivo(personagem)`. Os dois atacam em turnos, começando pelo herói, até alguém ser derrotado.
    Input: os dicionários já estão definidos no programa.
    Output:
    ```
    Turno 1: Herói causa 10 de dano. Monstro: 30 de vida
    Turno 1: Monstro causa 6 de dano. Herói: 44 de vida
    Turno 2: Herói causa 10 de dano. Monstro: 20 de vida
    Turno 2: Monstro causa 6 de dano. Herói: 38 de vida
    Turno 3: Herói causa 10 de dano. Monstro: 10 de vida
    Turno 3: Monstro causa 6 de dano. Herói: 32 de vida
    Turno 4: Herói causa 10 de dano. Monstro: 0 de vida
    Monstro derrotado! Vitória do Herói em 4 turnos.
    ```

27. (Medidor de Senha) Crie as funções `tem_tamanho(senha)` (pelo menos 8 caracteres), `tem_numero(senha)`, `tem_maiuscula(senha)` e `tem_simbolo(senha)` (algum caractere de `!@#$%`). Crie também `forca_da_senha(senha)`, que conta quantas regras foram cumpridas: 0 ou 1 é `Fraca`, 2 ou 3 é `Média` e 4 é `Forte`. O programa lê senhas até o usuário digitar `FIM`.
    Input:
    ```
    abc
    Python123
    Python123!
    FIM
    ```
    Output:
    ```
    abc -> Fraca
    Python123 -> Média
    Python123! -> Forte
    ```

28. (Banco do Jogo) Guarde as contas em um dicionário `{nome: saldo}`. Crie as funções `criar_conta(contas, nome, saldo)`, `sacar(contas, nome, valor)`, `depositar(contas, nome, valor)` e `transferir(contas, origem, destino, valor)`. Valide se a conta existe e se há saldo suficiente. O programa lê comandos até `FIM`.
    Input:
    ```
    CRIAR Ana 100
    CRIAR Beto 50
    TRANSFERIR Ana Beto 30
    SACAR Beto 100
    SALDO Ana
    FIM
    ```
    Output:
    ```
    Conta criada: Ana (100)
    Conta criada: Beto (50)
    Transferência de 30 de Ana para Beto realizada
    Saldo insuficiente para Beto
    Saldo de Ana: 70
    ```

29. (Relatório da Turma) Dado `turma = {'Ana': [8, 9, 7], 'Beto': [4, 5, 3], 'Cris': [6, 7, 5]}`, crie as funções `calcular_media(notas)`, `situacao(media)`, `gerar_boletim(turma)` (retorna um dicionário `{nome: media}`) e `melhor_aluno(boletim)`. Mostre cada aluno com a média e a situação, a quantidade de aprovados e o melhor aluno.
    Input: o dicionário já está definido no programa.
    Output:
    ```
    Ana: média 8.0 - Aprovado
    Beto: média 4.0 - Reprovado
    Cris: média 6.0 - Recuperação
    Aprovados: 1
    Melhor aluno: Ana (8.0)
    ```

30. (Mini-projeto: Jogo da Forca) A palavra secreta é `python` e o jogador começa com 6 vidas. Crie funções como `mostrar_palavra(secreta, acertos)` (mostra as letras já descobertas e `_` nas demais), `letra_valida(letra, tentativas)` (uma só letra e ainda não tentada), `jogar_rodada(...)` e `venceu(secreta, acertos)`. Use uma lista para as letras tentadas, e o `while` termina quando o jogador vence ou perde todas as vidas.
    Input (uma letra por linha):
    ```
    p
    z
    y
    t
    h
    o
    n
    ```
    Output:
    ```
    Palavra: p _ _ _ _ _  | Vidas: 6
    Letra 'z' não está na palavra.
    Palavra: p _ _ _ _ _  | Vidas: 5
    Palavra: p y _ _ _ _  | Vidas: 5
    Palavra: p y t _ _ _  | Vidas: 5
    Palavra: p y t h _ _  | Vidas: 5
    Palavra: p y t h o _  | Vidas: 5
    Palavra: p y t h o n  | Vidas: 5
    Você venceu! A palavra era python.
    ```
