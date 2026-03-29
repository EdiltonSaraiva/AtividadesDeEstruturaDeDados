print("\nPreencha uma matriz 4x4 para descobrir")
print("quantos valores maiores que 10 ela tem.\n")

linha_quant, coluna_quant = 4, 4

matriz_valores =  [int] * linha_quant
maiores_que_dez = 0

for gerando_colunas in range(len(matriz_valores)):
    matriz_valores[gerando_colunas] = [int] * coluna_quant
print("HORA DE INSERIR OS VALORES\n")

for valores_linha in range(len(matriz_valores)):
    for valores_coluna in range(len(matriz_valores[valores_linha])):
        matriz_valores[valores_linha][valores_coluna] = int(input("Digite um valor:\t"))
        if matriz_valores[valores_linha][valores_coluna] > 10:
            maiores_que_dez += 1

print("\nA matriz foi criada com sucesso!\n")
print("---- MATRIZ ----")
for impressao_linha in matriz_valores:
    for impressao_coluna in impressao_linha:
        print(f"{impressao_coluna:2d}", end="  ")
    print()
    print()
print("\nEssa matriz possui ", maiores_que_dez, " valores maiores que 10.\n")
