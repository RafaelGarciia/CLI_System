from InquirerPy 				import inquirer, get_style
from InquirerPy.base.control 	import Choice

# Tela de menu feita em inquirer.select
def menu(
		message				: str,										# Titulo do menu
		
		buttons				: list[int | str, str],						# Opções / botões do menu, exemp: [ ("MP", "Matéria prima") ]
		border				: bool				= False,				# Ativa uma borda agrupando os botões
		
		style				: dict | None		= None,					# Cores dos componentes
		
		qmark				: str 				= "#",					# Marcador de menu, caracter ou string que fica no inicio do titulo
		pointer				: str				= ">",					# Caracter indicador de seleção do menu
		
		instruction			: str 				= "",					# Curta instrução localizada logo apos o titulo do menu
		long_instruction	: str 				= "",					# Instrução longa localizada no roda-pé da janela

		key_binds			: dict | None		= None,					# Teclas de atalho desta tela
		
		mandatory			: bool 				= True,					# Ativa a obrigatoriedade desta janela, não deixando dar skip
		mandatory_message	: str 				= "Mandatory prompt"	# Frase que aparecera se tentar dar skip na janela com mandatory = True
	) -> str | int:
	
	# class.__doc__
	""" 
		menu(
			"Menu",\n
			[ (1, "Iniciar"), (2, "Config"), (0, "Sair") ],
		)
	"""
	
	# Define e constroi os botões
	_menu_choices = []
	for item in buttons:
		_menu_choices.append(Choice(item[0], item[1]))
	
	# Instancia e executa o inquirer.select
	_option = inquirer.select(
		message 			= message,
		choices 			= _menu_choices,
		keybindings			= key_binds,
		style				= get_style(style, False),
		qmark				= qmark,
		instruction			= instruction,
		long_instruction	= long_instruction,
		mandatory			= mandatory,
		mandatory_message	= mandatory_message,
		border				= border,
		pointer				= pointer
	).execute()

	# Retorna a opção escolhida
	return _option


# Tela de entrada de dados feita em inquirer.text
def entry(
		message				: str,										# Mensagem / pergunta da entrada
		
		validate			: str | None 	= None,						# Função que valida a informação que foi inserida
		invalid_message 	: str			= "Invalid Input",			# Mensagem que aparece casa a validação seja falsa
		is_password			: bool			= False,					# Ativa o modo senha, que substitui os caracteres por *
		
		style				: dict			= None,						# Cores dos componentes
		
		qmark				: str			= ">",						# Caractere ou string que aparecera antes da mensagem
		amark				: str			= "|",						# Caractere ou string que substitui o qmark apos a informação ser inserida
		
		instruction			: str			= "",						# Curta instrução localizada logo apos o titulo do meu
		long_instruction	: str			= "",						# Instrução longa localizada no roda-pé da janela

		key_binds			: dict			= None,						# Teclas de atalho desta tela
		
		mandatory			: bool			= True,						# Ativa a obrigatoriedade desta janela, não deixando dar skip
		mandatory_message	:str			= "Mandatory prompt"		# Frase que aparecera se tentar dar skip na janela com mandatory = True
	) -> str | int:

	# class.__doc__
	""" 
		entry( "Qual sua idade?" )
	"""

	# Instancia e executa o inquirer.text
	_input = inquirer.text(
		message 			= message,
		validate			= validate,
		invalid_message		= invalid_message,
		is_password			= is_password,
		style				= get_style(style, False),
		keybindings			= key_binds,
		qmark				= qmark,
		amark				= amark,
		instruction			= instruction,
		long_instruction	= long_instruction,
		mandatory			= mandatory,
		mandatory_message	= mandatory_message
	).execute()

	# Retorna a inserção dada pelo usuario
	return _input


# Tela de confirmação feira em inquirer.confirm
def confirm(
		message				: str,									# Mensagem / pergunta da confirmação

		confirm_letter		: str			="y",					# Tecla para confirmar
		reject_letter		: str			="n",					# tecla para negar

		style				: dict			= None,					# Cores dos componentes
		
		qmark				: str			= ">",					# Caractere ou string que aparecera antes da mensagem
		amark				: str			= "|",					# Caractere ou string que substitui o qmark apos a informação ser inserida

		instruction			: str			= "",					# Curta instrução localizada logo apos o titulo do meu
		long_instruction	: str			= "",					# Instrução longa localizada no roda-pé da janela

		key_binds			: dict			= None,					# Teclas de atalho desta tela

		mandatory			: bool			= True,					# Ativa a obrigatoriedade desta janela, não deixando dar skip
		mandatory_message	:str			= "Mandatory prompt"	# Frase que aparecera se tentar dar skip na janela com mandatory = True
	) -> bool:

	# Instancia e executa o inquirer.confirm
	conf = inquirer.confirm(
		message 			= message,
		confirm_letter		= confirm_letter,
		reject_letter		= reject_letter,
		style				= get_style(style, False),
		qmark				= qmark,
		amark				= amark,
		instruction			= instruction,
		long_instruction	= long_instruction,
		keybindings			= key_binds,
		mandatory			= mandatory,
		mandatory_message	= mandatory_message
	).execute()

	# Retorna a True para confirmação e False para negação
	return conf


