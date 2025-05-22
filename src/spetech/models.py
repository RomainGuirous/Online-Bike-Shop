from src.db_api import DBConnection

class SpeTech:
    """
    SpeTecxh model representing technical specifications for any products in the database.
    """

    def __init__(self, db_connection: DBConnection, is_new: bool, spetech_id: int = None):
        self.__record = db_connection.new_table_record('SpeTech', {'spetech_id' : spetech_id}, is_new)

    @property
    def spetech_id(self):
        return self.__record.get_field('spetech_id')
    @spetech_id.setter
    def spetech_id(self, value):
        self.__record.set_field('spetech_id', value)

    @property
    def spetech_type(self):
        return self.__record.get_field('spetech_type')
    @spetech_type.setter
    def spetech_type(self, value):
        self.__record.set_field('spetech_type', value)

    @property
    def color(self):
        return self.__record.get_field('color')
    @color.setter
    def color(self, value):
        self.__record.set_field('color', value)

    @property
    def spetech_weight(self):
        return self.__record.get_field('spetech_weight')
    @spetech_weight.setter
    def spetech_weight(self, value):
        self.__record.set_field('spetech_weight', value)

    @property
    def brand(self):
        return self.__record.get_field('brand')
    @brand.setter
    def brand(self, value):
        self.__record.set_field('brand', value)

    @property
    def frame_size(self):
        return self.__record.get_field('frame_size')
    @frame_size.setter
    def frame_size(self, value):
        self.__record.set_field('frame_size', value)

    def save_to_db(self):
        self.__record.save_record()

