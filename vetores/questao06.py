print("\nAqui você tem um vetor de até no máximo 50 posições, onde você pode")
print("inserir valores e, feito isso, verá  a  soma dos valores do vetor.")

tamanho_vetor = int(input("\nDigite um tamanho para o vetor:\t"))

if tamanho_vetor <= 50:
    print()
    soma_numeros = 0
    vetor_numero = [int] * tamanho_vetor
    for numeros in range(len(vetor_numero)):
        vetor_numero[numeros] = int(input("Digite o número:\t"))
        soma_numeros += vetor_numero[numeros]
    print("\nVetor Criado com Sucesso!\n")
    print("VETOR -", vetor_numero)
    print("Soma dos valores presentes no vetor: ", soma_numeros, "\n")
elif tamanho_vetor == 0 or tamanho_vetor < 0:
    print("\nTamanho indicado muito pequeno. Por favor, tente novamente.\n")
else:
    print("\nTamanho indicado muito grande. Por favor, tente novamente.\n")
