from Librarys import(
	Lib_SQLite3  as sql,
	Lib_Inquirer as inq
)

# Modificando a class Data_base da Lib_SQLite3 para utilizar Inquirer


class Sql_Data_Base(sql.Data_base):
	def __init__(self, file_name: str) -> bool:
		# Classe herda a classe Data_base
		super().__init__(file_name)
		
		# Verifica de o arquivo do banco existe
		if self.exist:
			# Se existir, apenas conecta ao ele
			self.connect()
		else:
			# Senão, questiona ao usuario se deseja recriar o arquivo
			if inq.confirm(
				"Banco de dados não existente.\n  Deseja recrialo?",
				qmark = "x",
				style = {"questionmark" : "#ff0000"}
			):	
				# Cria o arquivo do banco de dados e já conecta com ele
				self.connect()
				# Cria a tabela de Usuarios para o sistema de login
				# Tabela Users: [ Nome de usuario, senha, nivel de permição de acesso ]
				self.create_table("Users", ["user_name", "password", "level"])
				# Insere um usuario root e um usuario padrão para o acesso
				self.insert("Users", ["root", "masterqi", 0])
				self.insert("Users", ["user", "1234", 3])

