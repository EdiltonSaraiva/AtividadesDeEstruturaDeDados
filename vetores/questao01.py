iniciar = input("\nDigite 'SIM' para iniciar o programa:\t")

def mensagem_de_erro():
    print("\nErro! Por favor, digite novamente.\n")


def vetor_iniciado():
    tamanho = 7

    vetor_numero = [int] * tamanho

    vetor_numero = [1, 2, 4, 16, 32, 64, -128]

    valor_a = vetor_numero[0]
    valor_b = vetor_numero[0] 
    posicao_maior = 0 
    posicao_menor = 0
    for i in range(len(vetor_numero)):
        if vetor_numero[i] > valor_a:
            valor_a = vetor_numero[i]
            posicao_maior = i
        if vetor_numero[i] < valor_b:
            valor_b = vetor_numero[i]
            posicao_menor = i
    print("\nVocê tem um vetor com 7 valores.")
    print("O vetor tem os seguintes valores: ", vetor_numero)
    print("O maior valor do vetor: ", valor_a)
    print("A posição do maior valor: ", posicao_maior)
    print("O menor valor do vetor: " , valor_b)
    print("A posição do menor valor: ", posicao_menor, "\n")

if iniciar == "SIM":
    vetor_iniciado()
else:
    while iniciar != "SIM":
        mensagem_de_erro()
        iniciar = input("\nDigite 'SIM' para iniciar o programa:\t")
        if iniciar == "SIM":
            vetor_iniciado()