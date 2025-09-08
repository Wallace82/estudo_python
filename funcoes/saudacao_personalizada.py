def saudacao_personalizada(hora, nome):
    if 0 <= hora < 12:
        return f"Bom dia, {nome}!"
    elif 12 <= hora < 18:
        return f"Boa tarde, {nome}!"
    else:
        return f"Boa noite, {nome}!"
    
hora_atual = int(input("Digite a hora atual (0-23): "))
nome_usuario = input("Digite seu nome: ")

mensagem = saudacao_personalizada(hora_atual, nome_usuario)
print(mensagem)