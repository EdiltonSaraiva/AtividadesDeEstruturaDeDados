print("\nAqui você tem um vetor de 10 posições")
print("Indique valores para preencê-lo, para")
print("em seguida, inverter aotomáticamente")
print("esse valores e criando um novo vetor")
print("com os números invertidos.\n")

vetor_numeros = [int] * 10
vetor_numero_invertido = [int] * 10

for valores_do_vetor in range(len(vetor_numeros)):
    vetor_numeros[valores_do_vetor] = int(input("Digite um valor:\t"))

for valores_invertidos in range(len(vetor_numero_invertido)):
    vetor_numero_invertido[valores_invertidos] = vetor_numeros[valores_do_vetor]
    valores_do_vetor -= 1

print("\nOs vetores foram criados com sucesso!")
print("VETOR ORIGINAL -", vetor_numeros)
print("VETOR INVERTIDO -", vetor_numero_invertido, "\n")
    