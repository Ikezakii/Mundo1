
lista = []
total = 0
qtd = int(input("Quantos numeros deseja inserir? "))

for i in range(qtd):
 n = int(input("Digite um número: "))
 lista.append(n)
 total = total + n


media = total / len(lista)

print("A média é {0}".format(media))