from Librarys import (
    Lib_SQLite3  as sql,
    Lib_Inquirer as inq
)

def aplication():
    print("Aplication")


def menu(messagem, options):
    
    buttons = []
    for item in options:
        if type(item) in (tuple, list): buttons.append(item[0])
        else:   buttons.append(item)

    while True:
        options[ inq.menu( messagem, buttons ) ]
            


menu('teste',
    [   ("Company", aplication),
        ("Supplier", aplication),
        ("separador"),
        ("back")
    ]
)

#["Company", "Supplier", "User","separator", "Back"]