total_despesas = float(input("Digite o total de despesas do mês (R$):"))
orcamento_mensal = 3000.00

if total_despesas > orcamento_mensal:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do orçamento mensal.")
