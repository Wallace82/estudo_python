vendas_banana = int(input("Digite a quantidade de BANANAS vendidas: "))
vendas_maca = int(input("Digite a quantidade de MAÇÃS vendidas: "))

max_vendas = max(vendas_banana, vendas_maca)
print("O maior número de vendas foi:", max_vendas)

if vendas_banana > vendas_maca:
    print("as BANANAS tiveram mais vendas.")
elif (vendas_maca > vendas_banana):
    print("as MAÇÃS tiveram mais vendas.")
else:
    print("Foram vendidas a mesma quantidade de BANANAS e MAÇÃS).")