from Modules import (
	module_SQL		as con_sql,
	module_Security	as security
)
from Librarys import (
	Lib_Inquirer as inq
)
from os import system, getcwd



# Mecanismos:
def fornecedor_valid(name_answer):
	""" Consulta se o fornecedor já esta cadastado """
	if name_answer in fornecedores_list:
			return False
	else: 	return True




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

# Definindo a lista para o controle de fornecedores cadastrados
fornecedores_list = {}
# Definindo a lista para o controle de mepresas cadastradas
empresas_list = {}




# System de Cadastro de Materia Prima
def System_MP():

	# Menu Principal de cadastros
	def cad_menu():

		# Menu de Cadastro de Fornecedores
		def cad_fornecedor():
			text_name 		= "Nome"
			text_empresa  	= "Empresa"
			text_nome_nota 	= "Nome na nota"
			text_remetente 	= "Remetente"
			text_motorista 	= "Motorista"
			
			# Loop do meu
			while True:
				system("cls")
				option = inq.menu(
					"Cadastro de fornecedor",
					[	("name"	, text_name 	),
	  					("emp"	, text_empresa	),
						("nom_n", text_nome_nota),
						("reme"	, text_remetente),
						("moto"	, text_motorista),
						inq.separator(			),
						(	1	, "Confirmar"	),
						(	0	, "voltar"		)
					], style = default_style
				)

				match option:
					case "name"	:			# Inserindo Nome do fornecedor
						name = inq.entry(
							"Digite o nome",
					   		validate		= fornecedor_valid,
							invalid_message	= "Fornecedor já cadastrado."
						)
						text_name = f"Nome  : {name}"
						
					case "emp":			# Inserindo a abreviação 								<-- Mudar (-Temporaria-)
						abrev = inq.entry("Digite uma abreviação")
						#text_abrev = f"Abrev.: {abrev}"
					
					case 1:					# Confirma as inserções
						system("cls")
						print (f"Name      : {name }")
						print (f"Abreviação: {abrev}")
						if inq.confirm("Confirmar as informções acima?", "s"):
							
							
							fornecedores_list.update(
								{ name: {	"name"			: name,
											"abreviação"	: abrev	} }
							)
							break
					
					case 0: break			# retorna ao Menu Principal

		def menu_empresa():


			while True:
				system('cls')
				option = inq.menu(
					"Cadastro de Empresa",
					[	("novo"	, "Nova"	),
						("list"	, "Listar"	),
	  					inq.separator(		),
						(	0	, "Voltar"	)
					], style = default_style
				)

				match option:
					case "novo":	







		# Loop Cad_fornecedor
		while True:
			system('cls')
			option = inq.menu(
				"Cadastro",
				[	("forn"	, "Fornecedor"	),
					("emp"	, "Empresa"	 	),
					inq.separator(			),
					(	0	, "Voltar"		)
				], style = default_style
			)
			match option:
				case "forn"	: cad_fornecedor()
				case "emp"	: ...
				case 0		: break

	# Loop Cad_menu
	while True:
		system("cls")
		option = inq.menu(
			"Materia Prima",
			[	("cad"	, "Cadastros"	),
				inq.separator(			),
				(	0	, "Voltar"		)
			], style = default_style
		)
		match option:
			case "cad": cad_menu()

			case 	 0: break







# Main Loop
while True:
	system('cls')		# Limpa a tela
	option = inq.menu(
		"Main Menu",
		[	(  "mp"	, "Systema de Materia prima"),
			(	0	, "Sair")
		], style = default_style
	)

	match option:
		case "mp":	sys_MP = System_MP()
		
		case	0: 	break





