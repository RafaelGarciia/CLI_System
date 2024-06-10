from Librarys  import (
    SQLite_Lib as sql,
    Inquirer_Lib as inq,
    Color_Lib   as c
)
from os         import getcwd, system
from Modules    import module_Security as sec
from time       import sleep
from random     import randint

# Root variables
data_base:sql.SQL_DB = None
db_file = f"{getcwd()}\\Database\\data.db"
user_loged = {'login': 'guest', 'passwd': None, 'level': None}
time_active = True



def main_loop():
    initialization()
    while True:
        command_str:str = get_command()

        if " " in command_str:
            command_str:list = command_str.split(' ')
            main_command = command_str.pop(0)
        else: main_command = command_str


        match main_command:
            case 'exit'   : exiting()
            case 'login'  : login_system()
            case 'time'   : set_time_active()
            case 'reboot' : initialization()


# FUNCTIONS
def login_system():
    global user_loged

    infos = sec.login(data_base.table_properties['users'])
    if infos[0]:
        user_loged = infos[1]

def time_load():
    global time_active

    if time_active:
        sleep(float(f'{randint(0, 2)}.{randint(0, 9)}'))

def set_time_active():
    global user_loged
    global time_active

    if user_loged['level'] == None:
        print(f'Usuario não logado')
    elif user_loged['level'] < 2:
        time_active = not time_active
        print(f'time if {time_active}')
    else:
        print(f'Usuario não tem permissão para isso')

def exiting():
    print(f'{c.blue}> {c.red}Saindo... {c.clear}')
    time_load()
    system('cls')
    exit()

def initialization():
    global data_base
    global db_file
    global c
    
    system('cls')
    data_base = sql.SQL_DB(db_file)
    print(f'{c.blue}# {c.clear}Booting...')
    time_load()
    if data_base.table_properties == {}:
        data_base.create_table('users', ['login', 'passwd', 'level'])
        print(f'{c.blue}|\t{c.green}V {c.clear}Created user table')
        time_load()
        data_base.insert('users', ['master', 'root', 0])
        print(f'{c.blue}|\t{c.green}V {c.clear}Default administrative user entered')
        time_load()
        data_base.insert('users', ['hero', '3232', 0])

    data_base.load_db()
    print(f'{c.blue}|\t{c.green}V {c.clear}Loaded database')
    time_load()

    print(c.clear)

def get_command():
    global c
    global user_loged

    print(f'{c.blue}[{c.green}{user_loged['login']}{c.blue}] {c.clear}')
    return inq.Entry("", question_mark='>')()
    














main_loop()