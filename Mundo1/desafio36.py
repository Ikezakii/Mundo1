valcasa = float(input("Qual valor da casa? R$"))
sala = float(input("Qual o seu salário? R$"))
tempo = int(input("Em quantos anos voce deseja pagar a casa? "))
tempo = tempo * 12
parcela = valcasa / tempo
minimo = sala*30/100

if parcela > minimo:
    print("O empréstimo não pode ser realizado!!")
else:
    print("Tudo certo, o valor mensal de sua parcela será R${:.2f} durante {} meses".format(round(parcela),tempo))
