posts = []
comando = {"1": "POST texto", "2": "DELETE índice", "3": "LISTAR"}
opcao = None

while opcao != "4":

    print("1. POST texto")
    print("2. DELETE índice")
    print("3. LISTAR")
    print("4. SAIR")
    opcao = input("Escolha uma das opções: ")
    acao = comando.get(opcao)

    if acao is not None:
      posts.append(acao)

                
print("Programa finalizado")
posts = str(posts)

with open("posts.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(posts)
