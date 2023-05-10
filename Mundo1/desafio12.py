prod = int(input("Digite o valor do produto: "))

desc = int(input("Qual porcentagem do desconto? "))
desc = desc/100

prodesc = prod * desc
prodesc = prod - prodesc

print("O valor aplicando o desconto é {0}".format(prodesc))
