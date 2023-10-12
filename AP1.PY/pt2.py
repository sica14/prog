def calculadora():
    num = 0.0
    while True:
        print(num)
        num1 = float(input("Informe um número, ou aperte ENTER para sair:"))

        if not num1:
            break
         
        operacao = input("Digite a operação (+, -, *, /), X para zerar ou ENTER para sair:")

        
        if operacao == "X": 
         num = 0.0
         continue
        
        num2 = float(input("Informe um número, ou ENTER para sair:"))
         
    
        if operacao == "+":
         num = num1 + num2
        elif operacao == "-":
         num = num1 - num2
        elif operacao == "*":
         num = num1 * num2
        elif operacao == "/":
         num = num1 / num2

    print(num)


calculadora()
        
    
    
         
         


        

   