import random

print("\nAs temperaturas em São Luís foram anotadas diariamente durante um determinado ano.")
print("Veja abaixo: 1-A temperatura média registrada.\n2-As temparaturas que ficaram abaixo da média.\n")

tamanho = 365
k = 0
vetor_temperatura_media = [float] * tamanho
vetor_temperatura_abaixo_media = [float] * tamanho
soma  = 0
media = 0

print("***PREENHCENDO O VETOR COM VALORES AUTOMÁTICOS***\n")

for i in range(len(vetor_temperatura_media)):
    vetor_temperatura_media[i] = round(random.uniform(20, 35), 2)
    soma = soma + vetor_temperatura_media[i]

media = soma/tamanho

for j in range(len(vetor_temperatura_media)):
    if vetor_temperatura_media[j] < media:
        vetor_temperatura_abaixo_media[k] = vetor_temperatura_media[j]
        k += 1
print("A média das temperaturas registrada foi %.2f" % media)
print("\nOs valores que ficaram abaixo da média: ", vetor_temperatura_abaixo_media, "\n")
