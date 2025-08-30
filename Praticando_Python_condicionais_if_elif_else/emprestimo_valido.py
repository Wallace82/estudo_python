
renda_mensal = float(input("Digite o valor da sua renda mensal: "))
parcela_desejada = float(input("Digite o valor da parcela desejada:"))

if renda_mensal < 2000:
    print("Empréstimo negado: renda abaixo de 2000.")
elif parcela_desejada > (renda_mensal * 0.3):
    print("Empréstimo negado: parcela acima de 30% da renda.")
else:
    print("Empréstimo aprovado.")
