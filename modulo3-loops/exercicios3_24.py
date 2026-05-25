anterior = 1
atual = 1

for n in range(1, 10):

    print(anterior)
    anterior, atual = atual, atual + anterior


def fibonacci(n):
    anterior = 1
    atual = 1

    for i in range(1, n + 1):
        print(f'{i}: {anterior}')
        anterior, atual = atual, atual + anterior


fibonacci(10)
