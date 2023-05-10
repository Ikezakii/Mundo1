nome = str(input("Digite uma frase: ")).strip()

print(nome.upper().count("A"))
print(nome.upper().find("A")+1)
print(nome.upper().rfind("A")+1)
