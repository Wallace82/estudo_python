input_produtos = input("Digite os produtos separados por vírgula: ")
input_precos = input("Digite os preços separados por vírgula: ")

produtos = [produto.strip() for produto in input_produtos.split(",")]
precos = [float(preco.strip()) for preco in input_precos.split(",")]    

estoque = dict(zip(produtos, precos))

print("Estoque:")
for produto, preco in estoque.items():
    print(f"{produto}: R$ {preco:.2f}")
