import PySimpleGUI as sg
import json

def edit_fields():
    layout = [
        [sg.Text("Welcome to the R7G Database Edit Fields Tool!")],
        [sg.Text("Input student's first name:"), sg.InputText(key="query"), sg.Button("Search")],
        [sg.Text("OR add a new field:"), sg.Button("Add New Fields")]
    ]

    window = sg.Window("R7G Database - Edit Fields - Menu", layout)
    event, values = window.read()

    if event == "Search":
        with open("stats/students.json", 'r') as f:
            data = json.load(f)["students"]

        query = values["query"]

        if not values["query"] in data:
            resp = [
                [sg.Text("That student was not found in the database.")],
                [sg.Button("OK"), sg.Button("Menu")]
            ]
        else:
            resp = []

            for key, value in data[values["query"].capitalize()].items():
                resp.append(
                    [sg.Text(key.replace('-', ' ').title() + ':'), sg.InputText(value, key=key)]
                )

            resp.append(
                [sg.Submit(), sg.Cancel()]
            )

        window.close()
        resp_window = sg.Window("R7G Database - Edit Fields", resp)
        event, values = resp_window.read()

        if event in ("OK", "Cancel", sg.WIN_CLOSED):
            return "Closed"
        else:
            with open("stats/students.json", 'r+') as f:
                data = json.load(f)

                for key, value in values.items():
                    data["students"][query][key] = value

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

            confirmation = [
                [sg.Text("Your changes have been saved.")],
                [sg.Button("OK"), sg.Button("Menu")]
            ]

            resp_window.close()
            con_window = sg.Window("R7G Database - Edit Fields - Confirmation", confirmation)
            event, values = con_window.read()

            if event == "Menu":
                con_window.close()
                return "Menu"
            else:
                con_window.close()
                return "Closed"

    elif event == "Add New Fields":
        layout = [
            [sg.Text("Add new field:"), sg.InputText(key="field")],
            [sg.Submit(), sg.Cancel()]
        ]

        window.close()
        window = sg.Window("R7G Database - Add New Field", layout)
        event, values = window.read()

        if event == "Submit":
            with open("stats/students.json", 'r+') as f:
                data = json.load(f)

                for student, fields in data["students"].items():
                    data["students"][student][values["field"].lower().replace(' ', '-')] = None

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

            resp_layout = [
                [sg.Text("Your changes have been saved.")],
                [sg.Button("OK"), sg.Button("Menu")]
            ]

            window.close()
            resp_window = sg.Window("R7G Database - Add New Field - Results", resp_layout)
            event, values = resp_window.read()

            if event == "Menu":
                resp_window.close()
                return "Menu"
            else:
                resp_window.close()
                return "Closed"
                    
        else:
            return "Closed"