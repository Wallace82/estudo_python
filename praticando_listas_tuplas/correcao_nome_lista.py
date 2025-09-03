lista_inicial = ['Ana', 'Carlos', 'Pedro']

nome_incorreto = input("Digite o nome incorreto:")
nome_correto = input("Digite o nome correto:")

if nome_incorreto in lista_inicial:
    lista_inicial[lista_inicial.index(nome_incorreto)] = nome_correto
    print("Lista corrigida:", lista_inicial)
else:
    print("Nome incorreto não encontrado na lista.")