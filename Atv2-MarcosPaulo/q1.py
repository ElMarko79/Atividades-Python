id = int(input("Sua idade: "))

if id >= 1 and id < 12:
    print("Você é uma criança")
elif id >= 12 and id <= 18:
    print("Você é um adolescente")
elif id > 18 and id < 60:
    print("Você é um adulto")
elif id > 60:
    print("Você é um idoso")

if id < 1:
    print("ERRO")