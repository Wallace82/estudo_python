def filtrar_numeros_pares(numeros):
    return list(filter(lambda x: x % 2 == 0, numeros))

input_numeros = input("Digite uma lista de números separados por espaços: ")
print("Números pares:", filtrar_numeros_pares(list(map(int, input_numeros.split()))))


