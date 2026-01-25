print("Abrindo arquivo...")

try: 
    open("teste.txt", 'r')
    print("Arquivo aberto com sucesso!")
except FileNotFoundError as erro:
    print("ERRO: Arquivo não encontrado!")
    print(f"Detalhes do erro: {erro}") 
except PermissionError as erro:
    print("ERRO: Você não tem permissão para acessar este arquivo!")
    print(f"Detalhes do erro: {erro}")

print("Termino do programa...")