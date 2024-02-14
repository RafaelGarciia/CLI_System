from InquirerPy 				import inquirer, get_style
from InquirerPy.base.control 	import Choice
from InquirerPy.separator 		import Separator

def separator():
	return Separator()

def menu(
		message				: str,
		
		buttons				: list[int | str, str],
		border				: bool				= False,
		
		style				: dict | None		= None,
		
		qmark				: str 				= "#",
		pointer				: str				= ">",
		
		instruction			: str 				= "",
		long_instruction	: str 				= "",

		key_binds			: dict | None		= None,
		
		mandatory			: bool 				= True,
		mandatory_message	: str 				= "Mandatory prompt"
	) -> str | int:
	
	# class.__doc__
	""" 
		menu(
			"Menu",\n
			[ (1, "Iniciar"), (2, "Config"), (0, "Sair") ],
		)
	"""
	
	# Defines choices
	_menu_choices = []
	for item in buttons:
		if type(item) not in (tuple, list):
			_menu_choices.append(item)
		else:
			_menu_choices.append(Choice(item[0], item[1]))
	
	# The Menu in inquirer.select
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

	return _option

def entry(
		message				: str,
		
		validate			: str | None 	= None,
		invalid_message 	: str			= "Invalid Input",
		is_password			: bool			= False,
		
		style				: dict			= None,
		
		qmark				: str			= ">",
		amark				: str			= "|",
		
		instruction			: str			= "",
		long_instruction	: str			= "",

		key_binds			: dict			= None,
		
		mandatory			: bool			= True,
		mandatory_message	:str			= "Mandatory prompt"
	) -> str | int:

	# class.__doc__
	""" 
		entry( "Qual sua idade?" )
	"""

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

	return _input

def confirm(
		message				: str,

		confirm_letter		: str			="y",
		reject_letter		: str			="n",

		style				: dict			= None,
		
		qmark				: str			= ">",
		amark				: str			= "|",

		instruction			: str			= "",
		long_instruction	: str			= "",

		key_binds			: dict			= None,

		mandatory			: bool			= True,
		mandatory_message	:str			= "Mandatory prompt"
	) -> bool:

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

	return conf




