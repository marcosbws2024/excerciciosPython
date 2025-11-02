import  time
data_atual = int(time.strftime("%Y"))
contMaior=0
contMenor=0

for i in range(0,8):
    nasc = int(input("Data Nascimento: "))
    idade = data_atual - nasc
    if(idade>=21):
        contMaior+=1
    else:
        contMenor+=1
        
print("A quantidade de Pessoas maior de idade é: {}".format(contMaior))
print("A quantidade de Pessoas menor de idade é: {}".format(contMenor))
