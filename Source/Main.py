from Librarys  import (
    SQLite_Lib as sql,
    Inquirer_Lib as inq,
    Color_Lib
)
from os        import getcwd, system
from Modules    import module_Security as sec

c = Color_Lib.Color()

data_base:sql.SQL_DB = None


def initialization():
    global data_base
    system('cls')
    data_base = sql.SQL_DB(f"{getcwd()}\\Database\\data.db")
    print(f'{c.blue}# {c.clear}Booting...')
    if data_base.table_properties == {}:
        data_base.create_table('users', ['login', 'passwd', 'level'])
        print(f'{c.blue}|\t{c.green}V {c.clear}Created user table')
        data_base.insert('users', ['master', 'root', 0])
        print(f'{c.blue}|\t{c.green}V {c.clear}Default administrative user entered')
        data_base.insert('users', ['hero', '3232', 0])

    print(c.clear)





initialization()
#input(data_base.table_properties['users'])
sec.login(data_base.table_properties['users'])
