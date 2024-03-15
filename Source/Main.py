from Librarys  import (
    Lib_SQLite3  as sql,
    Lib_Inquirer as inq
)
from os        import getcwd, system
from functools import partial


"V ---------------- Database system variables ---------------- V"

list_supplier   :dict   = {}
"List that stores the company database"

list_company    :dict   = {}
"List that stores the company database"

list_users      :dict   = {}
"List that stores the user database"

"V ------------------- Database functions -------------------- V"

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

def load_db() -> None:
    "Loads or reloads the database into memory"

    # Clears dictionaries from memory to be loaded again
    list_users.clear()
    list_company.clear()
    list_supplier.clear()

    # Loads Users dictionary
    for _item in data_base.query("User"):
        list_users.update({
            _item[0]:{
                'password'  : _item[1],
                'level'     : _item[2]
            }
        })
    
    # Loads Companys dictionary
    for _item in data_base.query("Company"):
        list_company.update({
            _item[0]: None
        })
    
    # Loads Suppliers dictionary
    for _item in data_base.query("Supplier"):
        list_supplier.update({
            _item[0]:{
                'note'      : _item[1],
                'sender'    : _item[2],
                'driver'    : _item[3]
            }
        })
load_db()

"V ---------------- Decorators for validation ---------------- V"
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

def not_in_database(function) -> callable:
    "Checks if the parameter is not in database"
    def valid(name_base:dict, parameter) -> callable:
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

"V -------------------- Interact database -------------------- V"
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


#"""                        INTERFACES                        """
#"V ---------------------------------------------------------- V"

default_key_binds = {"skip": [{"key": "alt-q"}]}
default_instruction = "Alt-Q - back"

"V ------------------------ Main Menu ------------------------ V"
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

"V -------------------- Registration Menu -------------------- V"
def registration_menu() -> None:
    while True:
        system("cls")
        match inq.menu(
            "Registration",
            ["Company", "Supplier", "User","separator", "Back"]
        ):
            case 0: menu_registration( "Company" )
            case 1: menu_registration("Supplier" )
            case 2: menu_registration(  "User"   )
            case 4: break

def menu_registration(_type) -> None:

    def entry_name() -> str:
        return inq.entry("",
            lambda x: False if x in base[_type] else True,
            invalid_message  = f"{_type} is are register",
            key_binds        = default_key_binds,
            mandatory        = False,
            long_instruction = default_instruction
        )
    
    def entry_generic() -> str:
        return inq.entry("",
            key_binds        = default_key_binds,
            mandatory        = False,
            long_instruction = default_instruction
        )

    _entrys = {
        "User"      : [ ("Name"     , entry_name   ),
                        ("Password" , entry_generic),
                        ("Level"    , entry_generic) ],
        
        "Company"   : [ ("Name"     , entry_name   ) ],
        
        "Supplier"  : [ ("Name"     , entry_name   ),
                        ("Note"     , entry_generic),
                        ("Sender"   , entry_generic),
                        ("Driver"   , entry_generic) ],
    }

    while True:
        system("cls")
        load_db()
        base = {
            "User"      : list_users,
            "Company"   : list_company,
            "Supplier"  : list_supplier
        }
        
        match inq.menu(
            f"{_type} Registration",
            ["New", "Remove", "List", "separator", "Back"]
        ):
            case 0:
                infos = inq.input_menu(f"New {_type}",
                    _entrys[_type]
                )
                
                if infos == False:
                    return
                
                _entry_list = []
                for colum in infos:
                    _entry_list.append(infos[colum])

                add(_type, _entry_list)
            
            case 1:
                _remove_entry = inq.entry("",
                    lambda x: True if x in base[_type] else False,
                    f"{_type} not found",
                    key_binds = default_key_binds,
                    mandatory = False,
                    long_instruction = default_instruction,
                    auto_complet = {item: None for item in base[_type]}
                )

                if _remove_entry == None or not inq.confirm(
                    f"Do you want to delete the {_remove_entry} {_type}?", 
                    confirm_letter  = "s",
                    reject_letter   = "n"
                ): return
                else:
                    dell(_type, _remove_entry)


            case 2:
                print()
                index = 0
                for item in base[_type]:
                    index += 1
                    print(f"| {index:>2} - {item}")
                input("\nEnter to continue")
            
            case 4: break







"^ ----------------------------------------------------------- ^"

main_menu()
