print("\nAqui você tem uma situação onde é necessário indicar a")
print("idade e a altura de 5 pessoas. Essas informações serão")
print("guardadas em vetores para que que se possa descobrir:")
print("-a média das idades;")
print("-a média das alturas;")
print("-o mais velho;")
print("-o mais novo;")
print("-o mais baixo;")
print("-o mais alto.")

vetor_idades = [int] * 5
vetor_alturas = [float] * 5
soma_idades = 0
soma_alturas = 0

print("\nHora de digitar as 5 idades.")
for idades in range(len(vetor_idades)):
    vetor_idades[idades] = int(input("Digite a idade:\t"))
    soma_idades += vetor_idades[idades]

mais_novo = vetor_idades[0]
mais_velho = vetor_idades[0]

for i in range(len(vetor_idades)):
    if vetor_idades[i] > mais_velho:
        mais_velho = vetor_idades[i]
    if vetor_idades[i] < mais_novo:
        mais_novo = vetor_idades[i]

print("\nHora de digitar as 5 alturas.")
for alturas in range(len(vetor_alturas)):
    vetor_alturas[alturas] = float(input("Digite a altura:\t"))
    soma_alturas += vetor_alturas[alturas]

mais_alto = vetor_alturas[0]
mais_baixo = vetor_alturas[0]

for j in range(len(vetor_alturas)):
    if vetor_alturas[j] > mais_alto:
        mais_alto = vetor_alturas[j]
    if vetor_alturas[j] < mais_baixo:
        mais_baixo = vetor_alturas[j]

media_idades = soma_idades / 5
media_alturas = soma_alturas / 5

print("\nInformações processadas. Vetores criados com sucesso!\n")

print("IDADES -",vetor_idades)
print("MÉDIA DAS IDADES -",media_idades)
print("MAIS NOVO -",mais_novo)
print("MAIS VELHO -", mais_velho, "\n")
print("ALTURAS -",vetor_alturas)
print("MÉDIA DAS ALTURAS -", media_alturas)
print("MAIS BAIXO -", mais_baixo)
print("MAIS ALTO -", mais_alto, "\n")
