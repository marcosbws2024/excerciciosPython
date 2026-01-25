import os

try:
    os.mkdir("meu_diretorio")
    print("Diretório criado com sucesso.")
except FileExistsError as erro:
    print("ERRO: O diretório já existe!")
    print(f"Detalhes do erro: {erro}")  
except PermissionError as erro:
    print("ERRO: Permissão negada ao tentar criar o diretório!")
    print(f"Detalhes do erro: {erro}")
    
print("Fim do programa.")