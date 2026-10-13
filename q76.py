dados=[10,"20",30,"abc",50]
for valor in dados:
    if str(valor).isnumeric(): print(int(valor))
    else: print("valor invalido")
