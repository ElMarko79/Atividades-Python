n = int(input("Insira um número: "))
num = 1
while num <= 11:
    result = num * n
    print(f"{n} x {num} = {result}")
    num = num + 1
    if num == 11:
        break