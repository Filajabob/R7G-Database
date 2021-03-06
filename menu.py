import PySimpleGUI as sg

def menu():
    sg.theme("DarkAmber")

    layout = [
        [sg.Text("Welcome to the R7G Database! Please select one of the branches to go to.")],
        [sg.Button("Student Lookup"), sg.Button("Edit Fields"), sg.Button("List Students"), sg.Button("JSON"), sg.Button("Quit")]
    ]

    window = sg.Window("R7G Database - Menu", layout)
    event, values = window.read()

    if event == "Student Lookup":
        window.close()
        return "Student Lookup"
    elif event == "Edit Fields":
        window.close()
        return "Edit Fields"
    elif event == "List Students":
        window.close()
        return "List Students"
    elif event == "JSON":
        window.close()
        return "JSON"
    elif event == "Quit":
        window.close()
        return "Closed"