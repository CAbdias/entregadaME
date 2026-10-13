temperaturas=[]
for i in range(5):
    temperatura=float(input("Digite a temperatura"))
    temperaturas.append(temperatura)
media=sum(temperaturas)/5
print("media",media)
if media>=18 and media<=28:
    print("dentro da faixa ideal")
else:
    print("fora da faixa ideal")
print(temperaturas)
