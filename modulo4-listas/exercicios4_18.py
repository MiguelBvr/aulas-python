usuarios = ["ana", "joao", "bia", "carlos", "rui", "fernanda"]

for nome in usuarios[:]:
    if len(nome) < 4:
        usuarios.remove(nome)

print(usuarios)
