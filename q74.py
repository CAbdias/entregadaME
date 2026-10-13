produtos={1:"arroz",2:"feijao",3:"carne"}
id=int(input("Digite o id"))
if id in produtos: print(produtos[id])
else: print("HTTP 404")
