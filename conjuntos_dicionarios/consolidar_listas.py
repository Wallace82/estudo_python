
equipe_a = set({"planejar reunião", "revisar documento", "testar sistema"})
equipe_b = set({"testar sistema", "implementar funcionalidade", "corrigir bug"})

equipe_unificada = equipe_a.union(equipe_b)

tarefa_remover = input("Tarefa a ser removida: ").lower()  

if tarefa_remover in equipe_unificada:  
    equipe_unificada.remove(tarefa_remover) 

print(F"Tarefas unificadas da equipe: {equipe_unificada}")


