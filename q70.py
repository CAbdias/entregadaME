perfil={"permissoes":["ler","editar","excluir"]}
indice=int(input("Digite o indice"))
if 0<=indice<len(perfil["permissoes"]): print(perfil["permissoes"][indice])
else: print("acesso_restrito")
