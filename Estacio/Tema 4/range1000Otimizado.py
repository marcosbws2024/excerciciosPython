for raiz in range(32, 99):
    num = raiz * raiz#calcula o numero gerado da raiz
    menor = num %100 #obtem o numero de algarismos  menos significativos
    maior =  num //100 #obtem o numero dos algarismos mais significativos

    if(menor + maior) == raiz:
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print("Terminou")
print("Saiu ", raiz)