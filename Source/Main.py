from Librarys import (
    Lib_SQLite3  as sql,
    Lib_Inquirer as inq
)
from os import getcwd


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


def add(table_name:str, info:list):
    """
    Infos:
        `User`    : "name", "note", "sender", "driver"  \n
        `Company` : "name"                              \n
        `Supplier`: "name", "note", "sender", "driver"  \n
        \n
        Exemple: add("Company", ["My company name"])
    """

    match table_name:
        case "User"     : _table = list_users
        case "Company"  : _table = list_company
        case "Supplier" : _table = list_supplier

    load_db()
    for _item in _table:
        if info[0] == _item:
            inq.entry(
                f"{table_name} already registered !",
                qmark = "X",
                style = {
                    "questionmark"  : "#900020",
                    "answermark"    : "#900020"
                }
            )
            return False

    valid = data_base.insert(table_name, info)
    load_db()

    if valid:
        inq.entry(
            f"{table_name} registered successfully !",
            qmark = "@",
            style = {
                "questionmark"  : "#008000",
                "answermark"    : "#008000"
            }
        )
        return True
    else:
        inq.entry(
            f"Unregistered {table_name} !",
            qmark = "X",
            style = {
                "questionmark"  : "#900020",
                "answermark"    : "#900020"
            }
        )
        return False


def dell(table_name:str, info:list):
    """
    Infos:
        `User`    : "name", "note", "sender", "driver"  \n
        `Company` : "name"                              \n
        `Supplier`: "name", "note", "sender", "driver"  \n
        \n
        Exemple: dell("Company", ["My company name"])
    """
    match table_name:
        case "User"     : _table = list_users
        case "Company"  : _table = list_company
        case "Supplier" : _table = list_supplier
    
    load_db()
    for _item in _table:
        if info[0] == _item:
            valid = data_base.delete(table_name, "name", info[0])
            load_db()

            if valid:
                inq.entry(
                    f"{table_name} successfully deleted !",
                    qmark = "@",
                    style = {
                        "questionmark"  : "#008000",
                        "answermark"    : "#008000"
                    }
                )
                return True
            else:
                inq.entry(
                    f"Unregistered {table_name} !",
                    qmark = "X",
                    style = {
                        "questionmark"  : "#900020",
                        "answermark"    : "#900020"
                    }
                )
                return False
    
    inq.entry(
        f"Unregistered {table_name} !",
        qmark = "X",
        style = {
            "questionmark"  : "#900020",
            "answermark"    : "#900020"
        }
    )
    return False


def in_database(table, info, not_in:bool):
    def valid(_function, table, info) -> callable:
        match table:
            case "User"     : _table = list_users
            case "Company"  : _table = list_company
            case "Supplier" : _table = list_supplier

        in_db = False
        for item in _table:
            if info[0] == item:
                in_db = True
                break
        
        if not_in:
            if in_db:
                return inq.entry(
                    f"{table} already registered !",
                    qmark = "X",
                    style = {
                        "questionmark"  : "#900020",
                        "answermark"    : "#900020"
                    }
                )
            else:
                return _function(_table, info)
        else:
            if in_db:
                return _function(_table, info)
            else:
                return inq.entry(
                    f"Unregistered {table} !",
                    qmark = "X",
                    style = {
                        "questionmark"  : "#900020",
                        "answermark"    : "#900020"
                    }
                )
    
    return valid


load_db()
@in_database(False)
def add_new(table, info):
    print(table)
    print(info)
    input()
    #data_base.insert(table, info)



add_new("User", ["ot"])
