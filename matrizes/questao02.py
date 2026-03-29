print("\n", "--MATRIZ IDENTIDADE 5x5--\n")

linha_quant, coluna_quant = 5, 5

matriz_identidade = [int] * linha_quant

for gerando_colunas in range(len(matriz_identidade)):
    matriz_identidade[gerando_colunas] = [int] * coluna_quant

for indice_linha in range(len(matriz_identidade)):
    for indice_coluna in range(len(matriz_identidade[indice_linha])):
        matriz_identidade[indice_linha][indice_coluna] = 0
        if indice_linha == indice_coluna:
            matriz_identidade[indice_linha][indice_coluna] = 1

for impressao_linha in matriz_identidade:
    for impressao_coluna in impressao_linha:
        print(f"{impressao_coluna:2d}", end="    ")
    print()
    print()
print()
