N = int(input("Quantos numeros você vai digitar: "))

vet = []

for i in range(N):
    valor = float(input("Digte os valores:"))
    vet.append(valor)

print("Numeros digitados: ")

for numero in vet:
    print(numero)
