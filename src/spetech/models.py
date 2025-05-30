from db_api import ConnectionType, DBConnection


class SpeTech:
    """
    SpeTech model representing technical specifications for any products in the database.
    """

    def __init__(
        self, db_connection: DBConnection, is_new: bool, spetech_id: int = None
    ):
        if db_connection.connection_type == ConnectionType.SQLITE:
            self.__id_field_name = "spetech_id"
            self.__record = db_connection.get_record_object(
                "SpeTech", {"spetech_id": spetech_id}, is_new
            )
        else:
            self.__id_field_name = "_id"
            self.__record = db_connection.get_record_object(
                "SpeTech", spetech_id, is_new
            )

    @property
    def spetech_id(self):
        return self.__record.get_field(self.__id_field_name)

    @spetech_id.setter
    def spetech_id(self, value):
        self.__record.set_field(self.__id_field_name, value)

    @property
    def spetech_type(self):
        return self.__record.get_field("spetech_type")

    @spetech_type.setter
    def spetech_type(self, value):
        self.__record.set_field("spetech_type", value)

    @property
    def color(self):
        return self.__record.get_field("color")

    @color.setter
    def color(self, value):
        self.__record.set_field("color", value)

    @property
    def spetech_weight(self):
        return self.__record.get_field("spetech_weight")

    @spetech_weight.setter
    def spetech_weight(self, value):
        self.__record.set_field("spetech_weight", value)

    @property
    def brand(self):
        return self.__record.get_field("brand")

    @brand.setter
    def brand(self, value):
        self.__record.set_field("brand", value)

    @property
    def frame_size(self):
        return self.__record.get_field("frame_size")

    @frame_size.setter
    def frame_size(self, value):
        self.__record.set_field("frame_size", value)

    def save_to_db(self):
        self.__record.save()
