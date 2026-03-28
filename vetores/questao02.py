tamanho = 10

vetor_numero = [int] * tamanho
vetor_numero_quadrado = [int] * tamanho
print("\nPreencha um vetor com 10 números inteiros.\nPara descobrir o quadrado dos números digitados.\n")

for i in range (len(vetor_numero)):
    vetor_numero[i] = int(input("Digite aqui um número inteiro: "))

print("\nVetor criado com sucesso: ", vetor_numero)

for j in range(len(vetor_numero_quadrado)):
    vetor_numero_quadrado[j] = (vetor_numero[j] * vetor_numero[j])

print("\nO quadrado dos valores do seu vetor: ", vetor_numero_quadrado, "\n")
