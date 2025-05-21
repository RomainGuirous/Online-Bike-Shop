from src.db_api import DBConnection

class User:
    """
    User model representing a user in the database.
    """
    def __init__(self, db_connexion: DBConnection, is_new: bool, user_id: int = None):
        self.__dataset = db_connexion.new_table_record('User', {'user_Id' : user_id}, is_new)

    @property
    def user_id(self):
        return self.__dataset.get_field('user_id')
    @user_id.setter
    def user_id(self, value):
        self.__dataset.set_field('user_Id', value)

    @property
    def first_name(self):
        return self.__dataset.get_field('first_name')
    @first_name.setter
    def first_name(self, value):
        self.__dataset.set_field('first_name', value)

    @property
    def last_name(self):
        return self.__dataset.get_field('last_name')
    @last_name.setter
    def last_name(self, value):
        self.__dataset.set_field('last_name', value)

    @property
    def email(self):
        return self.__dataset.get_field('email')
    @email.setter
    def email(self, value):
        self.__dataset.set_field('email', value)

    def save_to_db(self):
        self.__dataset.save_record()