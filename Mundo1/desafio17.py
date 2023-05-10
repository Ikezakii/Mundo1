import random

qtd = int(input("Quantos nomes deseja inserir: "))
lista = []
for i in range(qtd):
    nm = str(input("Digite o nome a ser adicionado: "))
    lista.append(nm)

print("O nome sorteado foi {0}".format(random.choice(lista)))