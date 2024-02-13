from Modules import (
	module_MP		as mp,
	module_SQL		as con_sql,
	module_Security	as security
)
from os import system, getcwd
from Librarys import Lib_Inquirer as inq


# Iniciando o banco de dados
data_base = con_sql.Sql_Data_Base(f"{getcwd()}\\data.db")
if not data_base.exist:
	# Caso não exista, o programa se fecha.
	input("O sistema não funciona sem o banco de dados")
	exit()

# Carregando os Usuarios do banco de dados
users_db = {}
for item in data_base.query("Users"):
	users_db.update({
		item[0]: {
			"name"		: item[0],
			"password"	: item[1],
			"level"		: item[2]
		}
	})
# Iniciando a tela de login
security.login(users_db)

# Setando o style padão das telas
default_style = {
	"questionmark"	: "#4040e3 bold",
	"question"		: "#ffffff",
	"input"			: "#000000",

	"pointer"		: "#89c6e0 bold",
}

# Main Loop
while True:
	system('cls')	# Limpa a tela
	option = inq.menu(
		"Main Menu",
		[
			("mp"	, "Systema de Materia prima"),
			(0		, "Sair")
		],
		style = default_style
	)

	match option:
		case "mp":
			sys_MP = mp.System_MP()			# Instancia o modulo
			sys_MP.Main_menu(default_style)	# Passando para o menu do modulo
		case	0: break



