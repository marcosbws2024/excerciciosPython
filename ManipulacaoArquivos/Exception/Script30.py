import os
import errno 

try: 
    os.mkdir("meu_diretorio")
    print("Diretório criado com sucesso.")
except OSError as erro:
    print(erro.errno)
    if erro.errno == errno.ENOTEMPTY:
        print("ERRO: O diretório já existe!")
    else:
        print("ERRO: Um erro inesperado ocorreu ao tentar criar o diretório!")
    print(f"Detalhes do erro: {erro}")
    
print("Fim do programa.")