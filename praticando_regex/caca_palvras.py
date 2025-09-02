import re

titulo = input("Digite o título dos livro: ")
letra_inicial = input("Digite a letra inicial para pesquisa: ")

palavras = re.findall(r'\b[' + letra_inicial.lower()+letra_inicial.upper() + ']\w*', titulo)
print(palavras)
