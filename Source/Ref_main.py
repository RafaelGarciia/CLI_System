from Modules import (
	module_SQL		as m_sql,
	module_Security as security
)
from Librarys import (
	Lib_Inquirer as inq,
	Lib_SQLite3  as sql
)
from os import system, getcwd

# Variaveis principais do sistema
list_fornecedor	= {}	# Armazena a base de dados dos fornecedores
list_empresa	= {}	# Armazena a base de dados das empresas
list_users		= {}	# Armazena a base de dados dos usuarios


def load_db():
	# Iniciadno o banco de dados
	banco_dados = sql.Data_base(f"{getcwd()}\\data.db")
	# Caso o arquivo não exista
	if not banco_dados.exist:
		# Questiona que deve recriar a base de dados
		confirm = inq.confirm(
			"Banco de dados não existente.\n  Deseja recrialo?",
			qmark = "X",
			style = {"questionmark" : "#ff0000"}
		)
		if confirm:
			# Cria o arquivo
			banco_dados.connect()
			
			# Cria as tabelas
			banco_dados.create_table( "Users",
				[ "user_name", "password", "level" ]
			)
			banco_dados.create_table( "Empresas",
				["nome"]
			)
			banco_dados.create_table( "Fornecedores",
				["nome", "nota", "remetente", "motorista"]
			)

			# Insere dados padões do sistema
			banco_dados.insert("Users", ['root', 'masterqi'	, 0])
			banco_dados.insert('Users', ['user', '1234'		, 3])
		else:
			# Caso não confirme, o programa fecha.
			input("O sistema não funciona sem o banco de dados.")
			exit()

	for item in banco_dados.query('Users'):
		list_users.update({
			item[0]: {
				'password'	: item[1],
				'level'		: item[2]
			}
		})
	
	for item in banco_dados.query('Empresas'):
		add_empresa(item[0])
	
	for item in banco_dados.query('Fornecedores'):
		add_fornecedor(item[0], item[1], item[2], item[3])

load_db()

# Instancia a tela de login
security.login(list_users)



# Dicionario para o estilo do sistema
default_style = {
	"questionmark"	: "#4040e3 bold",
	"question"		: "#ffffff",
	"input"			: "#000000",

	"pointer"		: "#89c6e0 bold",
}


def add_empresa(nome) -> bool:
	for item in list_empresa:
		if nome == item:
			print( "Empresa já cadastrada:	")
			print(f"Cadastrada: {item}		")
			print(f"Inserida  : {nome}		")
			return False

	list_empresa.update({nome: None	})
	return True

def add_fornecedor(nome, nota, remetente, motorista):
	for item in list_fornecedor:
		if nome == item:
			print( "fornecedor já cadastrado:	")
			print(f"Cadastrado: {item}			")
			print(f"Inserido  : {nome}			")
			return False
	
	list_fornecedor.update({
		nome: {
			'nota'		: nota,
			'remetente'	: remetente,
			'motorista'	: motorista,
		}
	})
	return True



# Validações:
def valid_fornecedor(name_answer):
	""" Consulta se o fornecedor já esta cadastrado\n
		Caso já esteja, retorna: False\n
		Caso não esteja, ele retorna: True """
	if name_answer in list_fornecedor: return False
	else: return True

def valid_empresa(name_answer):
	""" Consulta se a empresa já esta cadastrada\n
		Caso já esteja, retorna: False\n
		Caso não esteja, ele retorna: True """
	if name_answer in list_empresa: return False
	else: return True

	

# Menus
def Main_menu():
	while True:
		system('cls')
		option = inq.menu(
			"Main Menu",
			[	(	"cad"	, "Cadastros"		),
				inq.separator(					),
				(	0		, "Sair"			),
			], style = default_style
		)

		match option:
			case "cad":	menu_cadastro()

# Menu de cadastros gerais
def menu_cadastro():
	while True:
		system('cls')
		option = inq.menu(
			"Cadastros",
			[	(	"emp"	, "Empresa"			),
				inq.separator(					),
				(	0		, "Voltar"			),
			], style = default_style
		)
		match option:
			case "emp":	menu_cad_empresa()
			case 	0 : break


def menu_cad_empresa():
	while True:
		system('cls')
		option = inq.menu(
			"Cadastro de Empresa",
			[	(	"nova"	, "Nova"			),
				(	"List"	, "Listar"			),
				inq.separator(					),
				(	0		, "Voltar"			),
			], style = default_style
		)
		match option:
			case "emp":	
			case 	0 : break

def nova_empresa():
	text_nome = "Nome da empresa"
	while True:
		system('cls')
		option = inq.menu(
			"Cadastro de Empresa",
			[	(	"nome"	, text_nome			),
				inq.separator(					),
				(	1		, "Confirmar"		),
				(	0		, "Voltar"			),
			], style = default_style
		)
		match option:
			case "nome": 
				nome = inq.entry(
					text_nome,
					validate 		= valid_empresa,
					invalid_message = "Empresa já cadastrada."
				)
				text_nome = f"Nome: {nome}"
			
			case	1 : 
				system('cls')
				print(text_nome)
				if inq.confirm('Confirmar as informações acima?', "s"):
					list_empresa.update({})
			case 	0 : break


