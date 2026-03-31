print("\nPreencha duas matrizes com quantidades de Linhas e Colunas")
print("limitadas até no máximo 4 e uma terceira matriz será criada")
print("comparando os valores elemento por elemento das duas matrizes")
print("e selecionando apenas os maiores valores, mostrando no final:\n")
print("- a primeira matriz;")
print("- a segunda matriz;")
print("- a terceira matriz.\n")


linhas_quant_primeira = int(input("Digite a quantidade de Linhas e Colunas das Matrizes:\t"))

if linhas_quant_primeira <= 4:

    colunas_quant_primeira = linhas_quant_primeira

    linhas_quant_segunda = linhas_quant_primeira
    colunas_quant_segunda = linhas_quant_primeira

    linhas_quant_terceira = linhas_quant_primeira
    colunas_quant_terceira = linhas_quant_primeira

    primeira_matriz = [int] * linhas_quant_primeira

    for gerando_colunas_primeira in range(len(primeira_matriz)):
        primeira_matriz[gerando_colunas_primeira] = [int] * colunas_quant_primeira

    print("\nHORA DE PREENCHER A PRIMEIRA MATRIZ\n")

    for linha_valores_primeira in range(len(primeira_matriz)):
        for coluna_valores_primeira in range(len(primeira_matriz[linha_valores_primeira])):
            primeira_matriz[linha_valores_primeira][coluna_valores_primeira] = int(input("Digite um valor:\t"))
    print("\nA Primeria Matriz foi criada com sucesso!")

    segunda_matriz = [int] * linhas_quant_segunda

    for gerando_colunas_segunda in range(len(segunda_matriz)):
        segunda_matriz[gerando_colunas_segunda] = [int] * colunas_quant_segunda
    
    print("\nHORA DE PREENCHER A SEGUNDA MATRIZ\n")

    for linha_valores_segunda in range(len(segunda_matriz)):
        for coluna_valores_segunda in range(len(segunda_matriz[linha_valores_segunda])):
            segunda_matriz[linha_valores_segunda][coluna_valores_segunda] = int(input("Digite um valor:\t"))
    print("\nA Segunda Matriz foi gerada com sucesso!\n")

    terceira_matriz = [int] * linhas_quant_terceira

    for gerando_colunas_terceira in range(len(terceira_matriz)):
        terceira_matriz[gerando_colunas_terceira] = [int] * colunas_quant_terceira
    
    for linha_valores_terceira in range(len(terceira_matriz)):
        for coluna_valores_terceira in range(len(terceira_matriz[linha_valores_terceira])):
            if primeira_matriz[linha_valores_terceira][coluna_valores_terceira] > segunda_matriz[linha_valores_terceira][coluna_valores_terceira]:
                maior_valor = primeira_matriz[linha_valores_terceira][coluna_valores_terceira]
                terceira_matriz[linha_valores_terceira][coluna_valores_terceira] = maior_valor
            else:
                maior_valor = segunda_matriz[linha_valores_terceira][coluna_valores_terceira]
                terceira_matriz[linha_valores_terceira][coluna_valores_terceira] =  maior_valor
    print("\nA Terceira Matriz foi criada com sucesso!\n")

    print("\nA PRIMEIRA MATRIZ:\n")
    for imprimir_linhas_primeira in primeira_matriz:
        for imprimir_colunas_primeira in imprimir_linhas_primeira:
            print(f"{imprimir_colunas_primeira:2d}", end = "   ")
        print()
        print()
    print()

    print("\nA SEGUNDA MATRIZ:\n")
    for imprimir_linhas_segunda in segunda_matriz:
        for imprimir_colunas_segunda in imprimir_linhas_segunda:
            print(f"{imprimir_colunas_segunda:2d}", end = "   ")
        print()
        print()
    print()

    print("\nA TERCEIRA MATRIZ:\n")
    for imprimir_linhas_terceira in terceira_matriz:
        for imprimir_colunas_terceira in imprimir_linhas_terceira:
            print(f"{imprimir_colunas_terceira:2d}", end = "   ")
        print()
        print()
    print()    

else:
    print("\nQuantidades de Linhas ou Colunas indicados para as matrizes")
    print("ultrapassou o limite 4. Por favor, tente novamente.\n")
