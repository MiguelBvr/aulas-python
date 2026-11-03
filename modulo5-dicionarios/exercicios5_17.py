votos = ['Ana','Beto','Ana','Cris','Beto','Ana']
pontuacao = []
total = {}
from random import randint


for voto in range(len(votos)):
    numero_pontuacao = randint(0, 50)
    pontuacao.append(numero_pontuacao)

for i in range(len(votos)):
    total[votos[i]] = total.get(votos[i], 0) + pontuacao[i]

def ordena_por_pontuacao(objeto):
    return objeto[1]

ranking = sorted(total.items(), key=ordena_por_pontuacao, reverse=True)

print(f'O ganhador foi o(a) {ranking[0][0]}')

