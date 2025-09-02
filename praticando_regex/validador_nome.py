import re

nome = input("Digite o nome do cliente para validação: ")

if re.match(r'^[A-Z][a-z]+', nome):
    print("Nome válido.")
else:
    print("Nome inválido.")
