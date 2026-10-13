import random
numero=random.randint(1,10)
while True:
    chute=int(input("Digite um numero"))
    if chute==numero:
        print("acertou")
        break
    elif chute<numero:
        print("o numero é maior")
    else:
        print("o numero é menor")
