import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import PySimpleGUI as sg

TOGGLE_KEY = KeyCode(char='q')

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.0001)


def toggle_event(key):
    if key == TOGGLE_KEY or key == 'Start' or key == 'Stop':
        global clicking
        clicking = not clicking 

# GUI
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

    if event == 'Start':
        clicker()
    
    if event == 'Stop':
        toggle_event('Stop')

    if event == sg.WIN_CLOSED:
        break


window.close()


