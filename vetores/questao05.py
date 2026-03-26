tamanho = 0
maior_valor = 0
menor_valor = 1
print("\nVocê pode criar um vetor com o tamanho máximo de 20 posições e depois preenchê-lo")
print("com valores para descobrir quais são o maior e o menor valor nele presentes.")

tamanho = int(input("\nDigite um tamanho para o seu vetor: "))
vetor_numero = [int] * tamanho

if tamanho > 20:
    print("\nO valor digitado ultrapassa o limite permitido! Tente novamente.\n")
elif tamanho <= 0:
    print("\nValor muito pequeno, impossível criar vetor! Tente novamente.\n")
else:
    for i in range(len(vetor_numero)):
        vetor_numero[i] = int(input("Digite um valor: "))
    print("\nVetor criado com sucesso!\n")
    for j in range(len(vetor_numero)):
        if vetor_numero[j] > maior_valor:
            maior_valor = vetor_numero[j]
        elif vetor_numero[j] <= menor_valor:
            menor_valor = vetor_numero[j]
    print("VETOR -", vetor_numero)
    print("\nO MENOR valor presente no vetor é: ", menor_valor)
    print("O MAIOR valor presente no vetor é:", maior_valor, "\n")
