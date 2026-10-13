texto=input("Digite uma frase")
caractere=input("Digite um caractere")
total=0
for letra in texto:
    if letra==caractere:
        total=total+1
print(total)
