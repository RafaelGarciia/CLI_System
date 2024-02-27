from Librarys import (
    Lib_SQLite3  as sql,
    Lib_Inquirer as inq
)
from os import getcwd
from functools import partial

"# ----- Database system variables ----- #"
list_supplier   :dict   = {}    # Supplier database

list_company    :dict   = {}    # Company database

list_users      :dict   = {}
"Lista que armazena o banco de dados de usuarios"


"# ----- Database functions ----- #"
# Instantiating the database
data_base = sql.Data_base(f"{getcwd()}\\data.db")
if not data_base.exist:
    if inq.confirm(
        "Data base does't exist. \nDo you want to recreate the DataBase?",
        qmark = "X",
        style = {"questionmark" : "#ff0000"}
    ):
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
        inq.entry(
            "The system does't work without the Database. \nthe system will be closed",
            qmark = "X",
            style = {"questionmark" : "#ff0000"},   
        )
        exit()
else:
    data_base.connect()


def load_db():
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



def in_database(function):
    def valid(name_base:str, parameter:list):
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


@not_in_database
def add(name_base:str, info:list):
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
    data_base.delete(name_base, "name", info[0])
    inq.entry(
        f"{name_base} successfully deleted !",
        qmark = "@",
        style = {
            "questionmark"  : "#008000",
            "answermark"    : "#008000"
        }
    )

