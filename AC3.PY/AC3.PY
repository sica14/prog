salário = float(input("Diga o seu salário"))
print("Valor do salário atual")
def reajuste(salário):
    if salário <= 280:
        percentual = 0.2
        
    elif salário > 280 and salário < 700:
        percentual = 0.15
        
    elif salário > 700 and salário < 1500:
        percentual = 0.1
        
    elif salário > 1500:
        percentual = 0.05
        
    aumento = percentual* salário
    salarioatual = aumento + salário
    print("Aumento de", percentual*100,"%")
    print("Valor do aumento:",aumento)
    print("Salario atual",salarioatual)
reajuste(salário)

