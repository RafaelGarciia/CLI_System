from Librarys import(
	Lib_SQLite3  as sql,
	Lib_Inquirer as inq
)



class Sql_Data_Base(sql.Data_base):
	def __init__(self, file_name: str) -> bool:
		super().__init__(file_name)
		if self.exist:
			self.connect()
		else:
			if inq.confirm(
				"Banco de dados não existente.\n  Deseja recrialo?",
				qmark = "x",
				style = {"questionmark" : "#ff0000"}
			):	
				# Create the data base
				self.connect()
				# Create the tables
				self.create_table("Users", ["user_name", "password", "level"])
				# Insert the default data
				self.insert("Users", ["root", "masterqi", 0])
				self.insert("Users", ["hero", "3232", 1])

	def load(self):
		self.query()
