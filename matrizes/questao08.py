matriz_quadrado_magico = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
    ]

percorrer_inverso = 3
soma_linhas = [0, 0, 0]
soma_colunas = [0, 0, 0]
soma_diagonal_principal, soma_diagonal_secundaria = 0, 0

def gerar_matriz():
    for impressao_linhas in matriz_quadrado_magico:
        for impressao_colunas in impressao_linhas:
            print(f"{impressao_colunas:2d}", end = "   ")
        print()
        print()

for percorrendo_linhas in range(len(matriz_quadrado_magico)):
    for percorrendo_colunas in range(len(matriz_quadrado_magico[percorrendo_linhas])):

        valor = matriz_quadrado_magico[percorrendo_linhas][percorrendo_colunas]
        soma_linhas[percorrendo_linhas] += valor
        soma_colunas[percorrendo_colunas] += valor

        if matriz_quadrado_magico[percorrendo_linhas] == matriz_quadrado_magico[percorrendo_colunas]:
            soma_diagonal_principal += valor
        
for verificando_linhas in range(len(matriz_quadrado_magico)):
    coluna_inversa = percorrer_inverso - 1 - verificando_linhas
    soma_diagonal_secundaria += matriz_quadrado_magico[percorrendo_linhas][coluna_inversa]

def mostrar_somas():
    print("\n", 12 * "-", "LINHAS", "-" * 12)
    print("Soma dos valores da LINHA 0 é ", soma_linhas[0])
    print("Soma dos valores da LINHA 1 é ", soma_linhas[1])
    print("Soma dos valores da LINHA 2 é ", soma_linhas[2], "\n")
    print("\n", 12 * "-", "COLUNAS", "-" * 13)
    print("Soma dos valores da COLUNA 0 é ", soma_colunas[0])
    print("Soma dos valores da COLUNA 1 é ", soma_colunas[1])
    print("Soma dos valores da COLUNA 2 é ", soma_colunas[2])
    print("\n", 11 * "-", "DIAGONAIS", "-" * 11)
    print("Soma da DIAGONAL PRINCPAL é ", soma_diagonal_principal)
    print("Soma da DIAGONAL SECUNDÁRIA é ", soma_diagonal_secundaria)


if soma_linhas[percorrendo_linhas] == soma_colunas[percorrendo_colunas] and soma_diagonal_principal == soma_diagonal_secundaria:
    print("\nUMA MATRIZ QUADRADO MÁGICO 3x3:\n")
    gerar_matriz()
    mostrar_somas()
    print("\nESSA MATRIZ É UM QUADRADO MÁGICO.\n")

else:
    print("\nMATRIZ:\n")
    gerar_matriz()
    mostrar_somas()
    print("\nESSA MATRIZ NÃO É UM QUADRADO MÁGICO.\n")
