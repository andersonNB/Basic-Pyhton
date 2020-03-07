def pedirPizza():
    print("Pedir pizza")


# pedirPizza()


def validar_entrada(edad):
    if edad < 18:
        print("No puedes entrar".upper())
    elif edad >= 21:
        print("Puedes entrar y beber")
    else:
        print("Puedes entrar , pero no beber")


edad = 17
validar_entrada(edad)


