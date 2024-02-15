import sqlite3 as sql
from os.path import isfile

class Data_base():
		# class.__doc__
	""" Syntax:\n\tData_base( file_name )
	\n Creates a connection to the database
	"""
	def __init__(self, file_name: str) -> bool:
		
		if ".db" not in file_name:
			file_name += ".db"
		self.name_db		= file_name

		if isfile(self.name_db):self.exist		= True
		else:					self.exist		= False	

		self.version_base 	= 0
		self.tables 		= {}
		#self.content 		= {}

	
	# functions for internal use of the object
	def update_tables(self, cursor:sql.Cursor) -> None:
		# class.__doc__
		""" Syntax:\n\tupdate_tables(cursor)
		\n Function for internal use of the object
		\n Updates the list of table names
		"""
		select_sql = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
		if len(select_sql) > 0:
			for table in select_sql:
				table = table[0]
				table_columns = []
				for column in cursor.execute(f'SELECT * FROM {table}').description:
					table_columns.append(column[0])
				self.tables[str(table)] = table_columns


	# other functions
	def connect(self) -> tuple[sql.Connection, sql.Cursor]:
		# class.__doc__
		"""Connects to the database and returns the connection and cursor"""
		
		try:
			connec = sql.connect(self.name_db)
			self.exist = True
		except sql.Error:
			print("Error opening bank.")
			self.exist = False
			return False

		cursor = connec.cursor()
		self.version_base = cursor.execute('SELECT SQLITE_VERSION()').fetchone()
		self.update_tables(cursor)
		return connec, cursor

	def insert(self, table:str, values:list[int | str] | tuple[int | str]) -> bool:
		# class.__doc__
		"""Syntax:\n\tinsert( table_name , [value, value, ...])
		\nInsert a value into the table
		"""

		if table not in self.tables:
			print(f"Table '{table}' doesn't exists")
			return False

		columns = ""
		for column in self.tables[str(table)]:
			columns += f"{column.replace(' ', '_')}, "
		columns = columns[:-2]

		str_values = ""
		for value in values:
			if	 type(value) == type(1)		:	str_values += f"{value}, "
			elif type(value) == type("str")	:	str_values += f"'{value.replace(' ', '_')}', "
		str_values = str_values.removesuffix(', ')

		insert_scheme = f"INSERT INTO {table} ({columns}) VALUES ({str_values})"
		try:
			connection, cursor 	= self.connect()
			cursor.execute(insert_scheme)
			connection.commit()
			connection.close()
			return True
		except sql.Error as error:
			print(f"Error in insert() [{error}]\n{insert_scheme}")
			return False

	def delete(self, table, collum, id):
		if table not in self.tables:
			print(f"Table '{table}' doesn't exists")
			return False

		delete_scheme = f"DELETE FROM {table} where {collum}='{id}'"
		try:
			connection, cursor 	= self.connect()
			cursor.execute(delete_scheme)
			connection.commit()
			connection.close()
			return True
		except sql.Error as error:
			print(f"Error in delete() [{error}]\n{delete_scheme}")
			return False

	def create_table(self, name:str, columns:list[str]) -> bool:
		# class.__doc__
		""" Syntax:\n\tcreate_table('tabela', '''name_colum SQL_PROPERTIES'''
		\nCreates a table if it does't exist
		"""

		if name in self.tables:
			print(f"Table '{name}' already exists")
			return False

		sql_columns = ""
		for item in columns:
			sql_columns += f", {item}"

		table_schema = f"CREATE TABLE {str(name)} ({sql_columns.removeprefix(', ')});"
		try:
			connection, cursor 	= self.connect()
			cursor.execute(table_schema)
			self.update_tables(cursor)
			connection.close()
			return True
		except sql.Error as error:
			print(f"Error in create_table() [{error}]\n{table_schema}")
			return False
		
	def query(self, table:str) -> list[int | str]:
		# class.__doc__
		""" Syntax:\n\tquery( table_name )
		\n list all items in the table
		"""

		content = []
		connection, cursor = self.connect()
		cursor.execute(f"SELECT * FROM {table};")
		for linha in cursor.fetchall():
			content.append(linha)
		connection.close()
		return content