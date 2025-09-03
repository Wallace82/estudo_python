lista_atual = ['Ana', 'Pedro', 'Carlos']
inserir_nome = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))
lista_atual.insert(posicao-1, inserir_nome)
print("Lista atual de convidados:", lista_atual)
