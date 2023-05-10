import random

qtd = int(input("Quantos nomes deseja inserir: "))
lista = []
for i in range(qtd):
    nm = str(input("Digite o nome a ser adicionado: "))
    lista.append(nm)


random.shuffle(lista)
print(lista)