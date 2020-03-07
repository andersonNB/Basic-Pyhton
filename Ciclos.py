# # Ciclos en python
# manzanas = 10
# # While
# while manzanas > 0:
#     print("Me estoy comiendo una manzana:" + str(manzanas))
#     manzanas -= 1

# print("Me quede sin manzanas")

# # <------------------------------------------------------------>
# # For
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for numero in lista_numeros:
#     if numero == 5:
#         continue
#         # break
#     print(numero)


# vocales = "aeiou"
# for vocal in vocales:
#     print(vocal.upper())

# while vocales:
#     print(vocales.upper())
#     break
# <---------------------Mi solucion>

numero1 = input("Digite el primer numero: ")
numeroN = int(numero1)
numero2 = input("Digite el segundo numero: ")
numeroN2 = int(numero2)
suma = numeroN + numeroN2
print(suma)
