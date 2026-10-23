from random import randint

jogos = [
    {"nome": "Fernando", "pontos": randint(1, 10)},
    {"nome": "Miguel", "pontos": randint(1, 10)},
    {"nome": "Mauro", "pontos": randint(1, 10)},
    {"nome": "Mariana", "pontos": randint(1, 10)},
    {"nome": "Luisa", "pontos": randint(1, 10)},
    {"nome": "Dinah", "pontos": randint(1, 10)},
]

def ordena_por_pontos(objeto):
    return objeto.get("pontos")

jogos.sort(key=ordena_por_pontos, reverse=True)

print(jogos[:3])
