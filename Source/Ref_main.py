from Modules import (
	module_SQL		as m_sql,
	module_Security as security
)
from Librarys import (
	Lib_Inquirer as inq,
	Lib_SQLite3  as sql
)
from os import system, getcwd
from time import sleep



# Funções para adicionar
def add_usuario(nome, password, level):
	for item in list_usuario:
		if nome == item:
			print( "Usuario já cadastrado:	")
			print(f"Cadastrado: {item}		")
			print(f"Inserido  : {nome}		")
			return False
	
	banco_dados.insert("Usuarios", [nome, password, level])
	list_usuario.update({
		nome: {
			'password'	: password,
			'level'		: level
		}
	})
	return True

def add_empresa(nome) -> bool:
	for item in list_empresa:
		if nome == item:
			print( "Empresa já cadastrada:	")
			print(f"Cadastrada: {item}		")
			print(f"Inserida  : {nome}		")
			return False

	banco_dados.insert("Empresas", [nome])
	list_empresa.update({nome: None	})
	print("Empresa cadastrada com sucesso !")
	sleep(2)
	return True

def del_empresa(nome) -> bool:
	if banco_dados.delete("Empresas", 'nome', nome):
		list_empresa.pop(nome)
	else:
		print("erro")

def add_fornecedor(nome, nota, remetente, motorista):
	for item in list_fornecedor:
		if nome == item:
			print( "fornecedor já cadastrado:	")
			print(f"Cadastrado: {item}			")
			print(f"Inserido  : {nome}			")
			return False
	
	banco_dados.insert('Fornecedores', [nome, nota, remetente, motorista])
	list_fornecedor.update({
		nome: {
			'nota'		: nota,
			'remetente'	: remetente,
			'motorista'	: motorista,
		}
	})
	print("Fornecedor cadastrado com sucesso !")
	sleep(2)
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


# Variaveis principais do sistema
list_fornecedor	= {}	# Armazena a base de dados dos fornecedores
list_empresa	= {}	# Armazena a base de dados das empresas
list_usuario	= {}	# Armazena a base de dados dos usuarios

# Sistema que carrega o banco de dados
def load_db() -> sql.Data_base:
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
			banco_dados.create_table( "Usuarios",
				[ "user_name", "password", "level" ]
			)
			banco_dados.create_table("Empresas",
				["nome"]
			)
			banco_dados.create_table( "Fornecedores",
				["nome", "nota", "remetente", "motorista"]
			)

			# Insere dados padões do sistema
			banco_dados.insert("Usuarios", ['root', 'masterqi'	, 0])
			banco_dados.insert('Usuarios', ['user', '1234'		, 3])
		else:
			# Caso não confirme, o programa fecha.
			input("O sistema não funciona sem o banco de dados.")
			exit()

	# Retorna o objeto banco para ser utilizado nos cadastros
	return banco_dados
banco_dados		= load_db()

def atualizar_db():
	# Carrega as variaveis principais com os dados do banco de dados
	for item in banco_dados.query('Usuarios'):
		list_usuario.update({
			item[0]: {
				'password'	: item[1],
				'level'		: item[2]
			}
		})
	
	for item in banco_dados.query('Empresas'):
		list_empresa.update({item[0]: None	})
	
	for item in banco_dados.query('Fornecedores'):
		list_fornecedor.update({
			item[0]: {
				'nota'		: item[1],
				'remetente'	: item[2],
				'motorista'	: item[3],
			}
		})
atualizar_db()

def base_menu(message:str, buttons:list[str, type]) -> None:
	_choices = []
	_index = 0
	for _item in buttons:
		if   type(_item) == type(inq.separator()): _choices.append(_item)
		elif type(_item) == tuple:
			_choices.append((_index, _item[0]))
		_index += 1

	while True:
		system("cls")
		_option = inq.menu( message, _choices,
			style = {
				"questionmark"	: "#4040e3 bold",
				"question"		: "#ffffff",
				"input"			: "#000000",
				"pointer"		: "#89c6e0 bold",
			}
		)
		
		comand = buttons[_option][1]
		if comand == "break":	break
		else:	comand()
	
def menu_entry(message:str, entry_list:list, confirm_button:str = "Confirm", back_button:str = "Back"):
	_choices = []
	_exit_list = []
	_index = 0
	for _item in entry_list:
		if type(_item) == type(inq.separator()):
			_choices.append(_item)
			_exit_list.append("")
		elif type(_item) == tuple:
			_choices.append([_index, f"{_item[0]:>10}: --"])
			_exit_list.append("")
		_index += 1
	
	_choices.append(inq.separator())
	_choices.append(["ok", confirm_button])
	_choices.append(["bk", back_button])

	while True:
		system("cls")
		_option = inq.menu(message, _choices)

		if _option == "bk":	return False
		elif _option == "ok":
			return _exit_list
		else:
			entry = entry_list[_option]
			if entry[1] == None:
				insert = inq.entry(entry[0])
			else:
				insert = inq.entry(entry[0], entry[1], entry[2])

		_choices[_option][1] = f"{entry[0]:>10}: {insert}"
		_exit_list[_option] = insert

# Menus
def Main_menu():	# Menu principal
	base_menu(
		"Main Menu",
		[	("Cadastros"	, menu_cadastro			),
			inq.separator(							),
			("Sair"			, exit					),
		]
	)


def menu_cadastro():	# Menu de cadastros gerais
	base_menu(
		"Cadastros",
		[	("Empresa"		, menu_cad_empresa		),
			#("Fornecedor"	, menu_cad_fornecedor	),
			inq.separator(							),
			("Voltar"		, "break"				),

		]
	)



def menu_cad_empresa():
	base_menu(
		"Cadastros",
		[	("Nova"		, nova_empresa				),
			("Listar"	, listar_empresa			),
			("Deletar"	, deletar_empresa			),
			inq.separator(							),
			("Voltar"		, "break"				),
		]
	)

def nova_empresa():
	_returno = menu_entry(
		"Cadastro de Empresa",
		[("Nome", valid_empresa, "Empresa já cadastrada")]
	)

	if _returno != False:
		add_empresa(_returno[0])

def listar_empresa():
	for item in list_empresa:
		print(item)
	input()

def deletar_empresa():
	emp_select = ""
	
	_choices = []
	for item in list_empresa:
		_choices.append((item, ))
	base_menu("Deletar empresa", _choices)


"""
def menu_cad_fornecedor():
	while True:
		system('cls')
		option = inq.menu(
			"Cadastro de Fornecedor",
			[	(	"novo"	, "Novo"			),
				(	"list"	, "Listar"			),
				inq.separator(					),
				(	0		, "Voltar"			),
			], style = default_style
		)
		match option:
			case "novo": novo_fornecedor()
			case "list": input(list_fornecedor)				# <- Criar uma função para isso.
			case 	0  : break

def novo_fornecedor():
	text_nome = "Nome do fornecedor"
	text_nota = "Nome na nota"
	text_reme = "Remetente"
	text_moto = "Nome do motorista"
	while True:
		system('cls')
		option = inq.menu(
			"Cadastro de Fornecedor",
			[	(	"nome"	, text_nome			),
				(	"nota"	, text_nota			),
				(	"reme"	, text_reme			),
				(	"moto"	, text_moto			),
				inq.separator(					),
				(	1		, "Confirmar"		),
				(	0		, "Voltar"			),
			], style = default_style
		)
		match option:
			case "nome": 
				nome = inq.entry(
					text_nome,
					validate 		= valid_fornecedor,
					invalid_message = "Fornecedor já cadastrado."
				)
				text_nome = f"Nome     : {nome}"
			
			case "nota": 
				nota = inq.entry( text_nota )
				text_nota = f"nota     : {nota}"
			
			case "reme": 
				reme = inq.entry( text_reme )
				text_reme = f"Remetente: {reme}"
			
			case "moto": 
				moto = inq.entry( text_moto )
				text_moto = f"Motorista: {moto}"
			
			case	1 : 
				system('cls')
				print(text_nome)
				print(text_nota)
				print(text_reme)
				print(text_moto)
				if inq.confirm('Confirmar as informações acima?', "s"):
					if add_fornecedor(nome, nota, reme, moto):
						print("Fornecedor cadastrado.")
						sleep(2)
						break
					else: 
						print("Erro ao cadastrar Fornecedor.")
						sleep(2)

			case 	0 : break

"""


# Instancia a tela de login
#load_db()
#security.login(list_usuario)
Main_menu()