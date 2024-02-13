from Librarys import (
	Lib_Inquirer as inq,
	Lib_SQLite3	 as sql
)
from os import ( getcwd, system )
from os.path import isfile



# Class padrão do modulo
class System_MP():
	def __init__(self) -> None:
		# Definindo as variavels principais
		self.fornecedor = None

	# Menu principal do modulo MP
	def Main_menu(self, style):
		def cad_menu():
			while True:
				system("cls")	# Limpa a tela
				match inq.menu(
					"Cadastro",
					[
						("forn", "Fornecedor"),
						("emp", "Empresa"),
						(0, "Voltar")
					],
					style = style
				):
					case "forn"	: input("forn")
					case "emp"	: input("emp")
					case 	0	: break
					
		# Menu
		while True:
			system("cls")	# Limpa a tela
			
			option = inq.menu(
				"Materia Prima",
				[
					("cad", "Cadastros"),
					(0, "Voltar")
				],
				style = style
			)

			match option:
				case "cad"	: cad_menu()
				case	0	: break

