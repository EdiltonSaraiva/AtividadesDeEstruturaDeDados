print("\nVocê tem um vetor de 5 posições")
print("onde você irá preenchê-lo para:")
print("-Descobrir a soma dos valores;")
print("-Descobrir a multiplicação dos valores;")
print("-Ver os valores presentes no vetor.\n")

vetor_numeros = [int] * 5

soma_valores_vetor = 0
mulitiplica_valores_vetor = 1
for valores in range(len(vetor_numeros)):
    vetor_numeros[valores] = int(input("Digite um valor:\t"))
    soma_valores_vetor += vetor_numeros[valores]
    mulitiplica_valores_vetor *= vetor_numeros[valores]
print("\nTUDO PRONTO!")
print("\nOs valores digitados: ", vetor_numeros)
print("A soma dos valores: ",soma_valores_vetor)
print("A multiplicação dos valores: ", mulitiplica_valores_vetor, "\n")
