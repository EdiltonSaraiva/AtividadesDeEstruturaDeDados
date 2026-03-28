print("\nVocê tem aqui um vetor com capacidade de até 50 elementos")
print("nele você indica até que posição do vetor quer ir (0 a 49)")
print("para poder preenhcer automaticamente o vetor até a posição")
print("indicada. As posições são então preenchidas com o dobro do")
print("numero do indice.\n")

tamanho_vetor = int(input("\nDigite aqui até qual posição o vetor será preenchido:\t"))

if tamanho_vetor <= 49:
    vetor_numero = [int] * (tamanho_vetor + 1)
    for numero_indice in range(0, tamanho_vetor + 1):
        vetor_numero[numero_indice] = numero_indice * 2 
    print("\nVetor Criado com Sucessso!")
    print("VETOR -", vetor_numero, "\n")
else:
    print("\nA posição indicada ultrapassa o limite de 0 a 49. Tente novamente.\n")
