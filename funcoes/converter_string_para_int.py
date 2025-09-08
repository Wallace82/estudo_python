
telefones = ["1198D7654321", "21912345678", "31987654321", "11911223344"] 

def converter_string_para_int(lista_telefones):
    telefones_convertidos = []
    for telefone in lista_telefones:
        try:
            numero = int(telefone)
            telefones_convertidos.append(numero)
        except ValueError:
            print(f"Erro ao converter o telefone {telefone}. Ignorando este número.")
    return telefones_convertidos

telefones_convertidos = converter_string_para_int(telefones)

verificar = len(telefones_convertidos) == len(telefones)

if verificar:
    print("Todos os números foram convertidos com sucesso:")
    print(telefones_convertidos)
else:
    print("Nem todos os números foram convertidos. Números convertidos:")
    print(telefones_convertidos)