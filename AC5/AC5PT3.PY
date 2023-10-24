try:
    num1 = int(input("Digite o primeiro número inteiro para a divisão: "))
    num2 = int(input("Digite o segundo número inteiro para a divisão: "))

    resultado = num1 / num2
    print(f'A divisão de {num1} por {num2} é: {resultado}')

except ValueError:
    print("Você deve inserir apenas números inteiros.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

finally:
    print("Programa encerrado.")
