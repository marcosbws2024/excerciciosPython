from PIL import Image
import numpy as np
import os

def main():
    try:
        # Pega o caminho absoluto da pasta onde este script está salvo
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        
        # Constrói o caminho completo para a imagem (ex: .../imagem/pngwing.png)
        caminho_imagem = os.path.join(diretorio_atual, "pngwing.png")
        
        print(f"Buscando imagem em: {caminho_imagem}")

        # 1. Carregar a imagem original
        img = Image.open(caminho_imagem)
        img.show()

        # 2. Converter a imagem em dados binários (numpy array)
        img_data = np.array(img)
        shape_original = img_data.shape
        binary_data = img_data.tobytes()

        # 3. Salvar os dados binários (usando caminhos relativos para os arquivos .bin também)
        caminho_bin_orig = os.path.join(diretorio_atual, "original_img.bin")
        with open(caminho_bin_orig, "wb") as file:
            file.write(binary_data)

        # 4. Criar a cópia manipulada (Invertendo os bytes)
        data_invertida = bytearray(binary_data)[::-1]
        
        caminho_bin_copy = os.path.join(diretorio_atual, "copy_img.bin")
        with open(caminho_bin_copy, "wb") as file:
            file.write(data_invertida)

        # 5. Reconstruir a imagem a partir dos bytes invertidos
        # O reshape usa o shape_original para garantir que as dimensões batam
        modified_data = np.frombuffer(data_invertida, dtype=np.uint8).reshape(shape_original)
        modified_img = Image.fromarray(modified_data)
        
        modified_img.show()
        print("Processo finalizado com sucesso!")

    except FileNotFoundError:
        print(f"ERRO: O arquivo 'pngwing.png' não foi encontrado na pasta: {diretorio_atual}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()