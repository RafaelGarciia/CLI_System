from Librarys import Inquirer_Lib as inq
from os import system
from time import sleep


def login(users_data):
	
	default_style = inq.Style()
	default_style.questionmark = "#32cd32"
	default_style.question = ""
	default_style.input = "#3d3dbd"
	default_style.answermark = "#2c9b55"
	default_style.answered_question = ""
	default_style.answer = "#32cd32"
	default_style.validator = ""
	default_style = default_style()

	def login_valid(name_answer):
		if name_answer in users_data['content']: return True
	
	def password_valid(password_answer):
		if password_answer == users_data['content'][user_answer]["passwd"]: return True


	acess = False
	while not acess:
		system("cls")
		user_answer_entry = inq.Entry(
			message				= "Login:",
			validate			= login_valid,
			invalid_message		= "Usuario não cadastrado.",
			style				= default_style,
			question_mark		= ">",
			answer_mark			= "|",
			long_instruction	= "| C-Q : Sair |",
			mandatory			= False
		)
		user_answer_entry.keybindings = {"interrupt": [{"key": "c-q"}]}
		user_answer=  user_answer_entry()

		password_answer_entry = inq.Entry(
			message				= "Senha:",
			validate			= password_valid,
			invalid_message		= "Senha invalida.",
			style				= default_style,
			question_mark		= ">",
			answer_mark			= "|",
			long_instruction	= "| C-B : Voltar | C-Q : Sair",
			mandatory			= False,
			is_password			= True
		)
		password_answer_entry.keybindings = {
			"interrupt": [{"key": "c-q"}],
			"skip": [{"key": "c-b"}]
		}
		password_answer = password_answer_entry()

		if user_answer != None and password_answer != None:
			system("cls")
			print(f"\033[32m Logado! \033[m \n Bem vindo \033[36m{user_answer.upper()}\033[m")
			sleep(2)
			return True

