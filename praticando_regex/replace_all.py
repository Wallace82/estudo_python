texto = input("Digite o texto a ser revisado: ")
palavra_antiga = input("Qual palavra deseja substituir? ")
palavra_nova = input("Qual a nova palavra? ")

texto = texto.replace(palavra_antiga, palavra_nova)

print("Texto revisado:")
print(texto)