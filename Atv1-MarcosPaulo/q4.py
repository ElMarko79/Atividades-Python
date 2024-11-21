num1 = int(input("Medida 1: "))
num2 = int(input("Medida 2: "))
num3 = int(input("Medida 3: "))

if (num1 == num2 and num2 == num3) and num1 == num3:
    print("Triângulo equilátero")
elif num1 != num2 and num2 != num3 and num1 != num3:
    print("Trinângulo escaleno")
elif (num1 != num2 and num1 == num3):
    print("Triângulo isóceles")
elif (num1 == num2 and num1 != num3):
    print("Triângulo isóceles")
elif num1 == num3 and num2 != num3:
    print("Triângulo isóceles")
elif (num1 < 0 and num2 < 0) and num3 < 0:
    print("Não é possivel classificar o triângulo")