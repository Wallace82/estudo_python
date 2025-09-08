input_vendas = input("Digite os valores das vendas: ")
lista_vendas = [float(valor) for valor in input_vendas.split()]

def calcular_valor_total_vendas(vendas):
    return sum(vendas)

valor_total = calcular_valor_total_vendas(lista_vendas)
print(f"O valor total das vendas é: R$ {valor_total:.2f}")