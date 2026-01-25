import os   

try:
    os.name("teste_alpha.txt","teste_beta.txt")
    print("Arquivo Renomeado!.")
    
except FileNotFoundError as erro:
        print("Arquivo Inexistente!")
        print(f"Detalhes do erro {erro}")
except PermissionError as erro:
    print("ERRO: Permissão negada ao tentar remover o arquivo!")
    print(f"Detalhes do erro: {erro}")
except FileExistsError as erro:
    print("ERRO: O arquivo já existe!")
    print(f"Detalhes do erro: {erro}")
except Exception as erro:
    print("ERRO: Ocorreu um erro inesperado!")
    print(f"Detalhes do erro: {erro}")
    
print("Fim do programa.")