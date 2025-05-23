from orders.models import OrderHead
from db_api import DBConnection
from streamlit import session_state as st_session
from datetime import datetime

class BasketDetail():

    def __init__(self, product_id: int):
        self.__product_id = product_id
        self.__quantity = 0

    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def quantity(self):
        return self.__quantity
    
    def add_quantity(self, quantity: int)-> None:
        self.__quantity += quantity

class Basket():

    def __init__(self):
        self.__detail_list: list[BasketDetail] = []

    def __get_detail(self, product_id: int)-> BasketDetail | None:
        for detail in self.__detail_list:
            if detail.product_id == product_id:
                return detail
        return None
    
    def __get_or_create_detail(self, product_id: int)-> BasketDetail:
        detail = self.__get_detail(product_id)
        if detail is None:
            detail = BasketDetail(product_id)
            self.__detail_list.append(detail)
        return detail

    def add(self, product_id: int, quantity: int = 1):
        detail = self.__get_or_create_detail(product_id)
        detail.add_quantity(quantity)
        if detail.quantity == 0:
            self.__detail_list.remove(detail)

    def get_product_list(self)-> list[int]:
        return [detail.product_id for detail in self.__detail_list]
    
    def get_quantity(self, product_id: int)-> int:
        detail = self.__get_detail(product_id)
        if detail is None:
            return 0
        else:
            return detail.quantity
    
    def remove(self, product_id: int)-> None:
        detail = self.__get_detail(product_id)
        if detail is not None:
            self.__detail_list.remove(detail)

    def empty_basket(self):
        self.__detail_list = []
        
    def create_order(self, connection: DBConnection, user_id: int)-> OrderHead:
        if not self.__detail_list:
            raise Exception('Order creation impossible. The basket is empty.')
        connection: DBConnection = st_session['connection']
        order = OrderHead(connection, True)
        order.user_id = user_id
        order.orderhead_date = datetime.today().strftime('%Y-%m-%d')
        order.save_to_db() # we need to save before adding details (we must know the new order's id to continue...)
        for basket_detail in self.__detail_list:
            order.add_product(basket_detail.product_id, basket_detail.quantity)
        order.save_to_db()
        connection.commit()
        return order