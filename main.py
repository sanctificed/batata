import random


elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

senhacarct = int(input("Insira a quantidade de caracteres: "))

senha = ""

for i in range (senhacarct):
senha += random.choice(elements)

print("Essa é sua senha: " + senha
