print("\nCrie um vetor para ver os valores digitados na ordem inversa.\n1-Indique o tamanho do vetor.\n2-Digite os valores que irão compôr o vetor.\n")

tamanho_vetor = int(input("Digite o tamanho do vetor:\t"))
vetor_numero = [int] * tamanho_vetor
vetor_numero_invertido = [int] * tamanho_vetor

print("")

for i in range(len(vetor_numero)):
    vetor_numero[i] = int(input("Digite o valor :\t"))
print("Vetor criado com sucesso:\n", "VETOR -", vetor_numero, "\n")

for j in range(len(vetor_numero_invertido)):
    vetor_numero_invertido[j] = vetor_numero[i]
    i -= 1
print("O seu vetor com os valores na ordem iversa:\n", "VETOR -", vetor_numero_invertido, "\n")