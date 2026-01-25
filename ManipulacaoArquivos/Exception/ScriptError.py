try: 
    #tentativa de criar um arquivo em um diretorio protegido
    with open("/protected_dir/arquivo_protegido.txt", 'w') as arquivo:
        arquivo.write("Tentando escrever em um diretório protegido.")
except PermissionError as erro:
    print("ERRO: Permissão negada ao tentar criar o arquivo!")
    print(f"Detalhes do erro: {erro}")  

try: 
    #tentativa de abrir um arquivo que ja  existe
    with open("arquivo_existente.txt", 'x') as arquivo:
        arquivo.write("Conteudo do Arquivo Existente.")
except FileExistsError as erro:
    print("ERRO: O arquivo já existe!")
    print(f"Detalhes do erro: {erro}")


try:
    #Tentativa de abrir um arquivo que não existe
    with open("arquivo_inexistente.txt", 'r') as arquivo:
        conteudo = arquivo.read()               
except FileNotFoundError as erro:
    print("ERRO: Arquivo não encontrado!")
    print(f"Detalhes do erro: {erro}")
    