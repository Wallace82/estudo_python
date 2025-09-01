nome = ""
senha = ""
while True:
    
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome) < 5:
        print("Nome de usuário deve ter pelo menos 5 caracteres.")
        continue
    
    if len(senha) < 8:
        print("Senha deve ter pelo menos 8 caracteres.")
        continue
    
    print("Cadastro realizado com sucesso!")
    break