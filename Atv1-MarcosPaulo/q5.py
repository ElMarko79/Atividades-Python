a = int(input("Valor a: "))
b = int(input("Valor b: "))
c = int(input("valor c: "))

delta = b**2 - 4*a*c

if a > 0 and delta > 0:
    print("Concavidade para cima e 2 raízes reais distintas (toca no eixo x em 2 pontos)")
elif a > 0 and delta == 0:
    print("Concavidade para cima e 2 raízes reais e iguais (toca no eixo x em 1 ponto)")
elif a > 0 and delta < 0:
    print("Concavidade para cima e não tem raiz real (não toca no eixo x)")
elif a < 0 and delta > 0:
    print("Concavidade para baixo e 2 raízes reais distintas (toca no eixo x em 2 pontos)")
elif a < 0 and delta == 0:
    print("Concavidade para baixo e 2 raízes reais e iguais (toca no eixo x em 1 ponto)")
elif a < 0 and delta < 0:
    print("Concavidade para baixo e não tem raiz real (não toca no eixo x)")