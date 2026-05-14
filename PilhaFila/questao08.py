from collections import deque

fila_tarefa = []

fila_tarefa.append("A")
fila_tarefa.append("B")
fila_tarefa.append("C")

print("Fila:")

tarefa = ""

print(f"Processando tarefa {fila_tarefa[0]}...")
print(f"Processando tarefa {fila_tarefa[1]}...")
print(f"Processando tarefa {fila_tarefa[2]}...")

while len(fila_tarefa) > 0:
   
       tarefa = fila_tarefa.pop(0)

print("Todas as tarefas foram processadas.")