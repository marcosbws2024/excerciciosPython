import os 

try:
    entradas = os.scandir("diretorio_inexistente")
    
    for obj in entradas:
        print(obj.name) 
        print("Nome: ", obj.name)   
        print("Caminho: ", obj.path)
        print("É diretório? ", obj.is_dir())
        print("É arquivo? ", obj.is_file())
        
        if obj.is_file():
            tamanho = os.path.getsize(obj.path)
            print("Tamanho do arquivo em bytes: ", tamanho,"8")
except FileNotFoundError as erro:
    print("ERRO: O diretório não foi encontrado!")
    print(f"Detalhes do erro: {erro}")
except NotADirectoryError as erro:
    print("ERRO: O caminho especificado não é um diretório!")
    print(f"Detalhes do erro: {erro}")