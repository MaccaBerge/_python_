import PySimpleGUI as sg

#sg.theme('SandyBeach')
width, height = 300, 200

layout = [
    [sg.Text('Autoclicker')],
    [sg.VPush()],
    [sg.Button('Start', size = (10, 2)), sg.Button('Stop', size = (10,2))],
    [sg.VPush()]
]

window = sg.Window('Autoclicker', layout, size = (width, height), no_titlebar = False, element_justification = 'center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()