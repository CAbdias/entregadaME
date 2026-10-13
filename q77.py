saldo=1000
valor=float(input("Digite o valor do saque"))
if valor<=0: print("valor invalido")
elif valor>saldo: print("saldo insuficiente")
else:
    saldo=saldo-valor
    print("novo saldo",saldo)
