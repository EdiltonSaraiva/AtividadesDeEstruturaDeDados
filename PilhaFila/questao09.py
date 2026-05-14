print("\nAqui você pode digitar um número de base decimal")
print("para convertê-lo para número de base binária.")

def decimal_para_binario(numero):
    pilha = []

    while numero > 0:
        resto = numero % 2
        pilha.append(resto)
        numero = numero // 2

    binario = ""

    while len(pilha) > 0:
        binario += str(pilha.pop())

    return binario

numero = int(input("Digite um número decimal: "))

print(f"Binário: {decimal_para_binario(numero)}")