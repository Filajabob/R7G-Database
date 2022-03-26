from student_lookup import student_lookup
from menu import menu
from edit_fields import edit_fields
from list_students import list_students
from manage_json import manage_json

while True:
    menu_res = menu()
    if menu_res == "Student Lookup":
        if student_lookup() == "Menu":
            continue
        else:
            break

    elif menu_res == "Edit Fields":
        if edit_fields() == "Menu":
            continue
        else:
            break

    elif menu_res == "List Students":
        if list_students() == "Menu":
            continue
        else:
            break

    elif menu_res == "JSON":
        if manage_json() == "Menu":
            continue
        else:
            break

    else:
        break