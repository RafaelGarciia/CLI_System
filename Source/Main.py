from Modules import (
	module_MP		as mp,
	module_SQL		as con_sql,
	module_Security	as security
)
from os import system, getcwd
from Librarys import Lib_Inquirer as inq
from InquirerPy.separator import Separator


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

fornecedores_list = {}



def fornecedor_valid(name_answer):
	if name_answer in fornecedores_list:
		return False
	else:
		return True


def System_MP():
	def cad_menu():
		def cad_fornecedor():
			text_name = "Nome"
			text_abrev = "Abreviação"
			while True:
				system("cls")
				option = inq.menu(
					"Cadastro de fornecedor",
					[	("name", text_name),
	  					("abrev", text_abrev),
						Separator(),
						(1, "Confirmar"),
						(0, "voltar")
					]
				)
				match option:
					case "name"	:
						name = inq.entry(
							"Digite o nome",
					   		validate=fornecedor_valid,
							invalid_message="Fornecedor já cadastrado."
						)
						text_name = f"Nome  : {name}"
					case "abrev":
						abrev = inq.entry("Digite uma abreviação")
						text_abrev = f"Abrev.: {abrev}"
					case 1:
						system("cls")
						print(f"Name      : {name }")
						print(f"Abreviação: {abrev}")
						if inq.confirm("Confirmar as informções acima?", "s"):
							fornecedores_list.update({
								name: {
									"name"			: name,
									"abreviação"	: abrev
								}
							})
							input(fornecedores_list)
							break


		while True:
			system('cls')
			option = inq.menu(
				"Cadastro",
				[	("forn", "Fornecedor"),
					("emp", "Empresa"),
					Separator(),
					(0, "Voltar")
				],
				style = default_style
			)
			match option:
				case "forn"	: cad_fornecedor()
				case "emp"	: ...
				case 0		: break


	while True:
		system("cls")
		option = inq.menu(
			"Materia Prima",
			[	("cad", "Cadastros"),
				Separator(),
				(0, "Voltar")
			],
			style = default_style
		)
		match option:
			case "cad": cad_menu()

			case 	 0: break







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
			sys_MP = System_MP()
		case	0: break





