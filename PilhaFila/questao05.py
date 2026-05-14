def calcular_estatisticas(colecao):
    if not colecao:
        return "A coleção está vazia."

    maior = colecao[0]
    menor = colecao[0]
    soma = 0

    for numero in colecao:

        if numero > maior:
            maior = numero
            
        if numero < menor:
            menor = numero

        soma += numero

    media = soma / len(colecao)

    return maior, menor, media

minha_fila = [12, 5, -3, 8, 20, 1]
maior_val, menor_val, media_val = calcular_estatisticas(minha_fila)

print(f"Fila: {minha_fila}")
print(f"Maior elemento: {maior_val}")
print(f"Menor elemento: {menor_val}")
print(f"Media: {media_val:.2f}")