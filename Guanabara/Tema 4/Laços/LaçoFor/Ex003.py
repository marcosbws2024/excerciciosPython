soma=0
qtdeValor=0
for i in range(1,501,2):
     if i%3==0:
         soma=soma +i
         qtdeValor+=1

print("A soma dos {} numeros é:{}".format(qtdeValor,soma))       
       
#print('*'*15)
#for i in range(1, 501, 2):
 #   print(i)