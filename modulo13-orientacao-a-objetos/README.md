# Módulo 13 — Orientação a Objetos (POO)

## 1. Introdução Teórica e Prática

Até agora, você guardava os dados de um personagem em um dicionário e criava funções separadas para mexer nele. Na **Orientação a Objetos**, você junta **os dados e as ações no mesmo lugar**. Pense em um **molde de personagem de RPG**: o molde (a **classe**) define que todo personagem tem nome, vida e ataque, e que ele sabe atacar e se curar. Cada personagem criado a partir do molde (um **objeto**) tem seus próprios valores.

Por que isso é útil?
- Organiza programas grandes: cada coisa do mundo (jogador, conta, livro) vira uma classe.
- Dados e ações ficam juntos, então é mais difícil errar.
- Permite reaproveitar código com herança (um Mago é um tipo de Personagem).
- É o jeito como jogos, apps e sistemas de verdade são construídos.
- Combina com tudo o que você já viu: loops, `if`, listas, dicionários, funções, strings, arquivos, erros, módulos e comprehensions.

### Classe e objeto

```python
class Jogador:
    # __init__ roda sozinho quando você cria um objeto: é o "montador" da ficha
    # self é "o próprio objeto"; sempre vem como primeiro parâmetro
    def __init__(self, nome, vida=100):
        self.nome = nome    # atributos: os dados do objeto
        self.vida = vida

    # métodos: as ações do objeto (funções dentro da classe)
    def receber_dano(self, dano):
        self.vida = max(self.vida - dano, 0)   # vida nunca fica negativa

    def esta_vivo(self):
        return self.vida > 0

# criando objetos (instâncias) a partir do molde
p1 = Jogador('Miguel')
p2 = Jogador('Ana', vida=80)

p1.receber_dano(30)
print(p1.vida)         # 70 -> só o p1 mudou
print(p2.vida)         # 80 -> objetos são independentes
print(p1.esta_vivo())  # True
```

### __str__: como o objeto aparece no print

```python
class Jogador:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    # sem isso, print(jogador) mostra algo como <Jogador object at 0x...>
    def __str__(self):
        return f'{self.nome} ({self.vida} de vida)'

print(Jogador('Miguel'))   # Miguel (100 de vida)
```

### Atributo de classe: compartilhado por todos

```python
class Monstro:
    total = 0                 # pertence à classe, não a um objeto específico

    def __init__(self, nome):
        self.nome = nome
        Monstro.total += 1    # conta quantos monstros já foram criados

Monstro('Slime')
Monstro('Goblin')
print(Monstro.total)          # 2
```

### Objetos dentro de objetos e listas de objetos

```python
class Item:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Mochila:
    def __init__(self):
        self.itens = []       # uma lista de objetos Item

    def adicionar(self, item):
        self.itens.append(item)

    def valor_total(self):
        return sum(item.valor for item in self.itens)

mochila = Mochila()
mochila.adicionar(Item('Espada', 120))
mochila.adicionar(Item('Poção', 10))
print(mochila.valor_total())  # 130
```

### Herança: um objeto "é um tipo de" outro

```python
class Personagem:
    def __init__(self, nome, ataque):
        self.nome = nome
        self.ataque = ataque

    def atacar(self):
        return self.ataque

# Mago herda tudo de Personagem e acrescenta ou muda o que for diferente
class Mago(Personagem):
    def __init__(self, nome, ataque, mana):
        super().__init__(nome, ataque)   # reaproveita o __init__ do "pai"
        self.mana = mana

    def atacar(self):                    # sobrescreve o método do pai
        if self.mana >= 10:
            self.mana -= 10
            return self.ataque * 2       # magia gasta mana e dá o dobro de dano
        return self.ataque

# polimorfismo: a mesma chamada, comportamentos diferentes
for p in [Personagem('Guerreiro', 12), Mago('Lyra', 10, 20)]:
    print(p.nome, p.atacar())
```

### Encapsulamento (por convenção)

```python
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo      # o _ avisa: "não mexa direto daqui de fora!"

    def sacar(self, valor):
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor

    def ver_saldo(self):
        return self._saldo
```

### Seus próprios erros (módulo 10 encontra a POO)

```python
# um erro personalizado é uma classe que herda de Exception
class SaldoInsuficienteError(Exception):
    pass

try:
    raise SaldoInsuficienteError('Faltam 30 moedas!')
except SaldoInsuficienteError as erro:
    print('Erro:', erro)
```

### Guardando objetos em JSON (módulo 11 também volta)

```python
import json

class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    # o JSON só entende dicionários, listas, textos e números, então convertemos
    def to_dict(self):
        return {'nome': self.nome, 'vida': self.vida}

jogador = Jogador('Miguel', 80)
with open('save.json', 'w', encoding='utf-8') as arquivo:
    json.dump(jogador.to_dict(), arquivo, ensure_ascii=False)

# para carregar, leia o dicionário e crie o objeto de novo
with open('save.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
jogador = Jogador(dados['nome'], dados['vida'])
```

Dica: nome de classe em `MaiusculaCadaPalavra` (`ContaBancaria`), nomes de métodos e atributos em `minusculas_com_underline`. Pergunte-se sempre: "isso é uma **coisa** (classe) ou uma **ação** (método)?"

## 2. Missões e Desafios (Lista de Exercícios)

Instruções: Faça todos os exercícios sem olhar soluções. Os exercícios de nível Médio e Difícil devem combinar conceitos dos módulos anteriores: Tipos de Dados, Condicionais, Loops, Listas, Dicionários, Funções, Strings, Tuplas e Conjuntos, Arquivos, Tratamento de Erros, Módulos e Comprehensions.

---

Fase 1: Aquecimento (Fácil — Exercícios 1 ao 15)

1. Crie uma classe `Cachorro` vazia (use `pass`) e crie um objeto dela.
2. Crie a classe `Pessoa` com `__init__(self, nome, idade)` e mostre os atributos de um objeto.
3. Crie três objetos `Pessoa` diferentes e mostre o nome de cada um.
4. Adicione o método `apresentar()` à classe `Pessoa`, que imprime `Oi, sou <nome> e tenho <idade> anos`.
5. Adicione o método `aniversario()` que soma 1 à idade da pessoa.
6. Crie a classe `Jogador` com o método `ganhar_pontos(qtd)` que soma pontos em um atributo `pontos`.
7. Crie a classe `Retangulo` (`largura`, `altura`) com o método `area()` que **retorna** a área.
8. Crie `Jogador(nome, vida=100)` com valor padrão para a vida e teste com e sem o segundo argumento.
9. Altere diretamente um atributo fora da classe (por exemplo, `jogador.vida = 50`) e mostre o resultado.
10. Implemente `__str__` na classe `Jogador` para que `print(jogador)` mostre algo como `Miguel (100 de vida)`.
11. Crie a classe `Monstro` com um atributo de classe `total` que conta quantos monstros já foram criados.
12. Adicione o método `esta_vivo()` ao `Jogador`, que retorna `True` se a vida for maior que zero.
13. Crie a classe `Mochila` com uma lista `itens` e um método `adicionar(item)`.
14. Mostre o tipo de um objeto com `type()` e confira com `isinstance(objeto, Classe)`.
15. Crie dois objetos da mesma classe, altere um deles e explique em um comentário por que o outro não mudou.

---

Fase 2: Subindo de Nível (Médio — Exercícios 16 ao 25)
Observação: use classes junto com `for`/`while`, `if`/`else`, listas, dicionários, funções, strings, tuplas, conjuntos, arquivos, tratamento de erros, módulos e comprehensions.

16. (Conta bancária) Crie a classe `Conta` (`titular`, `saldo`) com os métodos `depositar(valor)` e `sacar(valor)`. O saque deve levantar `ValueError` se o saldo for insuficiente. Percorra uma lista de operações com um loop e trate os erros com `try`/`except`.
17. (Boletim) Crie a classe `Aluno` (`nome`, lista `notas`) com os métodos `adicionar_nota(nota)`, `media()` e `situacao()` (`Aprovado` se >= 7, `Recuperação` se >= 5, `Reprovado` caso contrário). Crie vários alunos em uma lista e use uma comprehension para listar os aprovados.
18. (Personagem de RPG) Crie `Personagem` (`nome`, `vida`) com `receber_dano(dano)` (a vida não fica abaixo de 0) e `curar(qtd)` (a vida não passa de 100). Simule uma sequência de eventos com um loop.
19. (Loja) Crie `Produto` (`nome`, `preco`) e `Carrinho` com uma lista de produtos, o método `total()` e um desconto de 10% quando o total passar de 100. Mostre o resumo do carrinho com f-strings.
20. (Formas geométricas) Crie `Circulo` e `Retangulo`, ambos com `area()` e `perimetro()` (use o módulo `math`). Coloque objetos das duas classes na mesma lista e mostre as áreas em ordem decrescente com `sorted` e `lambda`.
21. (Tarefas) Crie `Tarefa` (`titulo`, `feita=False`) com `concluir()` e a classe `ListaDeTarefas` com `adicionar()`, `listar()` e `pendentes()` (use uma comprehension).
22. (Herança de animais) Crie `Animal` (`nome`) com o método `falar()` e as classes `Cachorro` e `Gato` que sobrescrevem `falar()`. Percorra uma lista com animais de tipos diferentes e chame `falar()` em cada um.
23. (Herança no RPG) Crie `Guerreiro` e `Mago`, ambos herdando de `Personagem`, usando `super().__init__()`. O mago tem `mana` e o método `atacar()` de cada um deve se comportar de forma diferente.
24. (Salvando objetos) Crie a classe `Jogador` com `to_dict()` e uma função `jogador_de_dict(dados)`. Salve em `jogador.json` e carregue de volta. Se o arquivo não existir, crie um jogador novo.
25. (Exceção personalizada) Crie `SaldoInsuficienteError`, que herda de `Exception`, e use-a no método `sacar()` da classe `Conta`. Capture o erro e mostre uma mensagem amigável.

---

Fase 3: O Desafio do Chefe (Difícil — Exercícios 26 ao 30)
Observação: são mini-projetos; combine variáveis, condicionais, loops, listas, dicionários, funções, strings, tuplas, conjuntos, arquivos, tratamento de erros, módulos, comprehensions e classes. O Input e o Output esperados estão descritos.

26. (Sistema de Biblioteca) Crie as classes `Livro` (`titulo`, `autor`, `disponivel`) e `Biblioteca` (que guarda os livros e quem pegou o quê). Cada membro pode ficar com no máximo 2 livros. Crie exceções personalizadas para livro indisponível e limite atingido. O programa lê comandos até `FIM`: `ADICIONAR titulo;autor`, `EMPRESTAR membro;titulo`, `DEVOLVER membro;titulo` e `LISTAR` (na ordem de cadastro).
    Input:
    ```
    ADICIONAR Percy Jackson;Rick Riordan
    ADICIONAR Harry Potter;J.K. Rowling
    ADICIONAR Naruto Vol 1;Masashi Kishimoto
    EMPRESTAR Ana;Percy Jackson
    EMPRESTAR Beto;Percy Jackson
    EMPRESTAR Ana;Harry Potter
    EMPRESTAR Ana;Naruto Vol 1
    DEVOLVER Ana;Percy Jackson
    LISTAR
    FIM
    ```
    Output:
    ```
    Livro adicionado: Percy Jackson
    Livro adicionado: Harry Potter
    Livro adicionado: Naruto Vol 1
    Ana pegou: Percy Jackson
    Erro: Percy Jackson não está disponível
    Ana pegou: Harry Potter
    Erro: Ana atingiu o limite de 2 livros
    Ana devolveu: Percy Jackson
    Percy Jackson (Rick Riordan) - Disponível
    Harry Potter (J.K. Rowling) - Emprestado para Ana
    Naruto Vol 1 (Masashi Kishimoto) - Disponível
    ```

27. (Arena com Herança) Crie a classe `Personagem` (`nome`, `vida`, `ataque`, `defesa`) com `atacar(alvo)` (dano = `ataque - defesa` do alvo, no mínimo 1) e `receber_dano(dano)` (a vida não fica abaixo de 0). Crie `Guerreiro`, que causa 4 de dano a mais em cada ataque, e `Mago`, que tem `mana`: se tiver pelo menos 10 de mana, gasta 10 e o ataque vale o dobro (`ataque * 2 - defesa`); sem mana, ataca normalmente. Dois personagens lutam em turnos, começando pelo guerreiro.
    Input (já definido no programa): `Guerreiro('Thor', vida=60, ataque=14, defesa=6)` e `Mago('Lyra', vida=45, ataque=10, defesa=2, mana=20)`.
    Output:
    ```
    Turno 1: Thor causa 16 de dano. Lyra: 29 de vida
    Turno 1: Lyra causa 14 de dano. Thor: 46 de vida
    Turno 2: Thor causa 16 de dano. Lyra: 13 de vida
    Turno 2: Lyra causa 14 de dano. Thor: 32 de vida
    Turno 3: Thor causa 16 de dano. Lyra: 0 de vida
    Lyra foi derrotada! Thor venceu com 32 de vida restante.
    ```

28. (Banco Orientado a Objetos) Crie as classes `Conta` (com histórico de operações guardado como lista de tuplas `(tipo, valor)`) e `Banco` (dicionário de contas). Crie exceções personalizadas para conta inexistente, saldo insuficiente e valor inválido. O programa lê comandos até `FIM`: `CRIAR nome saldo`, `TRANSFERIR origem destino valor`, `SACAR nome valor`, `DEPOSITAR nome valor` e `EXTRATO nome`. Ao final, salve o banco em `banco.json`. A criação da conta não entra no histórico; as transferências registram `transferência enviada` e `transferência recebida`.
    Input:
    ```
    CRIAR Ana 100
    CRIAR Beto 50
    TRANSFERIR Ana Beto 30
    SACAR Beto 100
    DEPOSITAR Cris 10
    DEPOSITAR Ana -5
    EXTRATO Ana
    FIM
    ```
    Output:
    ```
    Conta criada: Ana (100.00)
    Conta criada: Beto (50.00)
    Transferência de 30.00 de Ana para Beto realizada
    Erro: saldo insuficiente (disponível: 80.00)
    Erro: conta 'Cris' não existe
    Erro: o valor deve ser positivo
    Extrato de Ana:
    transferência enviada: 30.00
    Saldo: 70.00
    Banco salvo em banco.json
    ```

29. (Inventário com Peso) Crie `Item` (`nome`, `peso`, `valor`) e `Inventario` (capacidade máxima de peso, lista de itens). `adicionar()` levanta uma exceção personalizada se o item não couber, e `remover()` levanta outra se o item não existir. O programa lê comandos até `FIM`: `CAPACIDADE n`, `ADICIONAR nome peso valor`, `REMOVER nome` e `RESUMO` (peso usado, valor total e itens do mais valioso para o menos valioso).
    Input:
    ```
    CAPACIDADE 10
    ADICIONAR Espada 5 120
    ADICIONAR Escudo 4 80
    ADICIONAR Poção 1 10
    ADICIONAR Armadura 5 200
    REMOVER Espada
    ADICIONAR Armadura 5 200
    REMOVER Dragão
    RESUMO
    FIM
    ```
    Output:
    ```
    Capacidade definida: 10
    Adicionado: Espada
    Adicionado: Escudo
    Adicionado: Poção
    Erro: sem espaço para Armadura (peso 5, livre 0)
    Removido: Espada
    Adicionado: Armadura
    Erro: Dragão não está no inventário
    Peso: 10/10
    Valor total: 290
    Itens (do mais valioso): Armadura (200), Escudo (80), Poção (10)
    ```

30. (Mini-projeto: Sistema da Escola) Crie `Pessoa` (`nome`, `idade`), `Aluno` (herda de `Pessoa`, com lista de notas, `media()` e `situacao()`), `Professor` (herda de `Pessoa`, com `disciplina`) e `Turma` (nome `6A`, um professor e uma lista de alunos). A média de um aluno sem notas é `0.0`. O programa lê comandos até `FIM`: `PROFESSOR nome idade disciplina`, `ALUNO nome idade`, `NOTA nome valor` (a nota deve estar entre 0 e 10) e `RELATORIO` (alunos do maior para o menor valor de média e a média da turma). Ao final, salve a turma em `turma.json`. Trate todos os erros e organize as classes em um arquivo `escola.py` importado pelo `main.py`.
    Input:
    ```
    PROFESSOR Marta 40 Matemática
    ALUNO Ana 15
    ALUNO Beto 16
    NOTA Ana 8
    NOTA Ana 9
    NOTA Beto 5
    NOTA Beto 6
    NOTA Zeca 7
    NOTA Ana 11
    RELATORIO
    FIM
    ```
    Output:
    ```
    Professor(a) cadastrado(a): Marta (Matemática)
    Aluno cadastrado: Ana
    Aluno cadastrado: Beto
    Nota registrada: Ana = 8.0
    Nota registrada: Ana = 9.0
    Nota registrada: Beto = 5.0
    Nota registrada: Beto = 6.0
    Erro: aluno 'Zeca' não encontrado
    Erro: a nota deve estar entre 0 e 10
    Turma 6A - Professor(a): Marta (Matemática)
    Ana (15 anos) - média 8.5 - Aprovado
    Beto (16 anos) - média 5.5 - Recuperação
    Média da turma: 7.0
    Turma salva em turma.json
    ```
