from pathlib import Path

def main():
    # 1. Define o local do arquivo: sempre na mesma pasta onde este script está
    # .parent pega a pasta do script, / junta com o nome do arquivo
    caminho_pasta = Path(__file__).parent.resolve()
    caminho_arquivo = caminho_pasta / "meu_arquivo.txt"

    print(f"--- Iniciando Script em: {caminho_pasta} ---")

    # 2. Coleta de dados
    print("Digite suas frases. Digite 'sair' para terminar.")
    frases = []
    while True:
        entrada = input("> ").strip()
        if entrada.lower() == "sair":
            break
        if entrada:  # Evita salvar linhas vazias
            frases.append(entrada)
    
    # 3. Escrita Inicial (Garante a criação do arquivo)
    try:
        # O modo 'w' cria o arquivo. Usamos encoding utf-8 para evitar erro de acentos
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            for frase in frases:
                arquivo.write(frase + "\n")
        print("\n[OK] Arquivo original criado com sucesso.")

        # 4. Leitura e Manipulação (Tudo em memória primeiro)
        if caminho_arquivo.exists():
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                # Lemos, limpamos espaços e convertemos para maiúsculas
                dados_modificados = [linha.strip().upper() for linha in arquivo if linha.strip()]

            # 5. Sobrescrita com os dados novos
            with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                for linha in dados_modificados:
                    arquivo.write(linha + "\n")
            
            print("[OK] O arquivo foi sobrescrito com letras maiúsculas.")
            print(f"Local do arquivo: {caminho_arquivo}")
        
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um problema ao acessar o arquivo: {e}")
        print("Dica: Verifique se o OneDrive não está bloqueando a pasta ou se o arquivo está aberto em outro programa.")

if __name__ == "__main__":
    main()