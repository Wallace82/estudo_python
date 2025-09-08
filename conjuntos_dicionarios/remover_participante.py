
participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 
print("Participantes antes da remoção:")
for workshop, nomes in participantes.items():
    print(f"- {workshop}: {', '.join(nomes)}")

nome_remover = input("Digite o nome do participante a ser removido: ")

for workshop, nomes in participantes.items():

    if nome_remover in nomes:

        nomes.remove(nome_remover)

        print(f"{nome_remover} foi removido do {workshop}.")

        break
else:
    print(f"{nome_remover} não encontrado em nenhum workshop.")

print("Participantes após a remoção:")
for workshop, nomes in participantes.items():
    print(f"- {workshop}: {', '.join(nomes)}")