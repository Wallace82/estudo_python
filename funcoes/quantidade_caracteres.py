def quantidadeCaracteres(texto):
    return len(texto)

input_texto = input("Digite uma palavra: ")
quantidade = quantidadeCaracteres(input_texto)
print(f"A quantidade de caracteres é: {quantidade}")