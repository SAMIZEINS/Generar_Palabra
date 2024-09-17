import random

a = input("Ingrese una palabra en minuscula: ")
longitud = len(a)
contador = 0
letras = "abcdefghijqlmnñopqrstuvwxyz"

while True:

    b = "".join(random.SystemRandom().choice(letras) for i in range(longitud))
    contador += 1
    if b == a:
        break
    

print("Intentos: ",contador)
print("Palabra: ",b)