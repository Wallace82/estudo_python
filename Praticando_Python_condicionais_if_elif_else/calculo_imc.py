peso = float(input("Digite seu peso (kg):"))
altura = float(input("Digite sua altura (m):"))

imc = peso / (altura * altura)

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25:
    print("Sobrepeso")