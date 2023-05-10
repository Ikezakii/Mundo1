a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))

menor = a
if b<a and b<c:
    menor = b
if c<a and b>c:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and b<c:
    maior = c

print("Menor numero: {0}".format(menor))
print("Maior numero: {0}".format(maior))