print("************************************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("************************************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("************************************************")
print("Qual grandeza deseja calcular?")
enter = int(input("> "))

if enter == 1:
    R = float(input("Resistência: "))
    i = float(input("Corrente: "))
    U = R * i
    print("")
    print(f"Tensão: {U}")
    print("")
elif enter == 2:
    U = float(input("Tensão: "))
    i = float(input("Corrente: "))
    R = U / i
    print("")
    print(f"Resistência: {R}")
    print("")
elif enter == 3:
    U = float(input("Tensão: "))
    R = float(input("Resistência: "))
    i = U / R
    print("")
    print(f"Corrente: {i}")
    print("")

if enter > 3:
    print("")
    print("Cálculo inexistente")
    print("")
elif enter < 1:
    print("")
    print("Cálculo inexistente")
    print("")
