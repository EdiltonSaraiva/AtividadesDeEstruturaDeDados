print("\nPreencha uma matriz 3x3 para descobrir:")
print("-A soma dos números ímpares fornecidos;")
print("-A soma de cada uma das 3 colunas;")
print("-A soma de cada uma das 3 linhas.")

linhas_quant, colunas_quant = 3, 3

matriz_Valores = [int] * linhas_quant

for gerando_colunas in range(len(matriz_Valores)):
    matriz_Valores[gerando_colunas] = [int] * colunas_quant

print("\nHORA DE PREENCHER A MATRIZ\n")

for linha_valores in range(len(matriz_Valores)):
    for coluna_valores in range(len(matriz_Valores[linha_valores])):
        matriz_Valores[linha_valores][coluna_valores] = int(input("Digite um valor:\t"))

print("\nA matriz foi criada com sucesso!\n")

soma_impares = 0
soma_linhas = [0, 0, 0]
soma_colunas = [0, 0, 0]

for percorrendo_linhas in range(len(matriz_Valores)):
    for percorrendo_colunas in range(len(matriz_Valores[linha_valores])):
        valor = matriz_Valores[percorrendo_linhas][percorrendo_colunas]
        soma_linhas[percorrendo_linhas] += valor
        soma_colunas[percorrendo_colunas] += valor
        if valor % 2 != 0: 
            soma_impares += valor

print("A sua Matriz:\n")

for impressao_linhas in matriz_Valores:
    for impressao_colunas in impressao_linhas:
        print(f"{impressao_colunas:2d}", end= "   ")
    print()
    print()

print("\nOBS: os índices das linhas e colunas vão de 0 a 3.\n")
print("A soma dos números ímpares presentes na matriz é ", soma_impares, "\n")
print("-" * 14, "LINHAS", "-" * 15)
print("A soma dos valores da LINHA 0 é ", soma_linhas[0])
print("A soma dos valores da LINHA 1 é ", soma_linhas[1])
print("A soma dos valores da LINHA 2 é ", soma_linhas[2], "\n")
print("-" * 14, "COLUNAS", "-" * 14)
print("A soma dos valores da COLUNA 0 é ", soma_colunas[0])
print("A soma dos valores da COLUNA 1 é ", soma_colunas[1])
print("A soma dos valores da COLUNA 2 é ", soma_colunas[2], "\n")
