#não funciona a versao atual do python - A solucão é o python webview
from cefpython3 import cefpython as cef
import platform
import sys

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook 
    
    # DICA: Adicionar configurações para evitar problemas de renderização
    settings = {
        "auto_zooming": "0.0",  # Impede problemas de escala em telas 4k/Notebooks
    }
    
    cef.Initialize(settings=settings)
    
    # Criando o navegador
    cef.CreateBrowserSync(url="https://www.google.com/", 
                          window_title="Olá, mundo! CEF Python") 
    
    cef.MessageLoop() 
    cef.Shutdown()

def check_versions(): 
    ver = cef.GetVersion()
    print(f"[CEF Python] Versão: {ver['version']}")
    print(f"[Chromium] Versão: {ver['chrome_version']}")
    
    # Verifica arquitetura e versão mínima
    print(f"[Python] {platform.python_version()} {platform.architecture()[0]}")
    assert cef.__version__ >= "57.0", "CEF python v57.0+ necessário"

if __name__ == '__main__':
    main()