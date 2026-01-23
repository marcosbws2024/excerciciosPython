with open("dados13.txt", "r") as arquivo:
   print("Total de linhas no Arquivo: ")
   contador = 0
   for linha in arquivo:
    if linha:
       contador += 1
    print("Total = ",contador)