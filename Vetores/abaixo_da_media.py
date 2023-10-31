N = int(input("Quantos elementos vai ter o vetor? "))
vet = [0] * 100

for i in range(N):
    valor = float(input("Digite um numero: "))
    vet[i] = valor
soma = 0
for i in range(N):
    soma += vet[i]
    media_vetor = (soma/N)


print(f"Media do Vetor = {media_vetor:,.3f}\n ")

for i in range(N):
    if vet[i] < media_vetor:
        print(f"Elementos abaixo da media {vet[i]}")




