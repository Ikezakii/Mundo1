nome = str(input("Digite um nome: ")).strip()
sep = nome.split()

if("SANTO" in sep[0].upper()):
    print("O nome começa com Santo")
else:
    print("O nome não comça com Santo")




