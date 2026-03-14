

tamanho = 8 
vetor_numero = [int] * tamanho 
soma = 0 
valor_posicao1 = 0
valor_posicao2 = 0 

for i in range(len(vetor_numero)):
    vetor_numero[i] = int(input("Digite o valor:\t"))
valor_posicao1 = int(input("\nDigite a 1ª posicao desejada:\t"))
valor_posicao1 = int(input("Digite a 2ª posicao desejada:\t"))

for i in range(len(vetor_numero)):
    if valor_posicao1 == i:
        soma = soma + vetor_numero[i]
    if valor_posicao2 == i:
        soma = soma + valor_posicao2[i]
print(vetor_numero)
print(vetor_numero(valor_posicao1))
print(vetor_numero(valor_posicao2))
print("A soma do conteúdo das posições ", valor_posicao1, valor_posicao2, " é", soma)