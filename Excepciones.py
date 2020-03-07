# a = int(input("Digite un número: "))

# b = int(input("Digite otro número: "))

# suma = a+b

# print("la suma es: " + str(suma))

try:
    a = int(input("Digite un número: "))

    b = int(input("Digite otro número: "))
except ValueError:
    print("Solo números")
else:
    suma = a+b
    print("la suma es: " + str(suma))
