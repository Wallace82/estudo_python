def calculaIdade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

input_ano_nascimento = int(input("Digite o ano de nascimento: "))
input_ano_atual = int(input("Digite o ano atual: "))

idade = calculaIdade(input_ano_nascimento, input_ano_atual)
print(f"A idade é: {idade} anos")
