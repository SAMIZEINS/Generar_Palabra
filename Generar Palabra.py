import random

palabra = input("Ingrese una palabra en minuscula: ")
longitud = len(palabra)
contador = 0
letras = "abcdefghijqlmnñopqrstuvwxyz"

while True:

    generador = "".join(random.SystemRandom().choice(letras) for i in range(longitud))
    contador += 1
    if generador == palabra:
        break
    

print("Intentos: ",contador)
print("Palabra: ",generador)
