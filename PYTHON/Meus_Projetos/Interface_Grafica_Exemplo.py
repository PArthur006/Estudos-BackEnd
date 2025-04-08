from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuário')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de login', layout)

#Leitura de dados
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuário'] == 'Pedro' and valores['senha'] == '123456':
            print('Bem vindo')
            break
