import PySimpleGUI as sg
import json

sg.theme("DarkAmber")

layout = [
    [sg.Text("Welcome to the R7G Database!")],
    [sg.Text("Start by looking up a student (first name):"), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window("R7G DATABASE", layout)

while True:
    event, values = window.read()

    if event == "Submit":
        window.close()
        student = values[0]

        with open("stats/students.json", 'r') as f:
            data = json.load(f)["students"]

        if not student.capitalize() in data:
            layout = [
                [sg.Text("Uh oh!")],
                [sg.Text("The student you searched was not found.")],
                [sg.Button("OK")]
            ]
        else:
            birthday = data[student]["birthday"]

            if birthday == None:
                birthday = "Unknown"

            layout = [
                [sg.Text("Birthday:"), sg.Text(birthday)],
                [sg.Button("OK")]
            ]

        res_window = sg.Window("R7G Database - Results", layout)
        res_event, res_values = res_window.read()

        if res_event == "OK":
            break

    elif event == sg.WIN_CLOSED or event == "Cancel":
        break