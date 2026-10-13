n1=float(input("Digite a primeira nota"))
n2=float(input("Digite a segunda nota"))
n3=float(input("Digite a terceira nota"))
if n1<0 or n1>10 or n2<0 or n2>10 or n3<0 or n3>10: print("nota invalida")
else:
    media=(n1+n2+n3)/3
    print("media",media)
    if media>=7: print("Aprovado")
    else: print("Reprovado")
