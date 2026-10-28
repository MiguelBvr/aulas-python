# Módulo 9 — Arquivos

## 1. Introdução Teórica e Prática

Até agora, tudo o que seu programa guardava em variáveis, listas e dicionários **sumia quando ele terminava**. Arquivos resolvem isso: são a **memória permanente** do programa. Pense no **save do seu jogo**: você desliga o console, volta no dia seguinte e continua de onde parou. Ou no **caderno de anotações**: o que você escreve fica lá, mesmo depois de fechá-lo.

Por que isso é útil?
- Salvar progresso, pontuações, configurações e listas de tarefas.
- Ler dados prontos (notas da turma, lista de compras, logs).
- Trocar informações com outros programas (como planilhas em formato `.csv`).
- Combina com tudo o que você já viu: strings, loops, listas, dicionários, funções e conjuntos.

### Os 3 modos principais de abrir um arquivo

| Modo | O que faz |
|------|-----------|
| `'r'` | **Ler** (read). O arquivo precisa existir. |
| `'w'` | **Escrever** (write). Cria o arquivo, ou **apaga tudo** se ele já existir! |
| `'a'` | **Acrescentar** (append). Escreve no final, sem apagar o que já existe. |

### Escrevendo com `with`

```python
# 'with' abre o arquivo e fecha sozinho no final (não precisa lembrar do close)
# encoding='utf-8' garante que acentos funcionem em qualquer computador
with open('recados.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Primeira linha\n')   # \n é a "tecla Enter": pula de linha
    arquivo.write('Segunda linha\n')
```

Dica: `write()` **não** pula linha sozinho (diferente do `print`). Você precisa colocar o `\n`.

### Lendo de 3 jeitos

```python
# 1) tudo de uma vez, como uma única string grande
with open('recados.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

# 2) como lista de linhas (cada uma termina com \n)
with open('recados.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

# 3) linha por linha com for (o mais usado!)
with open('recados.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        # strip() tira o \n do final, senão o print pula duas linhas
        print(linha.strip())
```

### Acrescentando sem apagar

```python
with open('recados.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Terceira linha\n')
```

### Guardando várias linhas de uma vez

```python
nomes = ['Ana', 'Beto', 'Cris']

with open('nomes.txt', 'w', encoding='utf-8') as arquivo:
    for nome in nomes:
        arquivo.write(nome + '\n')   # um nome por linha
```

### Arquivos CSV: uma "planilha" em texto

```python
# cada linha é um registro; os campos são separados por vírgula
# Conteúdo de alunos.csv:
#   nome,nota
#   Ana,8.5
#   Beto,6.0

notas = {}
with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        campos = linha.strip().split(',')   # split vira lista: ['Ana', '8.5']
        if campos[0] == 'nome':             # pula a linha de cabeçalho
            continue
        notas[campos[0]] = float(campos[1]) # texto -> número com float()
```

### E se o arquivo ainda não existir?

```python
import os   # "os" é uma ferramenta pronta do Python (módulos virão mais adiante)

# modo 'r' dá erro se o arquivo não existe; por isso, confira antes
if os.path.exists('save.txt'):
    print('Achei o save!')
else:
    print('Nenhum save ainda, vamos começar um jogo novo.')
```

Lembre-se: tudo que você lê de um arquivo chega como **string**. Se precisar de números, converta com `int()` ou `float()`.

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas, Dicionários, Funções, Strings, Tuplas e Conjuntos. Sempre que o enunciado falar de um arquivo de entrada, crie-o manualmente com o conteúdo indicado.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Crie o arquivo `ola.txt` contendo a frase `Olá, arquivo!` usando `with open(...)` e o modo `'w'`.
2. Leia o arquivo `ola.txt` com `read()` e mostre o conteúdo na tela.
3. Escreva 3 linhas diferentes em `lista.txt` (lembre-se do `\n`).
4. Leia somente a primeira linha de `lista.txt` com `readline()`.
5. Leia `lista.txt` com `readlines()` e mostre a lista resultante. Repare nos `\n`.
6. Percorra `lista.txt` com `for` e mostre cada linha sem espaços em branco extras (use `strip()`).
7. Acrescente uma nova linha em `lista.txt` com o modo `'a'`, sem apagar as anteriores.
8. Abra `lista.txt` com o modo `'w'` e escreva só uma linha. O que aconteceu com o conteúdo antigo? Explique em um comentário.
9. Conte quantas linhas tem o arquivo `lista.txt`.
10. Crie o arquivo `numeros.txt` com os números de 1 a 10, um por linha (use `for` e `range()`).
11. Dada a lista `['Ana', 'Beto', 'Cris']`, grave cada nome em uma linha do arquivo `nomes.txt`.
12. Leia `nomes.txt` e mostre quantos caracteres tem o conteúdo inteiro (com `len()`).
13. Depois de sair do bloco `with`, mostre o valor de `arquivo.closed`. O que ele indica?
14. Escreva a frase `Coração, ação e emoção` em `acentos.txt` com `encoding='utf-8'` e leia-a de volta.
15. Use `writelines()` para gravar a lista `['a\n', 'b\n', 'c\n']` em um arquivo e confira o resultado.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use arquivos junto com `for`/`while`, `if`/`else`, listas, dicionários, funções, strings, tuplas e conjuntos.

16. (Diário) Peça ao usuário uma frase e acrescente-a em `diario.txt`. Depois, mostre todas as entradas do diário numeradas (`1 - ...`, `2 - ...`).
17. (Notas da escola) O arquivo `notas.txt` tem uma nota por linha (ex.: `8.5`, `6`, `9`, `4.5`). Crie `calcular_media(notas)` e mostre a média e quantas notas são maiores ou iguais a 7.
18. (Contador de palavras) Leia um arquivo de texto e mostre o total de linhas, o total de palavras e as 3 palavras mais frequentes (ignore maiúsculas).
19. (Busca no texto) Leia uma palavra do usuário e mostre o número e o conteúdo de cada linha do arquivo em que ela aparece (sem diferenciar maiúsculas e minúsculas). Se não aparecer, avise.
20. (Limpeza) Copie para `limpo.txt` apenas as linhas **não vazias** de um arquivo, já sem espaços sobrando nas pontas.
21. (Inventário CSV) O arquivo `inventario.csv` tem linhas no formato `nome,quantidade`. Monte um dicionário e mostre os itens com menos de 3 unidades.
22. (Médias em CSV) O arquivo `alunos.csv` tem o cabeçalho `nome,nota1,nota2` e várias linhas de alunos. Gere `medias.csv` com o cabeçalho `nome,media` e a média de cada aluno.
23. (Texto numerado) Leia um arquivo e grave em `copia_maiusculas.txt` cada linha em maiúsculas e numerada, no formato `1: TEXTO DA LINHA`.
24. (Contador de visitas) Guarde em `visitas.txt` quantas vezes o programa já foi executado. A cada execução, leia o número (use `os.path.exists`; se o arquivo não existir, comece do zero), some 1, grave e mostre `Você é o visitante nº X`.
25. (Lista de tarefas persistente) Ao iniciar, carregue as tarefas de `tarefas.txt` (se existir) em um conjunto. Receba novas tarefas até o usuário digitar `SAIR`. Ao final, grave todas as tarefas no arquivo, sem repetidas e em ordem alfabética.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários, funções, strings, tuplas, conjuntos e arquivos. O Input e o Output esperados estão descritos.

26. (Salvar e Carregar Jogo) O personagem é um dicionário `{'nome': 'Miguel', 'nivel': 5, 'vida': 80, 'ouro': 120}`. Crie `salvar_jogo(personagem)`, que grava `save.txt` com uma linha `chave=valor` para cada item, e `carregar_jogo()`, que lê o arquivo e devolve o dicionário, convertendo `nivel`, `vida` e `ouro` para inteiros. O programa salva, carrega, dá 30 de ouro ao jogador, salva de novo e carrega mais uma vez.
    Input: o dicionário já está definido no programa.
    Output:
    ```
    Arquivo save.txt criado com 4 linhas
    Jogo carregado: Miguel, nível 5, vida 80, ouro 120
    Ganhou 30 de ouro! Jogo salvo novamente.
    Jogo carregado: Miguel, nível 5, vida 80, ouro 150
    ```

27. (Relatório da Turma) O arquivo `turma.csv` tem este conteúdo:
    ```
    nome,nota1,nota2,nota3
    Ana,8,9,7
    Beto,4,5,3
    Cris,6,7,5
    ```
    Leia o arquivo (ignorando o cabeçalho), calcule a média de cada aluno e a situação (`Aprovado` se >= 7, `Recuperação` se >= 5, `Reprovado` caso contrário). Mostre o relatório na tela e também grave tudo em `relatorio.txt`.
    Input: o arquivo `turma.csv` descrito acima.
    Output:
    ```
    Ana: 8.0 - Aprovado
    Beto: 4.0 - Reprovado
    Cris: 6.0 - Recuperação
    Aprovados: 1
    Média da turma: 6.0
    Relatório salvo em relatorio.txt
    ```

28. (Analisador de Log) O arquivo `servidor.log` tem este conteúdo, e a primeira palavra de cada linha é o nível da mensagem:
    ```
    INFO login Ana
    ERRO falha_banco
    INFO login Beto
    AVISO disco_cheio
    ERRO timeout
    INFO logout Ana
    ```
    Conte quantas mensagens existem de cada nível usando um dicionário e grave em `erros.txt` somente as linhas de nível `ERRO`.
    Input: o arquivo `servidor.log` descrito acima.
    Output:
    ```
    INFO: 3
    ERRO: 2
    AVISO: 1
    Erros salvos em erros.txt (2 linhas)
    ```

29. (Agenda de Contatos Persistente) Guarde os contatos em `contatos.txt`, uma linha por contato no formato `nome;telefone`. Ao iniciar, carregue o arquivo em um dicionário (se ele existir). O programa lê comandos até `SAIR`: `ADICIONAR nome telefone`, `BUSCAR nome`, `REMOVER nome` e `LISTAR` (em ordem alfabética). Ao sair, grave todos os contatos no arquivo. Organize o código em funções.
    Input (primeira execução, arquivo ainda não existe):
    ```
    ADICIONAR Ana 9999
    ADICIONAR Beto 8888
    SAIR
    ```
    Output:
    ```
    Contato adicionado: Ana
    Contato adicionado: Beto
    2 contato(s) salvo(s).
    ```
    Input (segunda execução, mesmo arquivo):
    ```
    LISTAR
    REMOVER Ana
    BUSCAR Ana
    SAIR
    ```
    Output:
    ```
    Ana - 9999
    Beto - 8888
    Contato removido: Ana
    Contato não encontrado: Ana
    1 contato(s) salvo(s).
    ```

30. (Mini-projeto: Ranking Persistente) O arquivo `ranking.csv` tem este conteúdo (sem cabeçalho):
    ```
    Ana,120
    Beto,90
    Cris,150
    Davi,110
    Eva,70
    ```
    O programa lê o ranking em um dicionário e depois lê resultados de partidas no formato `nome pontos` até `FIM`. Se o jogador já existe, só atualiza a pontuação quando ela for maior que o recorde dele. Se é novo, entra no ranking. Ao final, monte uma lista de tuplas `(pontos, nome)`, ordene do maior para o menor, mantenha só os **5 primeiros** e grave de volta em `ranking.csv`, no mesmo formato.
    Input:
    ```
    Beto 130
    Eva 50
    Fabi 100
    FIM
    ```
    Output:
    ```
    Beto: novo recorde! (130)
    Eva: não superou o recorde (70)
    Fabi: entrou no ranking (100)
    Ranking final:
    1º Cris - 150
    2º Beto - 130
    3º Ana - 120
    4º Davi - 110
    5º Fabi - 100
    ranking.csv atualizado.
    ```
