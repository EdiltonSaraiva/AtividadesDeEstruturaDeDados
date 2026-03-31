matriz_distancias = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
    ]

print("\nA Tabela abaixo representa a distância entre varias cidades:\n")

for impressao_linhas in matriz_distancias:
    for impressao_colunas in impressao_linhas:
        print(f"{impressao_colunas:2d}", end = "    ")
    print()
    print()

print("\nVocê pode interagir com os valores desta tabela:\n")
print("1 - Indique duas cidades (valores de Linha e Coluna);")
print("2 - Descubra a distância entre as cidades indicadas;")
print("3 - Veja o total percorrido.\n")

distancia_cidades = [int] * 6
distancia_percorrida, percurso_total = 0, 0

for contagem_percurso in range(len(distancia_cidades)):
    
    print("\nINDIQUE A COORDENADA:\n")

    linha_posicao_primeira_cidade = int(input("Digite o valor da Linha da cidade:\t"))
    coluna_posicao_primeira_cidade = int(input("Digite o valor da Coluna da cidade:\t"))
    
    print()

    linha_posicao_segunda_cidade = int(input("Digite o valor da Linha da cidade:\t"))
    coluna_posicao_segunda_cidade = int(input("Digite o valor da Coluna da cidade:\t"))

    if linha_posicao_primeira_cidade + coluna_posicao_primeira_cidade <= 10 and linha_posicao_segunda_cidade + coluna_posicao_segunda_cidade <= 10:
        
        for adicionando_distancia in range(len(distancia_cidades)):
            distancia_cidades[adicionando_distancia] = matriz_distancias[linha_posicao_primeira_cidade][coluna_posicao_primeira_cidade] + matriz_distancias[linha_posicao_segunda_cidade][linha_posicao_segunda_cidade]
            percurso_total = matriz_distancias[adicionando_distancia]
            percurso_total += 1

            print("\nDistância percorrida = ", percurso_total[adicionando_distancia], "km\n")

    else:
        print("\nO posição da Cidade Não Existe. Linha ou Coluna Indicados")
        print("ultrapassam o limite de 5 linhas e 5 colunas. Tente novamente.\n")

print(f"\nPercurso total = {distancia_cidades[0]} + {distancia_cidades[1]} + {distancia_cidades[2]} + {distancia_cidades[3]} + {distancia_cidades[4]} + {distancia_cidades[5]} = {percurso_total}km\n")