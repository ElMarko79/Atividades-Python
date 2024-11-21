num = int(input("Insira um número: "))

if num % 3 == 0:
    print("O número é múltiplo de 3")
elif num % 5 == 0:
    print("O número é múltiplo de 5")
elif num % 3 == 0 and num % 5 == 0:
    print("O número é múltiplo de ambos")
elif (num % 3 and num % 5) != 0:
    print("O número não é múmtiplo de nenhum dos dois")