N = int(input("Informe quantos número você vai digitar: "))
vet = []
somar = 0

for i in range(N):
    valor = float(input("Digite o numero: "))
    somar += valor
    media = somar/N

print(f"Valores:{valor} \n Soma:{somar}\n Media:{media}")

