distancia_percorrida = float(input("Digite a distância percorrida (em km): "))

if distancia_percorrida <= 100:
    valor_pedagio = 10.00
elif 100 < distancia_percorrida <= 200:
    valor_pedagio = 20.00
else:
    valor_pedagio = 30.00

print(f"Valor do pedágio: {valor_pedagio:.2f}")

