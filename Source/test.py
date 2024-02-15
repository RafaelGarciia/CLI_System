from os import system
from Librarys import (
	Lib_Inquirer as inq,
	Lib_SQLite3  as sql
)
from InquirerPy.separator import Separator

print(type(inq.separator()))
print(type(inq.separator))
print(type(Separator))
input()



def menu_cadastro():
	input("cadastro")



def base_menu(message:str, buttons:list[str, type]) -> None:
	_choices = []
	_index = 0
	for _item in buttons:
		if   type(_item) == Separator:	_choices.append(_item)
		elif type(_item) == tuple:
			_index += 1
			_choices.append((_index, _item[0]))

	while True:
		system("cls")
		_option = inq.menu(message, _choices)
		for _item in buttons:
			
			if type(_item) != Separator:
				if _option == _item[0]:
					_item[2]()


base_menu(
		"Main Menu",
		[	(1, "Cadastros", menu_cadastro),
			inq.separator(                ),
			(2, "Teste", exit)
		]
	)


"""def cadastro():
	input("Cadastro")

def test():
	input("teste")

def menu(message, buttons):
	choices = []
	for item in buttons:
		choices.append((item[0], item[1]))
	while True:
		system("cls")
		option = inq.menu(message, choices)
		for item in buttons:
			if option == item[0]:
				item[2]()



menu("teste", [
	("cad", "Cadastros", cadastro),
	("tes", "Teste", test)
]
)
"""