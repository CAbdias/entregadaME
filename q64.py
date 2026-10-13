a=int(input("Digite o primeiro numero"))
b=int(input("Digite o segundo numero"))
c=int(input("Digite o terceiro numero"))
total=a+b+c
if total>21 and (a==11 or b==11 or c==11): total=total-10
if total<=21: print(total)
else: print(-1)
