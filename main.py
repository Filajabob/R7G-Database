from student_lookup import student_lookup
from menu import menu
from edit_fields import edit_fields

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

    else:
        break