lista_laura = set(['leite', 'pão', 'café', 'açúcar'])
lista_ana = set(['pão', 'café', 'biscoito', 'chocolate'])

print("Itens que Laura tem e Ana não:")
print(lista_laura - lista_ana)


print("Itens que Ana tem e Laura não:")
print(lista_ana - lista_laura)

print("Itens que ambos têm:")
print(lista_laura.intersection(lista_ana))
