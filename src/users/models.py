from src.db_api import DBConnection

class User:
    """
    User model representing a user in the database.
    """

    def __init__(self, db_connexion: DBConnection, is_new: bool, user_id: int = None):
        self.__record = db_connexion.new_table_record('User', {'user_id' : user_id}, is_new)

    @property
    def user_id(self):
        return self.__record.get_field('user_id')
    @user_id.setter
    def user_id(self, value):
        self.__record.set_field('user_id', value)

    @property
    def first_name(self):
        return self.__record.get_field('first_name')
    @first_name.setter
    def first_name(self, value):
        self.__record.set_field('first_name', value)

    @property
    def last_name(self):
        return self.__record.get_field('last_name')
    @last_name.setter
    def last_name(self, value):
        self.__record.set_field('last_name', value)

    @property
    def email(self):
        return self.__record.get_field('email')
    @email.setter
    def email(self, value):
        self.__record.set_field('email', value)

    def save_to_db(self):
        self.__record.save_record()

