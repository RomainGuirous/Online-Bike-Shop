from db_api import DBConnection

class Product:
    """
    Product model representing a product in the database.
    """
    def __init__(self, db_connection: DBConnection, is_new: bool, product_id: int = None):
        self.__record = db_connection.new_table_record('Product', {'product_id' : product_id}, is_new)

    @property
    def product_id(self):
        return self.__record.get_field('product_id')
    @product_id.setter
    def product_id(self, value):
        self.__record.set_field('product_id', value)

    @property
    def product_name(self):
        return self.__record.get_field('product_name')
    @product_name.setter
    def product_name(self, value):
        self.__record.set_field('product_name', value)

    @property
    def product_description(self):
        return self.__record.get_field('product_description')
    @product_description.setter
    def product_description(self, value):
        self.__record.set_field('product_description', value)

    @property
    def price(self):
        return self.__record.get_field('price')
    @price.setter
    def price(self, value):
        self.__record.set_field('price', value)

    @property
    def picture(self):
        return self.__record.get_field('picture')
    @picture.setter
    def picture(self, value):
        self.__record.set_field('picture', value)

    @property
    def spetech_id(self):
        return self.__record.get_field('spetech_id')
    @spetech_id.setter
    def spetech_id(self, value):
        self.__record.set_field('spetech_id', value)

    def save_to_db(self):
        self.__record.save_record()