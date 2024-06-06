import sqlite3 as sql
from os.path import isfile

# Class type Exceptions
class Generic_Error             (Exception):
    def __init__(self, message                          ) -> None:
        super().__init__(message)

class TableAlreadyExists_Error  (Exception):
    def __init__(self, table_name:str, scheme:str = ''  ) -> None:
        message = f"\n> Error\t : The '{table_name}' table already exists.\n> Scheme : {scheme}"
        super().__init__(message)

class TableDoNotExists_Error    (Exception):
    def __init__(self, table_name:str, scheme:str = ''  ) -> None:
        message = f"\n> Error\t : The '{table_name}' table doesn't exists.\n> Scheme : {scheme}"
        super().__init__(message)

class TableNeedsCollumns_Error  (Exception):
    def __init__(self, table_name:str, collumns:str = '') -> None:
        message = f"\n> Error\t : The '{table_name}' table needs collumns:\n {collumns}"
        super().__init__(message)

class OpeningDataBase_Error     (Exception):
    def __init__(self, error:sql.Error                  ) -> None:
        message = f"\n> Error\t : Error opening database.\n> {error}"
        super().__init__(message)

class EmptyValues_Error         (Exception):
    def __init__(self                                   ) -> None:
        message = f"\n> Error\t : The list of values cannot be empty."
        super().__init__(message)

class EmptyCollumn_Error        (Exception):
    def __init__(self                                   ) -> None:
        message = f"\n> Error\t : It is necessary to inform the query collumn."
        super().__init__(message)

class EmptyID_Error             (Exception):
    def __init__(self                                   ) -> None:
        message = f"\n> Error\t : It is necessaty to inform the query ID."
        super().__init__(message)







# Main Class
class SQL_DB():
    def __init__(self, file_path:str) -> None:
        if '.db' not in file_path: file_path += '.db'

        if isfile(file_path): self.file_exist = True
        else                : self.file_exist = False

        self.file_path        = file_path
        self.version_base     = self.get_version_base()
        self.table_properties = {}
        self.table_data       = {}

        self.load_db()

    def connect(self) -> tuple[sql.Connection, sql.Cursor]:
        """ Connects to the database file and returns the connection and cursor """
        
        try:
            connection = sql.connect(self.file_path)
            self.file_exist = True
        except sql.Error as error:
            self.file_exist = False
            raise OpeningDataBase_Error(error)
        
        cursor = connection.cursor()
        return connection, cursor

    def get_version_base(self) -> str:
        connection, cursor = self.connect()
        version = cursor.execute('SELECT SQLITE_VERSION()').fetchall()[0][0]
        connection.close()
        return version

    def load_db(self) -> None:
        """ Updates the list of tables with their properties """

        connection, cursor = self.connect()
        list_table_names = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchone()
        if list_table_names != None:
            for table in list_table_names:
                table_data = cursor.execute(f'SELECT * FROM {table}')
                table_columns = [column[0] for column in table_data.description]
                self.table_properties.update({table: {}})
                self.table_properties[table].update({'collumns': table_columns })
                self.table_properties[table].update({'content' : {}            })

                for row in table_data:
                    data = [item for item in row]
                    primary_key = data[0]
                    self.table_properties[str(table)]['content'].update({primary_key: {}})
                    for index, collumn in enumerate(self.table_properties[str(table)]['collumns']):
                        self.table_properties[str(table)]['content'][primary_key].update({collumn: data[index]})
        connection.close()

    def insert(self, table_name:str, values:list[str]) -> bool:
        """ Insert a value into the table.

            `table_name` : The name of the table to be inserted.
               `Values` : Values ​​to be inserted into the table according to the order of the columns.
        """

        if table_name not in self.table_properties:
            raise TableDoNotExists_Error(table_name)
        if len(values) == 0:
            raise EmptyValues_Error()

        collumns_str:str = ''
        for collumn in self.table_properties[str(table_name)]['collumns']:
            collumn:str
            collumns_str += f'{collumn.replace(' ', '_')}, '
        collumns_str = collumns_str.removesuffix(', ')

        values_str:str = ''
        for value in values:
            match value:
                case int(): values_str += f"{value}, "
                case str(): values_str += f"'{value.replace(' ', '_')}', "
        values_str = values_str.removesuffix(", ")

        insert_scheme = f"INSERT INTO {table_name} ({collumns_str}) VALUES ({values_str});"
        try:
            connection, cursor = self.connect()
            cursor.execute(insert_scheme)
            connection.commit()
            connection.close()
            self.load_db()
            return True
        except sql.Error as error:
            raise Generic_Error(f"Error: {error}\nScheme: {insert_scheme}")

    def create_table(self, table_name:str, collumns:list[str]) -> bool:
        """ Create a table if it does't exist.
            \n
            `table_name` : The name of the table to be created.
             `collumns`  : A list with the names of the columns of the table to be created.
        """

        if table_name in self.table_properties:
            raise TableAlreadyExists_Error(table_name)
        if len(collumns) == 0:
            raise TableNeedsCollumns_Error(table_name, collumns)

        sql_collumns = ''
        for item in collumns: sql_collumns += f', {item}'
        sql_collumns = sql_collumns.removeprefix(', ')

        table_scheme = f"CREATE TABLE {str(table_name)} ({sql_collumns});"
        try:
            connection, cursor = self.connect()
            cursor.execute(table_scheme)
            connection.close()
            self.load_db()
            return True
        except sql.Error:
            raise TableAlreadyExists_Error(table_name, table_scheme)

    def query(self, table_name:str) -> list[any]:
        """ List all items in the table.
            \n
            `table_name` : The name of the table to be queried.
        """

        if table_name in self.table_properties:
            raise TableAlreadyExists_Error(table_name)

        connection, cursor = self.connect()
        cursor.execute(f"SELECT * FROM {table_name};")
        content = [linha for linha in cursor.fetchall()]
        connection.close()
        self.load_db()
        return content

    def delete(self, table_name:str, collumn:str = None, id:str | int = None) -> bool:
        
        if table_name not in self.table_properties:
            raise TableDoNotExists_Error(table_name)
        if collumn == "" or collumn == None:
            raise EmptyCollumn_Error()
        if id == "" or id == None:
            raise EmptyID_Error()
        
        delete_scheme = f"DELETE FROM {table_name} WHERE {collumn}='{id}'"
        try:
            connection, cursor = self.connect()
            cursor.execute(delete_scheme)
            connection.commit()
            connection.close()
            self.load_db()
            return True
        except sql.Error as error:
            raise Generic_Error(f"Error: {error}\nScheme: {delete_scheme}")
