def imprimir_padrao(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="   ")
        print()

n = int(input("Digite um número inteiro: "))

imprimir_padrao(n)

