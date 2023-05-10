dias = float(input("Quandos dias foram alugados? "))
dias = dias * 60

k = float(input("Quantos quilometros rodados? "))
k = k * 0.15

total = k+dias

print("O preço a pagar é {0}".format(total))