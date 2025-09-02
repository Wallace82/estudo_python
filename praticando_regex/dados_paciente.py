import re

nome_paciente = input("Digite o nome completo e o ano de nascimento do paciente: ")

padrao = r'(?P<nome>[A-Za-z\s]+) (?P<ano>\d{4})'
resultado = re.match(padrao, nome_paciente)

if resultado:
    print("Saída esperada:")
    print("Primeiro Nome:", resultado.group("nome").split()[0])
    print("Sobrenome:", resultado.group("nome").split()[-1])
    print("Ano de Nascimento:", resultado.group("ano"))
else:
    print("Entrada inválida.")