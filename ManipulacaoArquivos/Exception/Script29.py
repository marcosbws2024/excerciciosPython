import os

try:
    os.rmdir("meu_diretorio")
    print("Diretório removido com sucesso.")
    
except FileNotFoundError as erro:
    print("ERRO: O diretório não foi encontrado!")
    print(f"Detalhes do erro: {erro}")
except PermissionError as erro:
    print("ERRO: Permissão negada ao tentar remover o diretório!")
    print(f"Detalhes do erro: {erro}")
except OSError as erro:
    print("ERRO: O diretório não está vazio ou ocorreu outro erro de sistema!")
    print(f"Detalhes do erro: {erro}")

print("Fim do programa.")