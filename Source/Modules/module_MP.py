from Librarys import (
	Lib_Inquirer as inq,
)
from os import system
from InquirerPy.separator import Separator



class System_MP():
	def __init__(self) -> None:
		self.fornecedor = None


	def Main_menu(self, style):
		while True:
			system("cls")
			match inq.menu(
				"Materia Prima",
				[
					("cad", "Cadastros"),
					Separator(),
					(0, "Voltar")
				],
				style = style
			):
				case "cad"	: 
					
					self.cad_menu(style)
				case	0	: break

	def cad_menu(self, style):
		def cad_fornecedor():
			text_name = "Nome"
			text_abrev = "Abreviação"
			while True:
				system("cls")
				match inq.menu(
					"Cadastro de fornecedor",
					[
						("name", text_name),
						("abrev", text_abrev),
						Separator(),
						(1, "Confirmar"),
						(0, "Voltar")

					]
				):
					case "name":
						name = inq.entry('Digite o nome')
						text_name 	= f"Nome  : {name}"
					case "abrev":
						abrev = inq.entry('Digite uma abreviação')
						text_abrev 	= f"Abrev.: {abrev}"
					
					case	1:
						system("cls")
						print(f"Name      : {name }")
						print(f"Abreviação: {abrev}")
						if inq.confirm("Confirmar as informções acima?", "s"):
							self.fornecedor = {
								name: {
									"name"			: name,
									"abreviação"	: abrev
								}
							}
							input(self.fornecedor)
							break
					
					case 0: break



		while True:
			system("cls")
			match inq.menu(
				"Cadastro",
				[
					("forn", "Fornecedor"),
					("emp", "Empresa"),
					Separator(),
					(0, "Voltar")
				],
				style = style
			):
				case "forn"	: cad_fornecedor()
				case "emp"	: input("emp")
				case 	0	: break
