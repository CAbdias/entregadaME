import random
numero=random.randint(1,10)
chute=int(input("Digite um numero"))
if chute==numero:
    print("acertou")
else:
    print("errou")
print("numero era",numero)
