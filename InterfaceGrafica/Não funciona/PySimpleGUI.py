#Não funciona, é aconselhavel usar o CustomTkinter
import PySimpleGUI as sg
import sys

# Verifica se você não nomeou o arquivo errado sem querer
if "InterfaceGrafica" in sg.__file__:
    print("ERRO CRÍTICO: Você ainda tem um arquivo chamado PySimpleGUI.py nesta pasta!")
    print("Apague o arquivo e a pasta __pycache__ antes de continuar.")
    sys.exit()

sg.theme('DarkAmber')

layout = [ 
    [sg.Text('Texto na linha 1')],
    [sg.Text('Entre com um texto:'), sg.InputText(key='-INPUT-')],
    [sg.Button('Ok'), sg.Button('Cancel')] 
]

window = sg.Window('Janela de Teste', layout)

try:
    while True:
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        
        if event == 'Ok':
            sg.popup(f"Você digitou: {values['-INPUT-']}")
finally:
    window.close()