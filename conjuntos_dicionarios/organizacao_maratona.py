
participantes = { 
    "Mariana": 25, 
    "Carlos": 32, 
    "Beatriz": 28, 
    "Rafael": 35 
} 

print(f"Nomes dos participantes: {', '.join(participantes.keys())}") 

print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}") 

print("Nomes e idades dos participantes da maratona:")
for nome, idade in participantes.items():
    print(f"- {nome} : {idade} anos ")

