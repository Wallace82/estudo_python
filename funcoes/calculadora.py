soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero!"

input1 = float(input("Digite o primeiro número: "))
input2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (| + | - | * | / |): ")

if operacao == '+':
    resultado = soma(input1, input2)
elif operacao == '-':
    resultado = subtracao(input1, input2)
elif operacao == '*':
    resultado = multiplicacao(input1, input2)
elif operacao == '/':
    resultado = divisao(input1, input2)
else:
    resultado = "Operação inválida!"

print(f"Resultado: {resultado}")