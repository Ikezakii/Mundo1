import random

acerto = 0

num = random.randint(0,5)




while acerto < 1:
        resp = int(input("Digite o numero que voce acha correto: "))
        if(resp == num):
            print("Voce acertou, o numero era {0}".format(num))
            acerto +=1
        else:
            print("Voce errou, o numero não era {0}".format(resp))