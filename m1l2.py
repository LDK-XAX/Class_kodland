import random
Caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("Ingresa tu longitud: "))
password=""
for i in range(longitud):
    password+=random.choice(Caracteres)
print(f"Esta es tu contraseña: {password}")
