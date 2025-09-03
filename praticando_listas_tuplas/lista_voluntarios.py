lista_voluntarios = []

while True:
    voluntario = input("Digite o nome do voluntário (ou 'sair' para encerrar):")
    if voluntario == "sair":
        break

    if voluntario in lista_voluntarios:
        print("O voluntário já está na lista.")
    else:
        lista_voluntarios.append(voluntario)
        print(f"O voluntário {voluntario} foi adicionado à lista.")

    print("Lista de voluntários:", lista_voluntarios)
