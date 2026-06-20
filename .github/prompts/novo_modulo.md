# Prompt: Gerador de Novo Módulo de Python

**Descrição:** Utilize este prompt em ferramentas como GitHub Copilot Workspace, Cursor ou outras IAs de desenvolvimento para criar novos módulos no repositório `aulas-python`, mantendo a consistência didática e estrutural.

---

**COPIE O TEXTO ABAIXO E ENVIE PARA A IA**

Atue como o professor de Python descrito em nosso arquivo `AGENTS.md` (com foco pedagógico em adolescentes, usando termos simples e analogias divertidas). 

Eu preciso que você crie um novo módulo para o nosso repositório.

**Parâmetros do Módulo:**
- Tema do módulo: [INSERIR TEMA, ex: Listas]
- Número do módulo: [INSERIR NÚMERO, ex: 4]
- Resumo dos módulos anteriores: 
  1-Tipos de Dados
  2-Condicionais
  3-Loops
  4-Listas

**Regras de Criação de Arquivos:**
1. Crie uma pasta raiz para o módulo no formato: `modulo[NÚMERO]-[tema_em_letras_minusculas]` (Ex: `modulo4-listas`).
2. Dentro dessa pasta, crie APENAS um arquivo chamado `README.md`.

**Estrutura obrigatória do `README.md`:**

## 1. Introdução Teórica e Prática
- Escreva uma explicação breve sobre o tema, com foco no "por que isso é útil?".
- Use analogias do dia a dia do adolescente (jogos, redes sociais, escola, animes/séries).
- Mostre blocos de código pequenos de exemplo com comentários pedagógicos.

## 2. Missões e Desafios (Lista de Exercícios)
Crie exatamente 30 exercícios seguindo a distribuição de dificuldade abaixo. 
**REGRA DE OURO (Aprendizado Cumulativo):** Os exercícios de níveis Médio e Difícil DEVEM obrigatóriamente exigir o uso combinado dos conceitos aprendidos nos módulos anteriores.

* **Fase 1: Aquecimento (Fácil - Exercícios 1 ao 15)**
    - Foco na sintaxe e funcionamento básico exclusivo do tema atual.
    - Enunciados curtos.
    
* **Fase 2: Subindo de Nível (Médio - Exercícios 16 ao 25)**
    - Exige raciocínio lógico.
    - Integra os temas passados obrigatóriamente (Ex: Se o tema for lista, force o uso de loops `for`/`while` para varrê-la e `if`/`else` para filtrar itens).
    - Crie historinhas de contexto (ex: inventário de um RPG, gerenciar notas da escola).

* **Fase 3: O Desafio do Chefe (Difícil - Exercícios 26 ao 30)**
    - Desafios complexos de raciocínio. Mini-projetos baseados em texto.
    - O aluno precisará juntar tudo o que sabe até hoje (variáveis, condicionais, loops e o tema atual) de forma inteligente.
    - Inclua exemplos de "O que o programa deve receber (Input)" e "O que deve mostrar (Output)".

**Observação final para a IA:** Gere apenas o conteúdo textual do arquivo. NÃO escreva a resolução dos exercícios no `README.md`, deixe o aluno tentar!
