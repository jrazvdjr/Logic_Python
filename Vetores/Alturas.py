N = int(input("Informe o número de pessoas que ira cadastrar: "))

nomes = [0] * 10
idades = [0] * 10
altura = [0.0] * 10



for i in range(N):
    print(f"Dados da {i+1} pessoa")
    nomes[i] = input("Digite o nome: ")

    idades[i] = int(input("Digite a idade: "))

    altura[i] = float(input("Digite a altura: "))

    print("---"*20)

altura_media = sum(altura) / N
print()
print(f"Altura media é {altura_media}")


cont = 0
for i in range(N):
    if idades[i] < 16:
        cont += 1

porcentagem = cont * 100 / N
print(f"Pessoas menores de 16 equivalem a {porcentagem}% ")

for i in range(N):
    if idades[i] < 16:
        print(nomes[i])
