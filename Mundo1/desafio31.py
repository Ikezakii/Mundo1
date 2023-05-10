num =float(input("Digite  distancia: "))

if num > 200:
    print("O preço a pagar é {0}".format(num*0.50))
else:
    print("O preço a pagar é {0}".format(num*0.45))