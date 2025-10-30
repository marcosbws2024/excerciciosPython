#criando dicionario com alguma chaves

dicionario = {"Nome":"Alice",
              "Idade":20,
              "Cidade":"São Paulo"
              }

#acessando e imprimindo individualmente valores individuais usando chaves
nome = dicionario["Nome"]
idade = dicionario ["Idade"]
cidade = dicionario["Cidade"]

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Cidade: {cidade}')

#adicionando um novo par chave-valor ao dicionario
dicionario["Profissão"] = "Engenharia"
print(f'Dicionario aós adicionar profissao: {dicionario}')

#modificando o valor associado uma chave existente
dicionario["Idade"] = 26
print(f'Dicionario adicionar idade: {dicionario}')

#removendo um par de chave-valor do dicionario
del dicionario["Cidade"]
print(f'Dicionario apos remover Cidade: {dicionario}')

#acessando todas as chaves e valores do dicionario
chaves = dicionario.keys()
valores = dicionario.values()
print(f'Chaves: {list(chaves)}')
print(f'Valores: {list(valores)}')

#iterar sobre as chaves
for chave, valor in dicionario.items():
    print(f'Chave: {chave} Valor: {valor}')

#verificando se existe no dicionario
if "Nome" in dicionario:
  print(f'Nome no dicionario: {dicionario["Nome"]}')
else:
    print('A chave não existe no dicionario')

#usando o metodo get() para acessar valores de forma segura
profissao  = dicionario.get("Profissão","Desconhecido")
print(f'Profissao: {profissao}')

#limpando todos os elementos do dicionario
dicionario.clear()
print(f'Dicionario apos remover todos os elementos: {dicionario}')