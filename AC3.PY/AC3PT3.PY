

def conta():
    a = float(input("Diga o valor de a"))
    b = float(input("Diga o valor de b"))
    c = float(input("Diga o valor de c"))
    delta = (b ** 2) - 4 * a * c
    r1 =  (-b + delta**0.5) / (2*a)
    r2 =  (-b - delta**0.5) / (2*a)
    if a == 0:
        return "A equação não é do segundo grau"
    if delta < 0:
        return "A equação não possui raizes iguais"
    if delta == 0:
        return "A equação possui apenas uma raiz real", r1
    if delta > 0:
        return "A equação possui duas raízes reais", r1,r2
print(conta())
