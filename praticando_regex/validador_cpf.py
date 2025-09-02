import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
