tamanho = 8

vetor_numero = [int] * tamanho 
soma = 0 
valor_posicao1 = 0
valor_posicao2 = 0 

print("\nVocê tem disponível um vetor de 8 posições (0 a 7).\nVocê dita os números que irão compôr o vetor (somente números inteiros).\n")

for i in range(len(vetor_numero)):
    vetor_numero[i] = int(input("Digite um número inteiro:\t"))
print("O vetor foi criado com sucesso.\n")
print("VETOR -", vetor_numero,"\n")

print("Você também pode digitar duas posições para somar os valores que nela se encontram.\nAs posições vão de 0 a 7.")
valor_posicao1 = int(input("\nDigite a 1ª posicao desejada:\t"))
valor_posicao2 = int(input("Digite a 2ª posicao desejada:\t"))

for i in range(len(vetor_numero)):
    if valor_posicao1 == i:
        soma = soma + vetor_numero[i]
    if valor_posicao2 == i:
        soma = soma + vetor_numero[i]

print("\n1ª posição digitada: ", vetor_numero[valor_posicao1])
print("2ª posição digitada: ", vetor_numero[valor_posicao2])
print("A soma do conteúdo das posições é", soma, "\n")
