print("Antes do While")
palavra =input("Digite a palavra Sair para parar o loop: ")
palavraformatada = palavra.lower().strip()
while palavraformatada != "sair":
    palavraformatada = input("Digite uma palavra Sair para parar o loop: ")
print("Voce digitou sair")