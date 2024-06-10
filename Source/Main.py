from Librarys  import (
    SQLite_Lib as sql,
    Inquirer_Lib as inq,
    Color_Lib   as c
)
from os         import getcwd, system
from Modules    import module_Security as sec
from time       import sleep
from random     import randint




data_base:sql.SQL_DB = None
db_file = f"{getcwd()}\\Database\\data.db"
user_loged = {'login': 'guest', 'passwd': None, 'level': 9}
time_active:bool = True
visual_mode:bool = True



def main_loop():
    initialization()
    while True:
        if visual_mode:   visual_main_loop()
        else:             command_line_main_loop()
        

# General functions
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

def time_load():
    global time_active

    if time_active:
        sleep(float(f'{randint(0, 2)}.{randint(0, 9)}'))

def exiting():
    print(f'{c.blue}> {c.red}Saindo... {c.clear}')
    time_load()
    system('cls')
    exit()

def login_system():
    global user_loged
    global data_base

    infos = sec.login(data_base.table_properties['users'])
    if infos[0]:
        user_loged = infos[1]

def set_time_active():
    global user_loged
    global time_active

    if user_loged['level'] < 2:
        time_active = not time_active
        print(f'time if {time_active}')
    else:
        print(f'Usuario não tem permissão para isso')

def set_visual_mode():
    global visual_mode
    visual_mode = not visual_mode
    system('cls')

def whoami():
    global user_loged
    global c

    print(f'{c.blue}[{c.green}{user_loged['login']}{c.blue}] {c.clear}')


# Command Line mode
def command_line_main_loop():
    command:str = get_command()

    if " " in command:
        arguments:list = command.split(' ')
        main_command = arguments.pop(0)
    else:
        main_command = command
        arguments = None
    
    del command
    match main_command:
        case 'exit'   : exiting()
        case 'login'  : login_system()
        case 'time'   : set_time_active()
        case 'reboot' : initialization()
        case 'vmode'  : set_visual_mode()
        case 'help'   : helper()

def get_command():
    whoami()
    return inq.Entry("", question_mark='>')()

def helper():
    print("#---------------------- HELP ----------------------#")
    print("v Commands v             v  Efects  v               ")
    print("    exit   - To exit the system                     ")
    print("   login   - To log in with a user                  ")
    print("    time   - To disable loading delays              ")
    print("   reboot  - To restart system and reload database  ")
    print("   vmode   - To activate Visual mode                ")
    print("                                                    ")



# Visual mode

style = inq.Style()

style = style()

def visual_main_loop():
    global style

    choices_list = []
    choices_list.append(inq.Choice('c', 'Config'))
    choices_list.append(inq.Separator())
    choices_list.append(inq.Choice( 0 , 'Exit'  ))

    system('cls')
    whoami()
    opt = inq.Select('Main menu',
        choices       = choices_list,
        style         = style,
        marker_empty  = ' ',
    )()

    match opt:
        case 'c': config_menu()
        case 0  : exiting()

def config_menu():
    while True:
        choices_list = []
        choices_list.append(inq.Choice('login', 'Log in'))

        if user_loged['level'] < 2:
            choices_list.append(inq.Choice('c_mode', 'Command line Mode'))
        
        choices_list.append(inq.Separator())
        choices_list.append(inq.Choice( 0 , 'Back'))
        
        system('cls')
        whoami()
        opt = inq.Select('Config',
            choices       = choices_list,
            style         = style,
            marker_empty  = ' ',
        )()

        match opt:
            case 'login'    : login_system()    ; break
            case 'c_mode'   : set_visual_mode() ; break
            case 0          : break



main_loop()