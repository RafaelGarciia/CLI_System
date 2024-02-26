from Librarys import (
    Lib_SQLite3  as sql,
    Lib_Inquirer as inq
)
from os import system, getcwd



# Main system variables
list_supplier   = {}    # Supplier database
list_company    = {}    # Company database
list_users      = {}    # Users database

data_base = sql.Data_base(f"{getcwd()}\\data.db")
if not data_base.exist:
    if inq.confirm(
        "Data base does't exist. \nDo you want to recreate the DataBase?",
        qmark = "X",
        style = {"questionmark" : "#ff0000"}
    ):
        data_base.connect()
        data_base.create_table(
            "Users",
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

        data_base.insert("Users", ['root', 'masterqi'   , 0])
        data_base.insert("Users", ['user', '1234'       , 3])
    else:
        inq.entry(
            "The system does't work without the Database. \nthe system will be closed",
            qmark = "X",
            style = {"questionmark" : "#ff0000"},   
        )
        exit()



def load_db():
    print("load")
    for table in data_base.tables:
        input(table)

load_db()