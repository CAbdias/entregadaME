numero=int(input("Digite um numero"))
total=0
for i in range(1,numero):
    if numero%i==0: total=total+i
if total==numero: print(True)
else: print(False)
