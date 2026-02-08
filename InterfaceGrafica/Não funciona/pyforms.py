#tambem tem problemas de compatibilidade, atualmente usa customtkinter

from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms import start_app

class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples, self).__init__('Exemplo Simples')
        
        # Definição dos campos
        self._nome = ControlText('Nome', 'João')
        self._sobrenome = ControlText('Sobrenome', 'Silva')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Gerar Nome Completo')

        # Definimos a ação do botão
        self._button.value = self.__botao_pressionado

    def __botao_pressionado(self):
        # Lógica para preencher o campo nome completo
        self._nomeCompleto.value = f"{self._nome.value} {self._sobrenome.value}"

if __name__ == "__main__":
    start_app(ExemploSimples)