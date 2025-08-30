hora_atual = int(input("Digite a hora atual (formato 24 horas):"))

if hora_atual < 8 or hora_atual > 18:
    print("Acesso negado.")
else:
    print("Acesso permitido.")