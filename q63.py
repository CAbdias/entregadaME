numeros=[]
for i in range(5):
    numeros.append(float(input("Digite um numero")))
maior=numeros[0]
menor=numeros[0]
for numero in numeros:
    if numero>maior: maior=numero
    if numero<menor: menor=numero
print("maior",maior)
print("menor",menor)
