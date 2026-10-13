alunos={}
total=0
for i in range(5):
    nome=input("Digite o nome")
    nota=float(input("Digite a nota"))
    alunos[nome]=nota
    total=total+nota
media=total/5
print("media da turma",media)
for nome in alunos:
    if alunos[nome]>=7:
        print(nome,"aprovado")
