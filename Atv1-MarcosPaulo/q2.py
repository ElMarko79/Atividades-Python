a = float(input("Estatura da 1° pessoa (Em metros): "))
b = float(input("Estatura da 2° pessoa (Em metros): "))
c = float(input("Estatura da 3° pessoa (Em metros): "))

if (a > b and a > c) and b > c:
    print("")
    print("1° pessoa > 2° pessoa > 3° pessoa")
    print("")
elif (a > c and a > b) and c > b:
    print("")
    print("1° pessoa > 3° pessoa > 2° pessoa")
    print("")
elif (b > a and b > c) and a > c:
    print("")
    print("2° pessoa > 1° pessoa > 3° pessoa")
    print("")
elif (c > a and c > b) and a > b:
    print("")
    print("3° pessoa > 1° pessoa > 2° pessoa")
    print("")
elif (c > a and c > b) and b > a:
    print("")
    print("3° pessoa > 2° pessoa > 1° pessoa")
    print("")
elif (b > c and b > a) and c > a:
    print("")
    print("2° pessoa > 3° pessoa > 1° pessoa")
    print("")

