medicamentos={}
for i in range(5):
    nome=input("Digite o medicamento")
    quantidade=int(input("Digite a quantidade"))
    medicamentos[nome]=quantidade
nome=input("Digite o medicamento para consultar")
print(medicamentos[nome])
