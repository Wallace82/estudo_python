texto1 = "O sol brilha forte no céu azul"
texto2 = "O céu azul anuncia um dia de sol intenso"

palavras_texto1 = set(texto1.lower().split())
palavras_texto2 = set(texto2.lower().split())

comuns = palavras_texto1.intersection(palavras_texto2)

print(f"Palavras em comum: {comuns}") 
