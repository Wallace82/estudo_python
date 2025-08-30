notas = []
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas.append(nota1)
notas.append(nota2)
notas.append(nota3)

media = (sum(notas)) /  len(notas)

print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif 5 <= media < 7:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")