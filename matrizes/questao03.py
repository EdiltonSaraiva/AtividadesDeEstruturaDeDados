print("\nUma matriz 4x4 preenchida com o produto do valor")
print("da linha e o valor da coluna de cada elemento.\n")

linha_quant, coluna_quant = 4, 4

matriz_valores = [int] * linha_quant

for gerando_colunas in range(len(matriz_valores)):
    matriz_valores[gerando_colunas] = [int] * coluna_quant

valor = 0

for linha_valores in range(len(matriz_valores)):
    for coluna_valores in range(len(matriz_valores[linha_valores])):
        matriz_valores[linha_valores][coluna_valores]  = valor
        valor += 1

for linha_produtos in range(len(matriz_valores)):
    for coluna_produtos in range(len(matriz_valores[linha_produtos])):
        matriz_valores[linha_produtos][coluna_produtos] = linha_produtos * coluna_produtos


print("\n", 6 * "-", "MATRIZ", 6 * "-")

for impressao_linha in matriz_valores:
    for impressao_coluna in impressao_linha:
        print(f"{impressao_coluna:2d}", end= "    ")
    print()
    print()
print()
