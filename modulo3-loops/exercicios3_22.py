numero = 30

for n in range(2, numero):

    primo = True

    for divisor in range(2, n):  # Tem que criar um loop só pro divisor

        if n % divisor == 0:
            primo = False
            break         # Interrompe o loop interno

    if primo == True:
        print(n)


def retorna_primos(numero):
    primos = []

    for num in range(2, numero):
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            primos.append(num)
    return primos

print(retorna_primos(30))
