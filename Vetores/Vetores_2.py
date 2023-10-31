N = int(input("Quantos números você vai digitar: "))

vet = []

for i in range(N):
    valor = float(input("Digite o numero: "))
    if valor < 0:
        vet.append(valor)



print("Numeros Negativos: ")

for numero_neg in vet:
    print(int(numero_neg))

