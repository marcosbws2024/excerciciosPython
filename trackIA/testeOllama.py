import ollama

try:
    # Testa uma comunicação simples
    res = ollama.list()
    print("Modelos encontrados:", [m['name'] for m in res['models']])
except Exception as e:
    print(f"Erro ao conectar com o servidor Ollama: {e}")