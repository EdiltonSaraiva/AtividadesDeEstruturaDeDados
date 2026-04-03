matriz_distancias = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
    ]

print("\nA Tabela abaixo representa a distância entre varias cidades:\n")

def gerar_tabela_cidades():
    print("-" * 27)
    print()
    for impressao_linhas in matriz_distancias:
        for impressao_colunas in impressao_linhas:
            print(f"{impressao_colunas:2d}", end = "    ")
        print()
        print()
    print("-" * 27)


gerar_tabela_cidades()

print("\nVocê pode interagir com os valores desta tabela:\n")
print("1 - Indique duas cidades (valores de Linha e Coluna);")
print("2 - Descubra a distância entre as cidades indicadas;")
print("3 - Veja o total percorrido.\n")

percurso_total = 0

for contagem_percurso in range(6):
    
    print("\nINDIQUE A COORDENADA:\n")

    linha_posicao_primeira_cidade = int(input("Digite o valor da Linha da cidade:\t"))
    coluna_posicao_primeira_cidade = int(input("Digite o valor da Coluna da cidade:\t"))
    
    print()

    linha_posicao_segunda_cidade = int(input("Digite o valor da Linha da cidade:\t"))
    coluna_posicao_segunda_cidade = int(input("Digite o valor da Coluna da cidade:\t"))

    if 0 <= linha_posicao_primeira_cidade < 5 and 0 <= coluna_posicao_primeira_cidade < 5 and 0 <= linha_posicao_segunda_cidade < 5 and 0 <= coluna_posicao_segunda_cidade < 5:
        valor1 = matriz_distancias[linha_posicao_primeira_cidade][coluna_posicao_primeira_cidade]
        valor2 = matriz_distancias[linha_posicao_segunda_cidade][coluna_posicao_segunda_cidade]

        distancia_entre_cidades = valor1 + valor2
        percurso_total += distancia_entre_cidades

        print("\nDistância percorrida = ", distancia_entre_cidades, "km\n")

        gerar_tabela_cidades()

    else:
        print("\nO posição da Cidade Não Existe. Linha ou Coluna Indicados")
        print("ultrapassam o limite de 5 linhas e 5 colunas. Tente novamente.\n")

print(f"\nVocê atingiu o limite de cidades para visitar. PERCURSO TOTAL = {percurso_total}km\n")
