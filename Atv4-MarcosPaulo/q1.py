while True:
    print("************************************************")
    print("PROGRAMA PARA CÁLCULO DE GRANDEZAS ELÉTRICAS")
    print("************************************************")
    print("1. Tensão (Em Volt)")
    print("2. Resistência (Em Ohm)")
    print("3. Corrente (Em Ampére)")
    print("0. SAIR DO PROGRAMA")
    print("************************************************")
    opcao = int(input("Qual grandeza deseja calcular? (digite a opção) > "))

    if opcao == 1:
        R = float(input("Resistência: "))
        i = float(input("Corrente: "))
        U = R*i
        print(f"Tensão: {U}")
        print("")
    elif opcao == 2:
        U = float(input("Tensão: "))
        i = float(input("Corrente: "))
        R = U/i
        print(f"Resistência: {R}")
        print("")
    elif opcao == 3:
        U = float(input("Tensão: "))
        R = float(input("Resistência: "))
        i = U/R
        print(f"Corrente: {i}")
        print("")
    elif opcao == 0:
        print("Programa encerrado")
        print("")
        break
