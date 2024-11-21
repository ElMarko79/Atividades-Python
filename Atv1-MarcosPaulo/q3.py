print("****************************************************")
print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")
print("****************************************************")
opcao = int(input("Escolha uma opção: "))

if opcao == 1: 
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    media = ((n1 * 2) + (n2 * 2) + (n3 * 3) + (n4 * 3)) / 10
    print("")
    print(f"Média: {media}")
    print("")
elif opcao == 2:
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    quad = (num1 + num2)**2
    print("")
    print(quad)
    print("")
elif opcao == 3:
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))

    if num1 < num2:
        x = num1**3
        print(x)
    elif num2 < num1:
        y = num2**3
        print(y)
elif opcao > 3 or opcao < 1:
    print("Opção inválida")      