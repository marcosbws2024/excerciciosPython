from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        # O método build retorna o widget principal da interface
        return Button(text='Olá, Mundo!')

# Esta parte é essencial para o Python executar o aplicativo
if __name__ == '__main__':
    ExemploApp().run()