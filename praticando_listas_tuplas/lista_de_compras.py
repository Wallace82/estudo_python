lista_compras  = ["café", "açúcar", "leite", "pão", "ovos"]

item = input("Digite o item que você quer verificar: ")

if item in lista_compras:
    print("O item está na lista de compras.")
else:
    lista_compras.append(item)
    print(f"O item {item} precisa ser comprado e foi adicionado à lista de compras.")
    print("Lista de compras atualizada:", lista_compras)