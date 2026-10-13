nome=input("Digite o nome")
preco=float(input("Digite o preco"))
quantidade=int(input("Digite a quantidade"))

if nome=="": print("nome invalido")
elif preco<=0: print("preco invalido")
elif quantidade<0: print("quantidade invalida")
else: print("produto cadastrado com sucesso")
