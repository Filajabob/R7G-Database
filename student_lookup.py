import PySimpleGUI as sg
import json

def student_lookup():
    sg.theme("DarkAmber")

    layout = [    
        [sg.Text("Welcome to the R7G Database!")],
        [sg.Text("Start by looking up a student (first name):"), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window("R7G Database - Student Lookup", layout)

    event, values = window.read()

    if event == "Submit":    
        student = values[0]

        with open("stats/students.json", 'r') as f:
            data = json.load(f)["students"]

        if not student.capitalize() in data:
            layout = [
                [sg.Text("Uh oh!")],
                [sg.Text("The student you searched was not found.")],
                [sg.Text(f"Query: {student.capitalize()}")],
                [sg.Button("OK"), sg.Button("Menu")]
            ]
        else:
            layout = []

            for key, value in data[student].items():
                layout.append([sg.Text(key.replace("-", " ").title() + ':'), sg.Text(value)])

            layout.append(
                [sg.Button("OK"), sg.Button("Menu")]
            )

        window.close()
        res_window = sg.Window(f"R7G Database - Query Results for '{student}'", layout)
        res_event, res_values = res_window.read()

        if res_event == "Menu":
            res_window.close()
            return "Menu"

        elif res_event in (sg.WIN_CLOSED, "OK"):
            res_window.close()
            return "Closed"
