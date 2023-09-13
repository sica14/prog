
def determina_porcetagem_juros(num_parcelas):
    
    if num_parcelas == 1:
        percentual = 0
    
    if num_parcelas == 3:
        percentual = 0.10
    if num_parcelas == 6:
        percentual = 0.15
    if num_parcelas == 9:
        percentual = 0.2
    
    if num_parcelas == 12:
        percentual = 0.25
    return percentual

def exibe_dados(divida, num_parcelas):
    valor_dos_juros = divida*determina_porcetagem_juros(num_parcelas)
    valor_total = valor_dos_juros + divida
    valor_das_parcelas = valor_total / num_parcelas
    print(valor_dos_juros,valor_total,num_parcelas,valor_das_parcelas)

def opcoes_divida(divida):
    print("Valor dos juros Valor total quantidade de parcelas valor de parcela")
    print("0 R$", divida, "1 R%", divida)
    for n in range(3,13,3):
        exibe_dados(divida,n)
div = float(input("Diga a sua divida:"))
opcoes_divida(div)


   


    
