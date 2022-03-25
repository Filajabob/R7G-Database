import json
import PySimpleGUI as sg

def list_students():
    with open("stats/students.json", 'r') as f:
        data = json.load(f)

    fields = list(data["students"][next(iter(data["students"]))].keys())

    layout = [
        [sg.Text("Choose field to list.")]
    ]

    for field in fields:
        layout.append([sg.Radio(field.replace('-', ' ').title(), "field-select", default=False, key=field)])

    layout.append([sg.Submit(), sg.Cancel()])

    window = sg.Window("R7G Database - List Students - Select Field", layout)
    event, values = window.read()

    if event == "Submit":
        resp_layout = []

        for key, value in values.items():
            if value:
                field = key

        for key, value in data["students"].items():
            resp_layout.append(
                [sg.Text(key + "\t" + str(data["students"][key][field]))]
            )

        resp_layout.append(
            [sg.Button("OK"), sg.Button("Menu")]
        )

        window.close()
        resp_window = sg.Window("R7G Database - List Students - Results", resp_layout)
        event, values = resp_window.read()

        if event == "Menu":
            resp_window.close()
            return "Menu"
        else:
            resp_window.close()
            return "Closed"


    else:
        window.close()
        return "Closed"