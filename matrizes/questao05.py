print("\nPreencha uma matriz que pode ter no máximo 5 linhas e 5 colunas")
print("para indicar um número. SE o numero indicado estiver presente na")
print("matriz, você verá em que linha e coluna ele se encontra. SENÃO, a")
print("a mensagem de não encontrado será exibida.\n")

print("HORA DE INDICAR A QUANTIDADE DE LINNHAS.\n")

linhas_quant = int(input("Digite a quantidade de linhas:\t"))
colunas_quant = int(input("Digite a quantidade de colunas:\t"))

if linhas_quant and colunas_quant <= 5:
    matriz_valores = [int] * linhas_quant

    for gerando_colunas in range(len(matriz_valores)):
        matriz_valores[gerando_colunas] = [int] * colunas_quant

    print("\nHORA DE PREENCHER A MATRIZ\n")
    
    for linha_valores in range(len(matriz_valores)):
        for coluna_valores in range(len(matriz_valores[linha_valores])):
            matriz_valores[linha_valores][coluna_valores] = int(input("Digite um valor:\t"))
    
    print("\nA matriz foi criada com sucesso!\n")
    print("HORA DE PROCURAR O VALOR.\n")

    valor_procurado = int(input("Digite um valor:\t"))

    valor_encontrado = False
    linha_do_valor, coluna_do_valor= -1, -1

    def gerar_matriz():
        print("\n", "A sua MATRIZ:", "\n")

        for impressao_linha in matriz_valores:
            for impressao_coluna in impressao_linha:
                print(f"{impressao_coluna:2d}", end= "   ")
            print()
            print()
        print()

    for verificando_linhas in range(len(matriz_valores)):
        for verificando_colunas in range(len(matriz_valores[linha_valores])):
            linha_do_valor, coluna_do_valor = verificando_linhas, verificando_colunas
            if matriz_valores[verificando_linhas][verificando_colunas] == valor_procurado:
                linha_do_valor, coluna_do_valor = verificando_linhas, verificando_colunas
                valor_encontrado = True
                break
            if valor_encontrado:
                break

    if valor_encontrado == True:
        print("\nO VALOR FOI ENCONTRADO!")
        gerar_matriz()
        print("OBS: Os indices de Linhas e Coluna vão de 0 até")
        print(f"o número que você indicou para a Linha ({linhas_quant} linhas) e Coluna ({colunas_quant} colunas)  menos 1.")
        print("\nO Valor", valor_procurado, "está na LINHA", linha_do_valor, " e COLUNA ", coluna_do_valor, "\n")
        
    else:
        gerar_matriz()
        print("O VALOR NÃO FOI ENCONTRADO!")
        print("-O valor que você digitou não está na presente na matriz.\n")

else:
    print("\nQuantidade de LINHAS ou COLUNAS indicado ultrapassa o limite de 5x5")
    print("Por favor, tente novamente.\n")
