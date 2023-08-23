Ano = float(input("Digite o ano"))

Ano % 4 == 0 
Ano % 100 == 0
Ano % 400 == 0

print(Ano % 4 == 0 and Ano%100!=0 or Ano % 400 ==0)

