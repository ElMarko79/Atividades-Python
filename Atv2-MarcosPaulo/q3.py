print("1. Janeiro")
print("2. Fevereiro")
print("3. Março")
print("4. Abril")
print("5. Maio")
print("6. Junho")
print("7. Julho")
print("8. Agosto")
print("9. Setembro")
print("10. Outubro")
print("11. Novembro")
print("12. Dezembro")
mes = int(input("Indique o mês: "))

if (mes == 12 or mes == 1) or mes == 2:
    print("Verão")
elif (mes == 3 or mes == 4) or mes == 5:
    print("Outono")
elif (mes == 6 or mes == 7) or mes == 8:
    print("Inverno")
elif (mes == 9 or mes == 10) or mes == 11:
    print("Primavera")
elif mes > 12 or mes < 1:
    print("Estação do ano inexistente")