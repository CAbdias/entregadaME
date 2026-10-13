disciplinas=("Matematica","Portugues")
alunos={}
for i in range(3):
    nome=input("Digite o nome")
    matematica=float(input("Digite a nota de matematica"))
    portugues=float(input("Digite a nota de portugues"))
    alunos[nome]=[matematica,portugues]
for nome in alunos:
    media=sum(alunos[nome])/2
    print(nome)
    print("media",media)
    if media>=7:
        print("Aprovado")
    else:
        print("Reprovado")
print(disciplinas)
