print("\nPreenhca uma matriz 4x4 com valores para")
print("descobrir a localização (linha e coluna)")
print("do maior valor presente na matriz.\n")

linha_quant, coluna_quant = 4, 4

matriz_valores = [int] * linha_quant

for gerando_colunas in range(len(matriz_valores)):
    matriz_valores[gerando_colunas] = [int] * coluna_quant

print("HORA DE PREENHCER A MATRIZ.\n")

for indice_linhas in range(len(matriz_valores)):
    for indice_colunas in range(len(matriz_valores[indice_linhas])):
        matriz_valores[indice_linhas][indice_colunas] = int(input("Digite um valor:\t"))

maior_valor = matriz_valores[0][0]
linha_maior_valor, coluna_maior_valor = 0, 0

for percorrendo_linhas in range(len(matriz_valores)):
    for percorrendo_colunas in range(len(matriz_valores[indice_linhas])):
        if matriz_valores[indice_linhas][indice_colunas] > maior_valor:
            maior_valor = matriz_valores[percorrendo_linhas][percorrendo_colunas]
            linha_maior_valor, coluna_maior_valor = percorrendo_linhas, percorrendo_colunas

print("\nMatriz criada com sucesso!\n")

print("-" * 22)
for impressao_linha in matriz_valores:
    for impressao_coluna in impressao_linha:
          print(f"{impressao_coluna:2d}", end= "    ")
    print()
    print()
print("-" * 22)

print("OBS: linhas e colunas vão de 0 a 3.")
print("O maior valor da matriz é", maior_valor, " que se encontra na LINHA ", linha_maior_valor," e COLUNA ", coluna_maior_valor,".\n")
