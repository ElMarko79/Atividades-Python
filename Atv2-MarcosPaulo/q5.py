print("************************************************")
print("CÁLCULO DE GRANDEZAS")
print("************************************************")
print("1. Velocidade (Em Km/h)")
print("2. Distância (Em Km)")
print("3. Tempo (Em h)")
print("************************************************")
print("Qual grandeza deseja calcular?")
grand = int(input("> "))

if grand == 1:
    Km = int(input("Distância: "))
    h = int(input("Tempo: "))
    Kmph = Km / h
    print(f"Velocidade: {Kmph}")
elif grand == 2:
    Kmph = int(input("Velocidade: "))
    h = int(input("Tempo: "))
    Km = Kmph * h
    print(f"Distância: {Km}")
elif grand == 3:
    Kmph = int(input("Velocidade: "))
    Km = int(input("Distância: "))
    h = Km / Kmph
    print(f"Tempo: {h}")

if grand < 1 or grand > 3:
    print("Grandeza inexistente")
