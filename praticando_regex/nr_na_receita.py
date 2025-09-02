import re

url = input("Digite a descrição da receita: ")

if re.search(r'\b\d+\b', url):
    print(f"O número da receita é: {re.search(r'\b\d+\b', url).group()}")
else:
    print("Nenhum número de receita encontrado.")

