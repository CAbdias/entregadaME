matriz=[[1,0,1],[1,1,0],[0,1,1]]
ocupadas=0
livres=0
for linha in matriz:
    for vaga in linha:
        if vaga==1:
            ocupadas=ocupadas+1
        else:
            livres=livres+1
print("ocupadas",ocupadas)
print("livres",livres)
