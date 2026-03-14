#. Ler um conjunto de números inteiros, armazenando-o em um vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

tamanho = 10
vetor_numero = [int] * tamanho
vetor_numero_quadrado = [int] * tamanho
print("Preencha um vetor com 10 números inteiros.\nPara descobrir o quadrado dos numeros digitados.\n")

for i in range (len(vetor_numero)):
    vetor_numero[i] = int(input("Digite aqui um número inteiro: "))
print("\nVetor criado com sucesso: ", vetor_numero)

for j in range(len(vetor_numero_quadrado)):
    vetor_numero_quadrado[j] = (vetor_numero[j] * vetor_numero[j])
print("\nO quadrado dos valores do seu vetor: ", vetor_numero_quadrado)

