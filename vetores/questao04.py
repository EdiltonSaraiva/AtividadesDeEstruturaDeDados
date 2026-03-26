tamanho = 100
vetor_numero = [int] * tamanho
resposta = ""

print("\nAo inicializar, você criará um vetor que vai de 1 a 100.")
resposta = input("Para iniciar o vetor digite SIM:\t")

if resposta == "SIM":
    for i in range(len(vetor_numero)):
        vetor_numero[i] = i + 1
    print("\nVetor criado com sucesso!\n")
    for j in range(len(vetor_numero)):
        print(vetor_numero[j], " ")
    print("")
else:
    print("\nResposta não reconhecida. Por favor, tente novamente.\n") 
