print("\nAqui você pode criar dois vetores e preenchê-los com valores com no")
print("máximo, 10 valores cada. A partir disso, um terceiro vetor será criado")
print("contendo a soma dos valores do seu primeiro e segundo vetor.")

tamanho_vetor_a = int(input("\nDigite um tamanho para o primeiro vetor:\t"))

if tamanho_vetor_a <= 10: 
    vetor_a = [int] * tamanho_vetor_a
    soma_valores_a = 0
    for numero_vet_a in range(len(vetor_a)):
        vetor_a[numero_vet_a] = int(input("Digite um valor:\t"))
        soma_valores_a += vetor_a[numero_vet_a]
    print("\nO primeiro vetor foi criado com sucesso!")
    print("VETOR -", vetor_a)
else:
    print("O valor do tamanho digitado é muito grande.\nPor favor, tente novamente.")

print("\nAgora é a vez do próximo vetor.\n")

tamanho_vetor_b = int(input("Digite um tamanho para o segundo vetor:\t"))

if tamanho_vetor_b <= 10:
    vetor_b = [int] * tamanho_vetor_b
    soma_valores_b = 0
    for numero_vet_b in range(len(vetor_b)):
        vetor_b[numero_vet_b] = int(input("Digite um valor:\t"))
        soma_valores_b += vetor_b[numero_vet_b]
    print("\nO segundo vetor foi criado com sucesso!")
    print("VETOR -", vetor_b)
else:
    print("O valor do tamanho digitado é muito grande.\nPor favor, tente novamente.")

tamanho_vetor_c = tamanho_vetor_a + tamanho_vetor_b

vetor_c = [int] * tamanho_vetor_c 
vetor_c = vetor_a + vetor_b

print("\nO vetor com as somas dos valores do primeiro e")
print("segundo vetor já foi criado. Observe abaixo:")
print("VETOR -", vetor_c, "\n")
    