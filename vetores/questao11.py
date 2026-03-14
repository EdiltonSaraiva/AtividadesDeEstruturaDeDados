#. Crie um programa que lê 6 valores inteiros usando vetores e, em seguida, mostre na tela os valores lidas na ordem inversa.

tamanho = 6
vetor_numero = [int] * tamanho
vetor_numero_invertido = [int] * tamanho

for i in range(len(vetor_numero)):
    vetor_numero[i] = int(input("Digite o valor :\t"))
print("Vetor criado com sucesso \t ", vetor_numero, "\n")

for j in range(len(vetor_numero_invertido)):
    vetor_numero_invertido[j] = vetor_numero[i]
    i -= 1
print("O seu vetor com os valores na ordem iversa:\t", vetor_numero_invertido, "\n")