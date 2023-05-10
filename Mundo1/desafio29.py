vel = int(input("Digite a velocidade: "))

if vel > 80:
    mul = vel - 80
    mul = mul * 7
    print("Voce ultrapassou o limite, e terá que pagar {0}".format(mul))
else:
    print("Voce está dentro dos limites")