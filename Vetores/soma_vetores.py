N = int(input("Informe quantos valores vai ter cada vetor:  "))
a = [0] * 100
b = [0] * 100
c = [0] * 100

print(f"Digite os valores do vetor A: ")
for i in range(N):
    valor = int(input())
    a[i] = valor

print(f"Digite os valores do vetor B: ")
for i in range(N):
    valor_2 = int(input())
    b[i] = valor_2

for i in range(N):
    c[i] = (a[i] + b[i])

print("Vetor Resultante: ")
for i in range(N):
    print(c[i])

