def operaciones(numero, x, y):
    if numero == 1:
        return x + y
    elif numero == 2:
        return x - y
    elif numero == 3:
        return x * y
    else:
        return x / y


print("Bienvenido a la calculadora \nEstas son las operaciones que puedes realizar:")
while True:
    print("1.Suma \n2.Resta \n3.Multiplicacion \n4.Division")
    try:
        numero = int(
            input("Introduce el número de la operacion que quieres realizar: "))
        if numero > 4:
            print("Ese no es un número valido")
            print()
            continue
        x = int(input("Introduce el primer número: "))
        y = int(input("Introduce el segundo número: "))
    except ValueError:
        print("Debe ser un valor númerico: (1,2,3...)")
    else:
        
        print("El resultado es: " + str(operaciones(numero, x, y)))
        continuar = input("Deseadas continuar? \n y/n ")
        print()
        print()
        if continuar != "y":
            break
print("Gracias por usar nuestra calculadora :D")
