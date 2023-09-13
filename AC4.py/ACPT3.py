a = 1
b1 = 0
b2 = 0
b3 = 0
b4 = 0
while a > 0:
    a = int(input("Digite um numero"))
    if a >= 0 and a <= 25:
        b1 = b1 + 1
    elif a >= 26 and a <= 50:
        b2 = b2 +1
    elif a >= 51 and a <= 75:
        b3 = b3 + 1
    elif a >= 76 and a <= 100:
        b4 = b4 + 1
print("A quantidade de números entre 0 e 25 é:", b1,"entre votos 26-50 é:", b2,"entre votos 51-75 é:", b3,"entre votos 76-100 é:",b4,)

