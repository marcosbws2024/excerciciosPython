import os

arquivo_remover = "arquivo_remover.txt"

try:
    os.remove("arquivo_remover.txt")
    print("Arquivo removido com sucesso.")

except FileNotFoundError as erro:
        print("Arquivo Inexistente!")
        print(f"Detalhes do erro {erro}")
except PermissionError as erro:
    print("ERRO: Permissão negada ao tentar remover o arquivo!")
    print(f"Detalhes do erro: {erro}")
except IsADirectoryError as erro:
    print("ERRO: Remove serve somente para Arquivos!")
    print(f"Detalhes do erro: {erro}")
    
print("Fim do programa.")