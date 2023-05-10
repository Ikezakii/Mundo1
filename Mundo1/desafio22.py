nome = str(input("Digite seu nome: ")).strip()

print(nome.upper())
print(nome.lower())

semesp = nome.replace(" ","")
print(len(semesp))

sepa = nome.split()
print(len(sepa[0]))