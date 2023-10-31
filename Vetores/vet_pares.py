N = int(input("Informe quantos números vai digitar: "))

pares = [0] * 100

for i in range(N):
    pares[i] = int(input("Digite um numero: "))


count_pares = 0

print("Numeros Pares: ")
for i in range(N):
    if pares[i] % 2 == 0:
        print(pares[i], " ")
        count_pares += 1

print("\n")

print(f"Quantidade de pares = {count_pares}")



