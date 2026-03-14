import random

tamanho = 365
k = 0
vetor_temperatura_media = [float] * tamanho
vetor_temperatura_abaixo_media = [float] * tamanho
soma  = 0
media = 0

for i in range(len(vetor_temperatura_media)):
    vetor_temperatura_media[i] = round(random.uniform(20, 35), 2)
    soma = soma + vetor_temperatura_media[i]

media = soma/tamanho

for j in range(len(vetor_temperatura_media)):
    if vetor_temperatura_media[j] < media:
        vetor_temperatura_abaixo_media[k] = vetor_temperatura_media[j]
        k = k + 1
print("A média das temperaturas %.2f" % media)
print(vetor_temperatura_abaixo_media)
