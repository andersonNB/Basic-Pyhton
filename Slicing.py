Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Pasos
>>> numeros = [0,1,2,3,4,5,6,7,8,9,10]
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[::]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[::2]
[0, 2, 4, 6, 8, 10]
>>> numeros[::1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[::3]
[0, 3, 6, 9]
>>> numeros[::2.5]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    numeros[::2.5]
TypeError: slice indices must be integers or None or have an __index__ method
>>> numeros[::5]
[0, 5, 10]
>>> numeros[2:8:2]
[2, 4, 6]
>>> numeros[2:9:2]
[2, 4, 6, 8]
>>> numeros[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> numeros[-2:-5:-1]
[9, 8, 7]
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> del numeros[0:4]
>>> numeros
[4, 5, 6, 7, 8, 9, 10]
>>> numeros[1:2] = [5,5.5,5.9]
>>> numeros
[4, 5, 5.5, 5.9, 6, 7, 8, 9, 10]
>>> numeros[7:] = [80,80]
>>> nuemros
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nuemros
NameError: name 'nuemros' is not defined
>>> numeros
[4, 5, 5.5, 5.9, 6, 7, 8, 80, 80]
>>> numeros[-1:-3] = [10,9]
>>> numeros
[4, 5, 5.5, 5.9, 6, 7, 8, 80, 10, 9, 80]
>>> del numeros[7:]
>>> numeros
[4, 5, 5.5, 5.9, 6, 7, 8]
>>> numeros[7:] = [9,10]
>>> numeros
[4, 5, 5.5, 5.9, 6, 7, 8, 9, 10]
>>> del numeros[1:4]
>>> numeros
[4, 6, 7, 8, 9, 10]
>>> numeros[0:1] = [5]
>>> numeros
[5, 6, 7, 8, 9, 10]
>>> numeros[0:2] = [4,5]
>>> numeros
[4, 5, 7, 8, 9, 10]
>>> numeros[1:] = [6,7,8,9,10]
>>> numeros
[4, 6, 7, 8, 9, 10]
>>> numeros[0:1] = [4,5]
>>> numeros
[4, 5, 6, 7, 8, 9, 10]
>>> 