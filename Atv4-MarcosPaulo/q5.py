cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco= 0

while True:
    print("**************************************")
    print("URNA DE VOTAÇÃO")
    print("**************************************")
    print("CANDIDATOS")
    print("**************************************")
    print("1 - Hugo")
    print("2 - Pedro Iuri")
    print("3 - Maíra")
    print("4 - Bruno")
    print("5 - Voto nulo")
    print("6 - Voto em Branco")
    print("**************************************")
    voto = int(input("Qual seu voto? > "))

    if voto == 1:
        cand1 = cand1 + 1
    elif voto == 2:
        cand2 = cand2 + 1
    elif voto == 3:
        cand3 = cand3 + 1
    elif voto == 4:
        cand4 = cand4 + 1
    elif voto == 5:
        nulo = nulo + 1
    elif voto == 6:
        branco = branco + 1
    elif voto == 0:
        quantv1 = (cand1 * 100) / (cand1 + cand2 + cand3 + cand4 + nulo + branco)
        quantv2 = (cand2 * 100) / (cand1 + cand2 + cand3 + cand4 + nulo + branco)
        quantv3 = (cand3 * 100) / (cand1 + cand2 + cand3 + cand4 + nulo + branco)
        quantv4 = (cand4 * 100) / (cand1 + cand2 + cand3 + cand4 + nulo + branco)
        quantv5 = (nulo * 100) / (cand1 + cand2 + cand3 + cand4 + nulo + branco)
        quantv6 = (branco * 100) / (cand1 + cand2 + cand3 + cand4 + nulo + branco)

        print("")
        print("FIM")
        print("")
        print("**************************************")
        print("RESULTADO DA ELEIÇÃO")
        print("**************************************")
        print(f"1 - Hugo > {cand1} / {quantv1}")
        print(f"2 - Pedro Iuri > {cand2} / {quantv2}")
        print(f"3 - Maíra > {cand3} / {quantv3}%")
        print(f"4 - Bruno > {cand4} / {quantv4}%")
        print(f"5 - Voto nulo > {nulo} / {quantv5}%")
        print(f"6 - Voto em Branco > {branco} / {quantv6}%")
        break