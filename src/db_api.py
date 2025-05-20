from sqlite3 import connect
from sqlite3 import Connection
from sqlite3 import Cursor
from sqlite3 import Error

class DBConnection:
    
    def __init__(self, db_file: str):
        self.__connection = None
        try:
            self.__connection = connect(db_file)
        except Error as e:
            print(e)

    def new_cursor(self)-> Cursor:
        return self.__connection.cursor()
    
    def commit(self)-> None:
        self.__connection.commit()
    
    def executescript(self,filename: str)-> None:
        contenu = open(filename, 'r').read()
        self.new_cursor().executescript(contenu)

    def new_table_record(self, table_name: str, primary_keys: dict, is_new: bool)-> "DBTableRecord":
        return DBTableRecord(self, table_name, primary_keys, is_new)

    def delete_record(self, table_name: str, primary_keys: dict)-> None:
        pass

class DBTableRecord:
    
    def __init__(self, db_connection: DBConnection, table_name: str, primary_keys: dict, is_new: bool):

        def set_fieldnames_from_row_description(description)-> None:
            for field_description in description:
                self.__fields[field_description[0]] = None

        self.__db_connection = db_connection
        self.__table = table_name
        self.__is_new = is_new
        self.__pk_list = [field_name for field_name in primary_keys]
        self.__fields = {}
        if is_new:
            sql = f"SELECT * FROM {self.table} LIMIT 0"
            cursor = self.__db_connection.new_cursor()
            row = cursor.execute(sql)
            set_fieldnames_from_row_description(row.description)
            for name, value in primary_keys.items():
                self.set_field(name, value)
        else:
            sql = f"SELECT * FROM {self.table} WHERE"
            and_keyword = ""
            for pk_field in primary_keys:
                sql += f" {and_keyword} {pk_field} = :{pk_field}"
                and_keyword = "and"
            sql_params = {}
            sql_params.update(primary_keys)
            #sql_params['table'] = table_name
            cursor = self.__db_connection.new_cursor()
            dataset = cursor.execute(sql, sql_params)
            set_fieldnames_from_row_description(dataset.description)
            # read the fields' values
            row = dataset.fetchone()
            for field_index in range(len(self.__fields)):
                field_name = list(self.__fields.keys())[field_index]
                self.set_field(field_name, row[field_index])

    @property
    def table(self)-> bool:
        return self.__table
    
    @property
    def created(self)-> bool:
        return not self.__is_new

    def get_field(self, field_name: str)-> any:
        if not field_name in self.__fields.keys():
            raise Exception(f"The field '{field_name}' was not found.")
        return self.__fields[field_name]

    def set_field(self, field_name: str, new_value: any)-> None:
        if not field_name in self.__fields.keys():
            raise Exception(f"The field '{field_name}' was not found.")
        self.__fields[field_name] = new_value

    def save_record(self)-> None:
        if self.__is_new:
            sql = f"INSERT INTO {self.table} ("
            comma = ''
            for field_name in self.__fields:
                if not((field_name in self.__pk_list) and (self.__fields[field_name] == 'AUTO')):
                    sql += f"{comma}{field_name}"
                    comma = ', '
            sql += ") values ("
            comma = ''
            for field_name in self.__fields:
                if not((field_name in self.__pk_list) and (self.__fields[field_name] == 'AUTO')):
                    sql += f"{comma}:{field_name}"
                    comma = ', '
            sql += ")"
        else:
            sql = f"UPDATE {self.table} SET "
            comma = ''
            for field_name in self.__fields:
                if not field_name in self.__pk_list:
                    sql += f"{comma}{field_name} = :{field_name}"
                    comma = ', '
            sql += " WHERE "
            and_keyword = ''
            for field_name in self.__fields:
                if field_name in self.__pk_list:
                    sql += f"{and_keyword}{field_name} = :{field_name}"
                    and_keyword = ' AND '
        cursor = self.__db_connection.new_cursor()
        dataset = cursor.execute(sql, self.__fields)
        cursor.close()
        self.__is_new = False