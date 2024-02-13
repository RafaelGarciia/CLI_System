from Librarys import Lib_Inquirer as inq
from os import system
from time import sleep


def login(users_data):
	default_style = {
			"questionmark"		: "#32cd32",	"question"			: "",
			"input"				: "#3d3dbd",	"answermark"		: "#2c9b55",
			"answered_question"	: "",			"answer"			: "#32cd32",
			"validator"			: ""
	}

	def login_valid(name_answer):
		if name_answer in users_data: return True
	
	def password_valid(password_answer):
		if password_answer == users_data[user_answer]["password"]: return True


	acess = False
	while not acess:
		system("cls")
		user_answer = inq.entry(
			message				= "Login:",
			validate			= login_valid,
			invalid_message		= "Usuario não cadastrado.",
			style				= default_style,
			qmark				= ">",
			amark				= "|",
			long_instruction	= "| C-Q : Sair |",
			key_binds			= {"interrupt": [{"key": "c-q"}]},
			mandatory			= False
		)
		password_answer = inq.entry(
			message				= "Senha:",
			validate			= password_valid,
			invalid_message		= "Senha invalida.",
			style				= default_style,
			qmark				= ">",
			amark				= "|",
			long_instruction	= "| C-B : Voltar | C-Q : Sair",
			key_binds			= {
				"interrupt": [{"key": "c-q"}],
				"skip": [{"key": "c-b"}]
			},
			mandatory			= False,
			is_password			= True
		)

		if user_answer != None and password_answer != None:
			system("cls")
			print(f"\033[32m Logado! \033[m \n Bem vindo \033[36m{user_answer.upper()}\033[m")
			sleep(2)
			return True

