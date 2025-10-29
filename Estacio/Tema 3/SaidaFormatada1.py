nome = "João"
idade = 25
altura = 1.75

saida_formatada = f"Nome:{nome}, Idade:{idade},Altura: {altura:.2f}m"
print(saida_formatada)

hora =  10
minutos = 26
segundos = 18
print(str(hora) + ":" + str(minutos) + ":" + str(segundos))
print(f"{hora}:{minutos}:{segundos}")
print('{}:{}:{}'.format(hora,minutos,segundos))

# colocando espaco na impressao
print('{:4},{:5}'.format(10,100))
print('{:8.5}' .format(10/3))

seq = [0,1,2,3,4,5,6,7,8,9]
print(seq)

str = "Hello World"
print(str[0:5])
print(str[5:11])
print(str[::-1])
print(str[4:0:-1])
