from Librarys  import (
    Lib_SQLite3  as sql,
    Lib_Inquirer as inq
)
from os        import getcwd, system
from functools import partial


"V --------------- Database system variables --------------- V"

list_supplier   :dict   = {}
"List that stores the company database"

list_company    :dict   = {}
"List that stores the company database"

list_users      :dict   = {}
"List that stores the user database"


"V ------------------ Database functions ------------------- V"

# Instantiating the database
data_base = sql.Data_base(f"{getcwd()}\\data.db")
"Variable that stores the database instance"

# In case it doesn't exist
if not data_base.exist:
    # Asks whether to recreate the database
    if inq.confirm(
        "Data base does't exist. \nDo you want to recreate the DataBase?",
        qmark = "X",
        style = {"questionmark" : "#ff0000"}
    ):
        # If yes, recreate the database
        data_base.connect()
        data_base.create_table(
            "User",
            [ "name", "password", "level" ]
        )
        data_base.create_table(
            "Company",
            [ "name" ]
        )
        data_base.create_table(
            "Supplier",
            [ "name", "note", "sender", "driver" ]
        )

        data_base.insert("User", ['root', 'masterqi'   , 0])
        data_base.insert("User", ['user', '1234'       , 3])
    else:
        # Else, informs that the system will be closed and exit
        inq.entry(
            "The system does't work without the Database. \nthe system will be closed",
            qmark = "X",
            style = {"questionmark" : "#ff0000"},   
        )
        exit()
else:
    # If it exists, it just instantiates the database
    data_base.connect()

def load_db():
    "Loads the database into memory"

    list_users.clear()
    list_company.clear()
    list_supplier.clear()

    for _item in data_base.query("User"):
        list_users.update({
            _item[0]:{
                'password'  : _item[1],
                'level'     : _item[2]
            }
        })
    
    for _item in data_base.query("Company"):
        list_company.update({
            _item[0]: None
        })
    
    for _item in data_base.query("Supplier"):
        list_supplier.update({
            _item[0]:{
                'note'      : _item[1],
                'sender'    : _item[2],
                'driver'    : _item[3]
            }
        })
load_db()


"V --------------- Decorators for validation --------------- V"

def in_database(function) -> callable:
    "Checks if the parameter is in the database"
    def valid(name_base:str, parameter:list) -> callable:
        database = {
            "User"      : list_users,
            "Company"   : list_company,
            "Supplier"  : list_supplier,
        }

        if parameter in database[name_base]:
            return function(name_base, parameter)
        
        else:
            return inq.entry(
                f"Unregistered {name_base} !",
                qmark = "X",
                style = {
                    "questionmark"  : "#900020",
                    "answermark"    : "#900020"
                }
            )
    
    return valid

def not_in_database(function):
    "Checks if the parameter is not in database"
    def valid(name_base:dict, parameter):
        database = {
            "User"      : list_users,
            "Company"   : list_company,
            "Supplier"  : list_supplier,
        }

        if parameter[0] not in database[name_base]:
            return function(name_base, parameter)
        
        else:
            return inq.entry(
                f"{name_base} already registered !",
                qmark = "X",
                style = {
                    "questionmark"  : "#900020",
                    "answermark"    : "#900020"
                }
            )

    return valid


"V ------------------- Interact database ------------------- V"
# funcions that interact with the database

@not_in_database
def add(name_base:str, info:list):
    "Adds data to the database if it doesn t exist"
    data_base.insert(name_base, info)
    inq.entry(
        f"{name_base} registered successfully !",
        qmark = "@",
        style = {
            "questionmark"  : "#008000",
            "answermark"    : "#008000"
        }
    )
    load_db()

@in_database
def dell(name_base:str, name:str):
    "Delete data from the database if it exists"
    data_base.delete(name_base, "name", name)
    inq.entry(
        f"{name_base} successfully deleted !",
        qmark = "@",
        style = {
            "questionmark"  : "#008000",
            "answermark"    : "#008000"
        }
    )
    load_db()


"V ------------------- Interface database ------------------ V"

add_company   = partial(add  , "Company" )
""" Partial to add a Company to the database.\n
    add_company( list["Company name"] )                     """

add_user      = partial(add  , "User"    )
""" Partial to add a User to the database.\n
    add_user( list["User_name", "password", "level"] )      """

add_supplier  = partial(add  , "Supplier")
""" Partial to add a Supplier to the database.\n
    add_supplier( list["Name", "Note", "Sender", "Driver"] )"""

dell_company  = partial(dell , "Company" )
""" Partial to delete a Company to the database.\n
    dell_company( list["Company name"] )                    """

dell_user     = partial(dell , "User"    )
""" Partial to delete a User to the database.\n
    dell_user( list["User name"] )                          """

dell_supplier = partial(dell , "Supplier")
""" Partial to delete a Supplier to the database.\n
    dell_user( list["Supplier name"] )                      """

"^ --------------------------------------------------------- ^"



def main_menu():

    while True:
        system("cls")
        _opt = inq.menu(
            "Main menu",
            ["Register", "separator","Exit"]
        )

        match _opt:
            case 0: # Register
                registration_menu()
            
            case 2: # Exit
                exit()



"V ------------------- Registration Menu ------------------- V"
def registration_menu():
    while True:
        system("cls")
        match inq.menu(
            "Registration",
            ["Company", "Supplier", "separator", "Back"]
        ):
            case 0: menu_company_reg()
            case 1: ...
            case 3: break


"V --------------------- Company Menu ---------------------- V"
def menu_company_reg():
    while True:
        system("cls")
        match inq.menu(
            "Company registration",
            ["New", "Remove", "List", "separator", "Back"]
        ):
            case 0: new_company()
            case 1: remove_company()
            case 2: ls_company()
            case 4: break

def new_company():
    load_db()
    def entry_name():
        return inq.entry("",
            lambda x: False if x in list_company else True,
            "Company is are register",
            key_binds = {"skip": [{"key": "alt-q"}]},
            mandatory = False,
            long_instruction = "Ctr-Q - back"
        )

    entry_list = []
    infos = inq.input_menu("New Company", [("name", entry_name)])
    if infos == False:
        return
    
    for colum in infos:
        entry_list.append(infos[colum])

    add_company(entry_list)

def remove_company():
    load_db()
    entry = inq.entry(
        "",
        lambda x: True if x in list_company else False,
        "Company not found",
        key_binds = {"skip": [{"key": "alt-q"}]},
        mandatory = False,
        long_instruction = "Ctr-Q - back",
        auto_complet = list_company
    )

    if entry == None or not inq.confirm(f"Do you want to delete the {entry} company?", "s", "n"):
        return

    dell_company(entry)

def ls_company():
    load_db()
    for item in list_company:
        print(item)
    input()



"^ --------------------------------------------------------- ^"