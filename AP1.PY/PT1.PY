import random

lancamentos = 0

while True:
    lancamentos += 1

    tamanho_dado = input("Forneça o tamanho do dado que será rolado (ENTER para sair):")
    if tamanho_dado == "":
        break
    elif tamanho_dado.isdigit() and int(tamanho_dado) > 0:
        tamanho_dado = int(tamanho_dado)
    else:
        print("A informação passada não é válida!")
        continue

    numero_dados = input("Forneça o número de dados que serão rolados (em branco == 1):")
    if numero_dados == "":
        numero_dados = 1
    elif numero_dados.isdigit() and int(numero_dados) > 0:
        numero_dados = int(numero_dados)
    else:
        print("A informação passada não é válida! Deve ser um número inteiro maior que zero.")
        continue

    resultados = [random.randint(1, tamanho_dado) for _ in range(numero_dados)]

    print(f"\nResultados do Lançamento n. {lancamentos}:")
    for i, resultado in enumerate(resultados):
        print(f"Lançamento n. {i+1} - {resultado}")

    print(numero_dados, "dado(s) de", tamanho_dado, "lados:", "\n", resultados)
    print("\n")


