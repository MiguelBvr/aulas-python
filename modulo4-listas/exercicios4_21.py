alunos = [('Ana',8.5),('Beto',6.7),('Cris',9.0)]
alunos_aprovados = []

for nome, nota in alunos:
    if nota >= 7:
        alunos_aprovados.append(nome)

print(alunos_aprovados)
