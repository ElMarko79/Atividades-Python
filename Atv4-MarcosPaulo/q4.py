while True:
    n = int(input("Insira um número: "))
    if n == 0:
        print("Operação encerrada")
        break
    num = int(input("Começar por: "))
    final = int(input("Terminar por: "))
    while num <= (final):
        result = num * n
        print(f"{n} x {num} = {result}")
        num = num + 1
        if num == (final + 1):
            break
    
