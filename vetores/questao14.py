print("\nAqui você digita 10 valores que irão ser armazenados em um vetor")
print("esses valores digitados irão ser copiados para um outro vetor que")
print("receberá os elementos do primeiro vetor, na posição decrescente no")
print("segundo vetor.\n")

vetor_x = [int] * 10
vetor_y = [int] * 10

for valores_x in range(len(vetor_x)):
    vetor_x[valores_x] = int(input("Digite um valor:\t"))

for valores_y in range(len(vetor_y)):
    vetor_y[valores_y] = vetor_x[valores_x]
    valores_x -= 1

print("VETOR -", vetor_y, "\n")
