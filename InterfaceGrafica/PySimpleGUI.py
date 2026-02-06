import PySimpleGUI as sg

sg.theme('DarkAmber')

# O layout é uma lista de listas
layout = [ 
    [sg.Text('Texto na linha 1')],
    [sg.Text('Entre com um texto na linha 2'), sg.InputText(key='-INPUT-')], # Adicionei uma key
    [sg.Button('Ok'), sg.Button('Cancel')] 
]

# A linha abaixo deve estar alinhada corretamente à esquerda
window = sg.Window('Bem-Vindo ao PySimpleGUI', layout)

while True:
    event, values = window.read()
    
    # Se o usuário fechar a janela ou clicar em Cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    # Usando a key '-INPUT-' em vez do índice 0
    print('Você entrou com: ', values['-INPUT-'])

window.close()