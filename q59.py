n1=int(input("Digite o primeiro numero"))
n2=int(input("Digite o segundo numero"))
if n1%2==0 and n2%2==0:
    if n1<n2: print(n1)
    else: print(n2)
else:
    if n1>n2: print(n1)
    else: print(n2)
