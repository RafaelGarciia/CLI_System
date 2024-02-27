from Librarys import (
    Lib_SQLite3  as sql,
    Lib_Inquirer as inq
)
from os import getcwd
from functools import partial

"V ----- Database system variables ----- V"
list_supplier   :dict   = {}
"List that stores the company database"
list_company    :dict   = {}
"List that stores the company database"
list_users      :dict   = {}
"List that stores the user database"


"V ----- Database functions ----- V"

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


"V ----- Decorators for validation ----- V"

def in_database(function) -> callable:
    "Checks if the parameter is in the database"
    def valid(name_base:str, parameter:list) -> callable:
        database = {
            "User"      : list_users,
            "Company"   : list_company,
            "Supplier"  : list_supplier,
        }
        
        if parameter[0] in database[name_base]:
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


"V ----- Interact database ----- V"
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

@in_database
def dell(name_base:str, info:list):
    "Delete data from the database if it exists"
    data_base.delete(name_base, "name", info[0])
    inq.entry(
        f"{name_base} successfully deleted !",
        qmark = "@",
        style = {
            "questionmark"  : "#008000",
            "answermark"    : "#008000"
        }
    )

