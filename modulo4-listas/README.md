# Módulo 4 — Listas

## 1. Introdução Teórica e Prática

Listas são coleções ordenadas de valores — pense nelas como uma playlist de músicas, a mochila do seu personagem num jogo ou a sua lista de amigas/os nas redes sociais: você guarda itens em uma ordem, pode adicionar, remover, consultar e percorrer cada item.

Por que isso é útil?
- Organizar dados relacionados (ex: notas da escola, inventário de jogo, sequência de passos).
- Permite automatizar tarefas repetitivas com loops (ex: conferir cada item da lista).
- Junta bem com variáveis e condicionais para tomar decisões sobre grupos de itens.

Exemplos rápidos (leia os comentários):

```python
# criar uma lista de frutas
frutas = ['maçã', 'banana', 'uva']

# acessar por índice (0 é o primeiro)
primeira = frutas[0]  # 'maçã'

# adicionar um item no final
frutas.append('laranja')

# tamanho da lista
quantidade = len(frutas)

# percorrer com for
for fruta in frutas:
    print('Eu gosto de', fruta)

# usar if dentro do loop
for f in frutas:
    if f == 'banana':
        print('Achei banana — vamos fazer vitamina!')
```

Dica: listas podem guardar números, textos e até outras listas (listas aninhadas). Use slices para pegar sublistas: `lista[1:3]` pega do índice 1 até 2.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais e Loops.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Crie uma lista chamada `cores` com 5 cores e imprima-a.
2. Acesse e mostre o primeiro e o último item de uma lista `animais`.
3. Adicione um novo elemento a uma lista vazia chamada `tarefas`.
4. Remova um item específico de uma lista `amigos` usando `remove()`.
5. Use `len()` para mostrar quantos itens tem a lista `frutas`.
6. Substitua o segundo item de `notas` por um novo valor.
7. Crie uma lista de números e calcule a soma usando um loop `for`.
8. Inverta a ordem de uma lista `mensagens` (não usar `reversed()` — experimente slicing).
9. Faça um slice que pegue os 3 primeiros elementos de `playlist`.
10. Verifique se o item `'chave'` está dentro da lista `objetos` (use `in`).
11. Copie uma lista `origem` para `copia` sem usar o mesmo objeto (ou seja, crie uma cópia independente).
12. Una duas listas `a` e `b` em uma só lista `ab`.
13. Conte quantas vezes um elemento aparece em `valores` (use `count`).
14. Limpe todos os itens de uma lista `caixa` (use `clear`).
15. Substitua os últimos dois itens de uma lista por uma lista nova (use slicing para atribuir).

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: exija o uso de `for`/`while` e `if`/`else` e tipos adequados.

16. (História) Você tem uma lista `inventario = ['espada','pocao','escudo','moeda']`. Escreva um loop que mostre só os itens que não são `'moeda'`.
17. (Notas) Dada uma lista de notas (floats), crie um programa que conte quantas notas são acima de 7.0.
18. (Rede social) Dada uma lista de nomes `usuarios`, remova todos os nomes com menos de 4 caracteres (modifique a lista original).
19. (Jogo) Crie uma lista de vidas com números inteiros; reduza a vida do jogador em 1 a cada iteração até chegar a zero e pare o loop.
20. (Filtro) Dada uma lista de números, crie outra lista somente com os números pares (use loop e condicional).
21. (Escola) Dada uma lista de tuplas `alunos = [('Ana',8.5),('Beto',6.7),('Cris',9.0)]`, produza uma nova lista com os nomes dos aprovados (nota >= 7.0).
22. (Inventário RPG) Você tem uma lista de dicionários simplificada: `itens = [{'nome':'pocao','qtd':3},{'nome':'espada','qtd':1}]`. Use loops e condicionais para somar a quantidade total de itens.
23. (Transformação) Receba uma lista de strings que representam números, converta para ints e calcule a média.
24. (Busca) Implemente uma função que recebe uma lista e um valor e retorna o índice do valor ou `-1` se não existir (não use `index()` direto — pratique o loop).
25. (Limpeza) Dada uma lista com strings que podem ter espaços extras, crie uma nova lista com as strings limpas (use `strip()` em cada item).

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops e listas. Para cada exercício, mostre claramente o que o programa deve receber (Input) e o que deve mostrar (Output).

26. (Gerenciador de Tarefas) Crie um programa que receba tarefas (strings) até o usuário digitar `'SAIR'`. Depois mostre:
    - Quantas tarefas foram adicionadas.
    - A lista de tarefas ordenada alfabeticamente.
    Input: entradas de tarefas uma por linha até `'SAIR'`.
    Output: número total e lista ordenada.

27. (Inventário Dinâmico) Simule um inventário onde o usuário informa comandos `ADICIONAR nome qtd`, `REMOVER nome qtd` e `FIM`. Use uma lista de dicionários ou duas listas paralelas. Ao final, mostre um resumo com itens e quantidades.
    Input: várias linhas com comandos até `FIM`.
    Output: lista de itens com quantidades finais.

28. (Notas e Estatísticas) Receba notas (float) até o usuário enviar uma linha vazia. Calcule e mostre: média, maior nota, menor nota e quantas notas ficaram abaixo da média.
    Input: várias notas, uma por linha; linha vazia encerra.
    Output: média, maior, menor, contagem abaixo da média.

29. (Ranking de Jogo) Dada uma lista de resultados onde cada item é um dicionário `{'nome':str,'pontos':int}`, ordene pelo score e mostre o top 3. Se houver empate, mantenha a ordem de chegada.
    Input: lista de dicionários já carregada no programa.
    Output: top 3 jogadores com pontuações.

30. (Mini-projeto: Rede Social Simples) Crie um mini-programa que gerencia posts: cada post é uma string em uma lista. Deve permitir comandos: `POST texto` (adiciona no início), `DELETE índice`, `LISTAR`. No final, salve os posts em um arquivo `posts.txt` (uma linha por post).
    Input: comandos do usuário até `SAIR`.
    Output: estado final da lista de posts e arquivo `posts.txt` criado.

---

Boa sorte! Lembre-se: tente primeiro na sua cabeça, depois no código. Use comentários para explicar cada passo como se estivesse ensinando um colega.
