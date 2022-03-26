import PySimpleGUI as sg
import os

def manage_json():
    layout = [
        [sg.Text(os.path.abspath("stats/students.json"))],
        [sg.Button("OK"), sg.Button("Menu")]
    ]

    window = sg.Window("R7G Database - JSON", layout)
    event, values = window.read()

    if event == "Menu":
        window.close()
        return "Menu"
    else:
        window.close()
        return "Closed"