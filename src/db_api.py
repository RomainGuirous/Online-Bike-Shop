from sqlite3 import connect
from sqlite3 import Cursor
from sqlite3 import Error
from config import DB_FILE
from pymongo import MongoClient
from pymongo.database import Database


class DBConnection:
    """
    A class to manage the connection to a SQLite database.
    This class provides methods to create a new cursor, commit changes,
    execute scripts from a file, create new table records, and delete records.
    """

    def __init__(self, db_file: str):
        self.__connection = None
        try:
            self.__connection = connect(db_file)
        except Error as e:
            print(e)

    def new_cursor(self) -> Cursor:
        return self.__connection.cursor()

    def commit(self) -> None:
        self.__connection.commit()

    def executescript(self, filename: str) -> None:
        contenu = open(filename, "r").read()
        self.new_cursor().executescript(contenu)

    def new_table_record(
        self, table_name: str, primary_keys: dict, is_new: bool
    ) -> "DBTableRecord":
        """
        Creates a new DBTableRecord instance for the specified table and primary keys.
        """
        return DBTableRecord(self, table_name, primary_keys, is_new)

    def delete_record(self, table_name: str, primary_keys: dict) -> None:
        """
        Deletes a record from the specified table using the provided primary keys.
        Raises an exception if no primary keys are provided.

        Args:
            table_name (str): The name of the table from which to delete the record.
            primary_keys (dict): A dictionary containing the primary key fields and their values.

        Raises:
            Exception: If no primary keys are provided or if the primary key value is unknown.

        Returns:
            None
        """
        if not primary_keys:
            raise Exception("Record deletion error : unknown primary key value")
        sql = f"DELETE FROM {table_name} WHERE "
        and_keyword = ""
        for field_name in primary_keys:
            sql += f"{and_keyword}{field_name} = :{field_name}"
            and_keyword = " AND "
        self.new_cursor().execute(sql, primary_keys)

class DBTableRecord:
    """
    A class representing a record in a database table.
    This class provides methods to get and set field values, save the record,
    and manage primary keys.
    """

    def __init__(
        self,
        db_connection: DBConnection,
        table_name: str,
        primary_keys: dict,
        is_new: bool,
    ):
        def set_fieldnames_from_row_description(description) -> None:
            """
            Sets the field names for the record based on the row description.
            This method initializes the fields dictionary with field names
            from the row description, setting their initial values to None.

            Args:
                description (list): A list of tuples representing the row description,
                                    where each tuple contains field name and type information.

            Raises:
                Exception: If the description is empty or not provided.

            Returns:
                None
            """
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
            # sql_params['table'] = table_name
            cursor = self.__db_connection.new_cursor()
            dataset = cursor.execute(sql, sql_params)
            set_fieldnames_from_row_description(dataset.description)
            # read the fields' values
            row = dataset.fetchone()
            for field_index in range(len(self.__fields)):
                field_name = list(self.__fields.keys())[field_index]
                self.set_field(field_name, row[field_index])

    @property
    def table(self) -> bool:
        return self.__table

    @property
    def created(self) -> bool:
        return not self.__is_new

    def get_field(self, field_name: str) -> any:
        """
        Retrieves the value of a specified field from the record.

        Args:
            field_name (str): The name of the field to retrieve.

        Raises:
            Exception: If the specified field does not exist in the record.

        Returns:
            any: The value of the specified field.
        """
        if field_name not in self.__fields.keys():
            raise Exception(f"The field '{field_name}' was not found.")
        return self.__fields[field_name]

    def set_field(self, field_name: str, new_value: any) -> None:
        """
        Sets the value of a specified field in the record.

        Args:
            field_name (str): The name of the field to set.
            new_value (any): The new value to assign to the field.

        Raises:
            Exception: If the specified field does not exist in the record.

        Returns:
            None
        """
        if field_name not in self.__fields.keys():
            raise Exception(f"The field '{field_name}' was not found.")
        self.__fields[field_name] = new_value

    def save_record(self, force_insert=False) -> None:
        """
        Saves the current record to the database.
        If the record is new, it performs an INSERT operation.
        If the record already exists, it performs an UPDATE operation.
        If `force_insert` is set to True, it forces an INSERT operation regardless of the record's state.

        Args:
            force_insert (bool): If True, forces an INSERT operation even if the record already exists.

        Raises:
            Exception: If the record is not new and no primary keys are set.

        Returns:
            None
        """
        if force_insert:
            self.__is_new = True
        if self.__is_new:
            sql = f"INSERT INTO {self.table} ("
            comma = ""
            for field_name in self.__fields:
                if not (
                    (field_name in self.__pk_list)
                    and (self.__fields[field_name] is None)
                ):
                    sql += f"{comma}{field_name}"
                    comma = ", "
            sql += ") values ("
            comma = ""
            for field_name in self.__fields:
                if not (
                    (field_name in self.__pk_list)
                    and (self.__fields[field_name] is None)
                ):
                    sql += f"{comma}:{field_name}"
                    comma = ", "
            sql += ")"
        else:
            sql = f"UPDATE {self.table} SET "
            comma = ""
            for field_name in self.__fields:
                if field_name not in self.__pk_list:
                    sql += f"{comma}{field_name} = :{field_name}"
                    comma = ", "
            sql += " WHERE "
            and_keyword = ""
            for field_name in self.__fields:
                if field_name in self.__pk_list:
                    sql += f"{and_keyword}{field_name} = :{field_name}"
                    and_keyword = " AND "
        cursor = self.__db_connection.new_cursor()
        cursor.execute(sql, self.__fields)
        if self.__is_new:
            for field_name, fieldvalue in self.__fields.items():
                if (fieldvalue is None) and (field_name in self.__pk_list):
                    self.set_field(field_name, cursor.lastrowid)
                    break
        cursor.close()
        self.__is_new = False

class DBDocument:

    def __init__(
        self,
        mongodb_db_connection: Database,
        collection: str,
        document_id: str|None,
    ):
        self.__db_connection:Database = mongodb_db_connection
        self.__collection = collection
        self.__is_new = (document_id is None)
        self.__document = {}
        if self.created:
            collection = self.__db_connection[self.__collection]
            self.__document = collection.find_one({"_id": document_id})

    @property
    def collection(self) -> bool:
        return self.__collection

    @property
    def created(self) -> bool:
        return not self.__is_new

    def get_field(self, field_name: str) -> any:
        return self.__document.get(field_name, None)

    def set_field(self, field_name: str, new_value: any) -> None:
        self.__document[field_name] = new_value

    def save_document(self) -> None:
        document_content = dict(self.__document)
        if "_id" in document_content:
            del document_content["_id"]
        if self.__is_new:
            response = self.__db_connection[self.__collection].insert_one(document_content)
            self.__document['_id'] = response.inserted_id
        else:
            self.__db_connection[self.__collection].update_one({'_id' : self.__document['_id']}, {'$set': document_content})
        self.__is_new = False


def create_connection() -> DBConnection | Database:
    """
    Creates a new database connection to the SQLite database specified by DB_FILE.
    This function initializes a DBConnection instance and returns it.

    Returns:
        DBConnection: An instance of the DBConnection class connected to the database.
    """
    if False:
        return DBConnection(DB_FILE)
    else:
        return MongoClient("mongodb://localhost:27017/")["online_bike_shop"]
