from Librarys import (
	Lib_Inquirer as inq,
	Lib_SQLite3	 as sql
)
from os import ( getcwd, system )
from os.path import isfile




class System_MP():
	def __init__(self) -> None:
		self.fornecedor = None


	def Main_menu(self, style):
		def cad_menu():
			while True:
				system("cls")
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
					

		while True:
			system("cls")
			match inq.menu(
				"Materia Prima",
				[
					("cad", "Cadastros"),
					(0, "Voltar")
				],
				style = style
			):
				case "cad"	: cad_menu()
				case	0	: break

	

			
		
	def load_db():
		database_path = f"{getcwd()}\\data.db"
		
		if isfile(database_path):
			base = sql.Data_base(database_path)
		else:
			if inq.confirm(
				"Banco de dados não existente.\n  Deseja recrialo?",
				qmark="x",
				style={"questionmark" : "#ff0000"}
			):
				#base = sql.Data_base(database_path)
				#base.create_table("", "user_name, password, level")
				#base.insert("Users", ["root", "masterqi", 0])
				...
			else:
				pass


System_MP()