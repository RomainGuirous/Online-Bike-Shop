from orders.models import OrderHead
from db_api import DBConnection
from datetime import datetime


class BasketDetail:
    """
    A class representing a detail of a product in the shopping basket.
    It contains the product ID and the quantity of that product in the basket.
    It allows adding to the quantity of the product.
    """

    def __init__(self, product_id: int):
        self.__product_id = product_id
        self.__quantity = 0

    @property
    def product_id(self):
        return self.__product_id

    @property
    def quantity(self):
        return self.__quantity

    def add_quantity(self, quantity: int) -> None:
        self.__quantity += quantity


class Basket:
    """
    A class representing a shopping basket.
    It allows adding, removing, and managing products in the basket.
    It can also create an order from the basket contents."""

    def __init__(self):
        self.__detail_list: list[BasketDetail] = []

    def __get_detail(self, product_id: int) -> BasketDetail | None:
        """
        Retrieves a BasketDetail by product_id.
        If the product_id is not found, it returns None.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            BasketDetail | None: The BasketDetail if found, otherwise None.
        """
        for detail in self.__detail_list:
            if detail.product_id == product_id:
                return detail
        return None

    def __get_or_create_detail(self, product_id: int) -> BasketDetail:
        """
        Retrieves a BasketDetail by product_id, or creates a new one if it does not exist.

        Args:
            product_id (int): The ID of the product to retrieve or create.

        Returns:
            BasketDetail: The existing or newly created BasketDetail.
        """
        detail = self.__get_detail(product_id)
        if detail is None:
            detail = BasketDetail(product_id)
            self.__detail_list.append(detail)
        return detail

    def add(self, product_id: int, quantity: int = 1) -> None:
        """
        Adds a product to the basket or updates its quantity if it already exists.

        Args:
            product_id (int): The ID of the product to add.
            quantity (int): The quantity of the product to add. Defaults to 1.

        Raises:
            Exception: If the quantity is less than 1.

        Returns:
            None
        """
        detail = self.__get_or_create_detail(product_id)
        detail.add_quantity(quantity)
        if detail.quantity == 0:
            self.__detail_list.remove(detail)

    def get_product_list(self) -> list[int]:
        """
        Returns a list of product IDs in the basket.
        This method iterates through the detail list and collects the product IDs.

        Returns:
            list[int]: A list of product IDs in the basket.
        """
        return [detail.product_id for detail in self.__detail_list]

    def get_quantity(self, product_id: int) -> int:
        detail = self.__get_detail(product_id)
        if detail is None:
            return 0
        else:
            return detail.quantity

    def remove(self, product_id: int) -> None:
        detail = self.__get_detail(product_id)
        if detail is not None:
            self.__detail_list.remove(detail)

    def empty_basket(self):
        self.__detail_list = []

    def create_order(self, connection: DBConnection, user_id: int) -> OrderHead:
        """
        Creates an order from the basket contents.
        This method creates an OrderHead instance, adds all products from the basket,
        and saves the order to the database.

        Args:
            connection (DBConnection): The database connection object.
            user_id (int): The ID of the user creating the order.

        Raises:
            Exception: If the basket is empty.

        Returns:
            OrderHead: The created OrderHead instance.
        """
        if not self.__detail_list:
            raise Exception("Order creation impossible. The basket is empty.")
        order = OrderHead(connection, True)
        order.user_id = user_id
        order.orderhead_date = datetime.today().strftime("%Y-%m-%d")
        order.save_to_db()  # we need to save before adding details (we must know the new order's id to continue...)
        for basket_detail in self.__detail_list:
            order.add_product(basket_detail.product_id, basket_detail.quantity)
        order.save_to_db()
        connection.commit()
        self.empty_basket()
        return order
