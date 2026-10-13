import random
tentativas=0
conectado=False
while tentativas<3 and conectado==False:
    tentativas=tentativas+1
    if random.randint(1,2)==1:
        conectado=True
        print("conectado")
    else: print("erro na conexao")
if conectado==False: print("falha na conexao")
