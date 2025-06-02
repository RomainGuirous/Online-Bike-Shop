from db_api import ConnectionType, DBConnection


class Product:
    """
    Product model representing a product in the database.
    """

    def __init__(
        self, db_connection: DBConnection, is_new: bool, product_id: any = None
    ):
        """
        Initializes a Product instance.

        :param db_connection: The database connection object.
        :param is_new: Boolean indicating if this is a new product.
        :param product_id: The ID of the product. If None, a new product will be created.
        :raises ValueError: If product_id is None and is_new is False.
        """
        if db_connection.is_of_type(ConnectionType.SQLITE):
            self.__id_field_name = "product_id"
            self.__record = db_connection.get_record_object(
                "Product", {"product_id": product_id}, is_new
            )
        else:
            self.__id_field_name = "_id"
            self.__record = db_connection.get_record_object(
                "Product", product_id, is_new
            )

    @property
    def product_id(self):
        return self.__record.get_field(self.__id_field_name)

    @product_id.setter
    def product_id(self, value):
        self.__record.set_field(self.__id_field_name, value)

    @property
    def product_name(self):
        return self.__record.get_field("product_name")

    @product_name.setter
    def product_name(self, value):
        self.__record.set_field("product_name", value)

    @property
    def product_description(self):
        return self.__record.get_field("product_description")

    @product_description.setter
    def product_description(self, value):
        self.__record.set_field("product_description", value)

    @property
    def price(self):
        return self.__record.get_field("price")

    @price.setter
    def price(self, value):
        self.__record.set_field("price", value)

    @property
    def picture(self):
        return self.__record.get_field("picture")

    @picture.setter
    def picture(self, value):
        self.__record.set_field("picture", value)

    @property
    def spetech_id(self):
        return self.__record.get_field("spetech_id")

    @spetech_id.setter
    def spetech_id(self, value):
        self.__record.set_field("spetech_id", value)

    def save_to_db(self):
        """
        Saves the product to the database.
        If the product is new, it will be created; otherwise, it will be updated.
        If using NoSQL, it saves the product in the collection.
        If using SQL, it executes an INSERT or UPDATE statement based on the is_new flag.
        """
        self.__record.save()
