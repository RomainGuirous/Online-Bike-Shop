from db_api import ConnectionType, DBConnection


class User:
    """
    User model representing a user in the database.
    It contains fields for user ID, first name, last name, and email.
    It provides methods to get and set these fields, and to save the user record to the database.
    """

    def __init__(self, db_connection: DBConnection, is_new: bool, user_id: int = None):
        if db_connection.connection_type == ConnectionType.SQLITE:
            self.__id_field_name = "user_id"
            self.__record = db_connection.get_record_object(
                "User", {"user_id": user_id}, is_new
            )
        else:
            self.__id_field_name = "_id"
            self.__record = db_connection.get_record_object("User", user_id, is_new)

    @property
    def user_id(self):
        return self.__record.get_field(self.__id_field_name)

    @user_id.setter
    def user_id(self, value):
        self.__record.set_field(self.__id_field_name, value)

    @property
    def first_name(self):
        return self.__record.get_field("first_name")

    @first_name.setter
    def first_name(self, value):
        self.__record.set_field("first_name", value)

    @property
    def last_name(self):
        return self.__record.get_field("last_name")

    @last_name.setter
    def last_name(self, value):
        self.__record.set_field("last_name", value)

    @property
    def email(self):
        return self.__record.get_field("email")

    @email.setter
    def email(self, value):
        self.__record.set_field("email", value)

    @property
    def username(self):
        return self.__record.get_field("username")

    @username.setter
    def username(self, value):
        self.__record.set_field("username", value)

    @property
    def hashed_password(self):
        return self.__record.get_field("hashed_password")

    @hashed_password.setter
    def hashed_password(self, value):
        self.__record.set_field("hashed_password", value)

    @property
    def password_hint(self):
        return self.__record.get_field("password_hint")

    @password_hint.setter
    def password_hint(self, value):
        self.__record.set_field("password_hint", value)

    @property
    def is_admin(self):
        return self.__record.get_field('is_admin')
    
    @is_admin.setter
    def is_admin(self, value):
        self.__record.set_field('is_admin', value)

    def save_to_db(self):
        self.__record.save()
