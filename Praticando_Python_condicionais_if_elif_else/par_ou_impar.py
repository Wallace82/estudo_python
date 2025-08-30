try:
    num_inteiro = int(input("Digite um número inteiro:"))

    if num_inteiro % 2 == 0:
        print(f"O número {num_inteiro} é par.")
    else:
        print(f"O número {num_inteiro} é ímpar.")
except ValueError:
       print("Por favor, digite um número inteiro válido.")