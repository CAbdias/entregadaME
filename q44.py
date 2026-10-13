matriz=[[10,8],[3,4]]
menor=matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor<menor:
            menor=valor
print(menor)
