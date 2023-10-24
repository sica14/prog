def contar_digitos(numero):
    if numero == 0:
        return 1
    count = 0
    while numero != 0:
        numero //= 10
        count += 1
    return count

numero = int(input("Digite um número inteiro: "))

quantidade_digitos = contar_digitos(numero)

print(f'O número {numero} possui {quantidade_digitos} dígitos.')

