# Módulo 11 — Módulos e Bibliotecas

## 1. Introdução Teórica e Prática

Você não precisa construir tudo do zero. O Python vem com uma **caixa de ferramentas gigante** de códigos prontos, chamados **módulos** (e um conjunto de módulos forma uma **biblioteca**). É como o **mod de um jogo**: alguém já programou novos itens e você só instala e usa. Para sortear números, calcular raízes ou mexer com datas, basta **importar** o módulo certo.

Por que isso é útil?
- Poupa tempo: em vez de inventar a roda, você usa código já testado.
- Deixa os jogos mais divertidos (dados, sorteios, cronômetros).
- Organiza projetos grandes em vários arquivos pequenos, cada um com uma função clara.
- Dá acesso a bibliotecas de outras pessoas, instaladas com `pip`.
- Combina com tudo o que você já viu: loops, `if`, listas, dicionários, funções, strings, arquivos e tratamento de erros.

### Importando: 3 jeitos

```python
import math                  # traz o módulo inteiro; use math.nome
print(math.sqrt(16))         # 4.0

from math import sqrt, pi    # traz só o que você quer, sem prefixo
print(sqrt(25), pi)

import math as m             # apelido, para digitar menos
print(m.floor(3.9))          # 3
```

Dica: use `help(math)` ou `dir(math)` para ver tudo o que o módulo oferece.

### random: sorteios e sorte

```python
import random

print(random.randint(1, 6))           # inteiro de 1 a 6 (um dado!)
print(random.random())                # decimal entre 0 e 1
print(random.uniform(1.5, 3.5))       # decimal entre 1.5 e 3.5

herois = ['Naruto', 'Goku', 'Luffy', 'Ichigo']
print(random.choice(herois))          # escolhe um item
print(random.sample(herois, 2))       # escolhe 2 itens diferentes
random.shuffle(herois)                # embaralha a própria lista (não devolve nada)
```

### math: matemática pronta

```python
import math

print(math.sqrt(144))        # 12.0 -> raiz quadrada
print(math.pi)               # 3.14159...
print(math.ceil(7.2))        # 8 -> arredonda para cima
print(math.floor(7.8))       # 7 -> arredonda para baixo
print(math.factorial(5))     # 120 -> 5 * 4 * 3 * 2 * 1
print(math.hypot(3, 4))      # 5.0 -> distância/hipotenusa
```

### datetime: datas e horas

```python
from datetime import date, datetime, timedelta

hoje = date.today()
print(hoje.strftime('%d/%m/%Y'))       # formata a data: 28/10/2026

agora = datetime.now()
print(agora.strftime('%H:%M'))         # hora e minuto

# transformar texto em data (strptime) -> dá ValueError se o texto for inválido
nascimento = datetime.strptime('15/03/2010', '%d/%m/%Y').date()

# subtrair datas devolve um objeto com .days
dias_de_vida = (hoje - nascimento).days

# somar dias
daqui_a_7_dias = hoje + timedelta(days=7)
print(hoje.year, hoje.month, hoje.day)
```

### time e statistics

```python
import time
import statistics

inicio = time.time()
time.sleep(1)                           # pausa por 1 segundo
print('Demorou', round(time.time() - inicio, 1), 'segundos')

notas = [8, 6.5, 9, 7]
print(statistics.mean(notas))           # média
print(statistics.median(notas))         # mediana (valor do meio)
```

### json: guardando dicionários em arquivos

```python
import json

jogador = {'nome': 'Miguel', 'nivel': 5, 'itens': ['espada', 'escudo']}

# salvar (ensure_ascii=False mantém os acentos)
with open('save.json', 'w', encoding='utf-8') as arquivo:
    json.dump(jogador, arquivo, indent=4, ensure_ascii=False)

# carregar de volta: vira dicionário de novo, com os tipos certos (inteiro, lista...)
with open('save.json', 'r', encoding='utf-8') as arquivo:
    jogador = json.load(arquivo)
```

### Criando o seu próprio módulo

Qualquer arquivo `.py` é um módulo! Se você criar o arquivo `utilidades.py`:

```python
# utilidades.py
def eh_par(numero):
    return numero % 2 == 0

# esse bloco só roda quando você executa ESTE arquivo diretamente,
# e não quando outro arquivo importa o módulo
if __name__ == '__main__':
    print(eh_par(4))   # teste rápido
```

Em outro arquivo, **na mesma pasta**, você importa:

```python
# principal.py
import utilidades

print(utilidades.eh_par(10))   # True
```

### Bibliotecas de outras pessoas: o pip

```text
# no terminal (de preferência dentro de um ambiente virtual)
python -m venv venv                # cria o ambiente isolado do projeto
source venv/bin/activate           # ativa (Windows: venv\Scripts\activate)
pip install colorama               # instala uma biblioteca
```

```python
# depois de instalada, é só importar
from colorama import Fore, init

init()   # garante que as cores funcionem também no Windows
print(Fore.GREEN + 'Acertou!' + Fore.RESET)
```

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas, Dicionários, Funções, Strings, Tuplas e Conjuntos, Arquivos e Tratamento de Erros. Em exercícios com sorteios, os resultados mudam a cada execução; os exemplos de saída mostram só o formato.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Use `random.randint()` para simular o lançamento de um dado de 6 lados e mostre o resultado.
2. Dada a lista `['maçã', 'banana', 'uva']`, mostre uma fruta sorteada com `random.choice()`.
3. Embaralhe a lista `[1, 2, 3, 4, 5]` com `random.shuffle()` e mostre-a.
4. Sorteie 3 itens diferentes de uma lista de 6 nomes com `random.sample()`.
5. Mostre um número decimal sorteado entre 1 e 10 com `random.uniform()`.
6. Use `math.sqrt()` para mostrar a raiz quadrada de `144`.
7. Calcule a área de um círculo de raio `5` (`math.pi * raio ** 2`) e mostre com 2 casas decimais.
8. Mostre `math.ceil()` e `math.floor()` do número `7.3`.
9. Calcule o fatorial de `5` com `math.factorial()`.
10. Importe só `sqrt` e `floor` com `from math import ...` e use-os sem o prefixo `math.`.
11. Importe `math` com o apelido `m` (`import math as m`) e calcule `m.sqrt(81)`.
12. Mostre a data de hoje no formato `dd/mm/aaaa` com `date.today()` e `strftime()`.
13. Mostre a hora atual no formato `HH:MM` com `datetime.now()`.
14. Crie a data `25/12/2025` com `date(2025, 12, 25)` e mostre o ano, o mês e o dia separadamente.
15. Use `statistics.mean()` e `statistics.median()` na lista `[8, 6.5, 9, 7, 5]`.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use módulos junto com `for`/`while`, `if`/`else`, listas, dicionários, funções, strings, tuplas, conjuntos, arquivos e tratamento de erros.

16. (Dado de RPG) Crie `rolar_dado(lados)`. Role um dado de 6 lados 20 vezes e use um dicionário para contar quantas vezes saiu cada face. Mostre a face mais sorteada.
17. (Amigo secreto) Dada uma lista de nomes, embaralhe-a e faça cada pessoa tirar a próxima da fila (a última tira a primeira). Mostre os pares `fulano -> sorteado`. Ninguém pode tirar a si mesmo.
18. (Adivinhe o número) O computador sorteia um número de 1 a 100. O jogador chuta até acertar, recebendo as dicas `maior` ou `menor`. Trate entradas que não são números e mostre o número de tentativas no final.
19. (Geometria) Crie `area_circulo(raio)`, `perimetro_circulo(raio)` e `distancia(p1, p2)`, em que `p1` e `p2` são tuplas `(x, y)` (use `math.sqrt` ou `math.hypot`). Teste com valores diferentes.
20. (Idade exata) Leia uma data de nascimento no formato `dd/mm/aaaa` com `datetime.strptime()` e mostre a idade em anos e quantos dias de vida a pessoa já tem. Se a data for inválida, peça de novo.
21. (Contagem regressiva) Mostre quantos dias faltam para o dia 31/12 do ano atual. Se a data já passou, calcule para o ano seguinte.
22. (Gerador de senhas) Crie `gerar_senha(tamanho)` que sorteia caracteres de uma string com letras, números e símbolos. Repita o sorteio até a senha ter pelo menos uma letra maiúscula e um número. Gere 5 senhas de tamanho 10.
23. (Estatísticas da turma) Dada uma lista de notas, mostre a média, a mediana, o desvio padrão (`statistics.stdev`), a maior e a menor nota, e quantas notas estão acima da média.
24. (Meu primeiro módulo) Crie o arquivo `utilidades.py` com as funções `eh_par(n)`, `media(lista)` e `saudacao(nome)`, e um bloco `if __name__ == '__main__':` com testes rápidos. Depois crie `principal.py`, importe o módulo e use as funções.
25. (Instalando uma biblioteca) Em um ambiente virtual, instale a biblioteca `colorama` com `pip install colorama`. Pegue o jogo do exercício 18 e mostre as dicas de `maior` e `menor` em vermelho e o acerto em verde.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários, funções, strings, tuplas, conjuntos, arquivos, tratamento de erros e módulos. O Input e o Output esperados estão descritos.

26. (Torneio de Dados) O jogador e o computador jogam 3 rodadas. Em cada rodada, cada um rola dois dados de 6 lados (`random.randint`) e vence quem tiver a maior soma (empate não pontua). O jogador pressiona ENTER para rolar. No final, mostre o placar e quem ganhou o torneio. Organize o código em funções.
    Input: ENTER em cada rodada.
    Output (exemplo, os números variam):
    ```
    Rodada 1 - Você: 4 + 6 = 10 | Computador: 2 + 3 = 5 -> Você ganhou
    Rodada 2 - Você: 1 + 2 = 3 | Computador: 5 + 5 = 10 -> Computador ganhou
    Rodada 3 - Você: 6 + 3 = 9 | Computador: 4 + 5 = 9 -> Empate
    Placar final: Você 1 x 1 Computador
    O torneio terminou empatado!
    ```

27. (Calendário de Aniversários) O programa recebe a data de "hoje" digitada pelo usuário (para facilitar a conferência) e um dicionário `{nome: data de nascimento}`. Para cada pessoa, mostre a idade e quantos dias faltam para o próximo aniversário, em ordem do mais próximo para o mais distante. Se hoje for o aniversário, mostre `Hoje é aniversário!`.
    Input:
    ```
    Hoje: 10/03/2025
    Ana: 15/03/2010
    Beto: 02/03/2009
    Cris: 10/03/2012
    ```
    Output:
    ```
    Cris: 13 anos - Hoje é aniversário!
    Ana: 14 anos - faltam 5 dias
    Beto: 16 anos - faltam 357 dias
    ```

28. (Quiz de Matemática Cronometrado) O programa gera 5 perguntas aleatórias de soma, subtração ou multiplicação com números de 1 a 10 (`random.randint` e `random.choice`). Trate respostas que não são números (a pergunta não é perdida). Use `time.time()` para medir o tempo total. Guarde o melhor resultado (mais acertos e, em caso de empate, menos tempo) em `recorde.json` e avise quando houver um novo recorde.
    Input: as respostas do jogador.
    Output (exemplo, os valores variam):
    ```
    Pergunta 1: 7 + 3 = 10
    Correto!
    Pergunta 2: 4 * 6 = abc
    Digite apenas números.
    Pergunta 2: 4 * 6 = 24
    Correto!
    ...
    Acertos: 4/5 | Tempo: 18.3 segundos
    Novo recorde! Salvo em recorde.json
    ```

29. (Agenda de Provas) O programa recebe a data de "hoje" e depois lê comandos até `FIM`: `ADICIONAR dd/mm/aaaa descrição` e `LISTAR`. Datas inválidas (como `31/02/2025`) e datas que já passaram devem ser recusadas com mensagens diferentes. A listagem mostra os compromissos em ordem de data e quantos dias faltam. Ao final, grave tudo em `agenda.json`.
    Input:
    ```
    Hoje: 20/10/2025
    ADICIONAR 25/10/2025 Prova de Matemática
    ADICIONAR 22/10/2025 Trabalho de História
    ADICIONAR 15/10/2025 Prova de Ciências
    ADICIONAR 31/02/2025 Teste
    LISTAR
    FIM
    ```
    Output:
    ```
    Compromisso adicionado: 25/10/2025
    Compromisso adicionado: 22/10/2025
    Erro: essa data já passou
    Erro: data inválida
    22/10/2025 - Trabalho de História (faltam 2 dias)
    25/10/2025 - Prova de Matemática (faltam 5 dias)
    ```

30. (Mini-projeto: Aventura em Vários Arquivos) Crie um projeto com 3 arquivos na mesma pasta:
    - `personagem.py`: funções `novo_personagem(nome)`, `salvar(personagem)` e `carregar()` usando `save.json`. `carregar()` devolve `None` se o arquivo não existir ou estiver corrompido.
    - `batalha.py`: função `lutar(heroi, monstro)` que roda os turnos. O herói causa `random.randint(5, 15)` de dano e o monstro causa `random.randint(3, 10)`. Retorna `True` se o herói vencer.
    - `main.py`: carrega o save (ou cria um novo herói com `vida` 100 e `ouro` 0), sorteia 3 monstros da lista `[('Slime', 20), ('Goblin', 35), ('Dragão', 60)]` (tuplas `(nome, vida)`, sem repetir), luta contra cada um, ganha ouro igual à vida do monstro derrotado e salva após cada luta. Se a vida do herói chegar a zero, o jogo termina.
    Input: o nome do herói (só se não houver save).
    Output (exemplo, os valores variam):
    ```
    Nenhum save encontrado. Novo jogo iniciado!
    Nome do herói: Miguel
    Um Slime selvagem apareceu!
    Você causou 12 de dano. Slime: 8 de vida
    Slime causou 5 de dano. Você: 95 de vida
    Você causou 9 de dano. Slime: 0 de vida
    Slime derrotado! +20 de ouro
    Jogo salvo em save.json
    ...
    Fim da aventura! Ouro total: 55
    ```
