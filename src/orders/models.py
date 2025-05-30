from db_api import ConnectionType, DBConnection

class OrderHead:
    """
    OrderHead model representing a order head in the database.
    """

    def __init__(
        self, db_connection: DBConnection, is_new: bool, orderhead_id: int = None
    ):
        self.__db_connection = db_connection
        self.__detail_records: list[OrderDetail] = []
        if db_connection.connection_type == ConnectionType.SQLITE:
            self.__id_field_name = "orderhead_id"
            self.__record = db_connection.get_record_object(
                "OrderHead", {"orderhead_id": orderhead_id}, is_new
            )
            if not is_new:
                sql = "SELECT product_id FROM OrderDetail WHERE orderhead_id = ?"
                rows = db_connection.new_query().execute(sql, (orderhead_id,)).fetchall()
                for row in rows:
                    self.__detail_records.append(
                        OrderDetail(db_connection, False, self.orderhead_id, row[0])
                    )
        else:
            self.__id_field_name = "_id"
            self.__record = db_connection.get_record_object('OrderHead', orderhead_id, is_new)
            if not is_new:
                rows = db_connection.new_query()['OrderDetail'].find({'orderhead_id' : orderhead_id})
                for row in rows:
                    self.__detail_records.append(row)

    @property
    def orderhead_id(self):
        return self.__record.get_field(self.__id_field_name)

    @orderhead_id.setter
    def orderhead_id(self, value):
        self.__record.set_field(self.__id_field_name, value)

    @property
    def orderhead_date(self):
        return self.__record.get_field("orderhead_date")

    @orderhead_date.setter
    def orderhead_date(self, value):
        self.__record.set_field("orderhead_date", value)

    @property
    def user_id(self):
        return self.__record.get_field("user_id")

    @user_id.setter
    def user_id(self, value):
        self.__record.set_field("user_id", value)

    def add_product(self, product_id: int, quantity: int) -> None:
        if self.__db_connection.connection_type == ConnectionType.SQLITE:
            if not self.__record.created:
                raise Exception("The order's head must be saved before adding details")
            detail = OrderDetail(self.__db_connection, True, self.orderhead_id, product_id)
            detail.quantity = quantity
            self.__detail_records.append(detail)
        else:
            self.__detail_records.append({'product_id': product_id, 'quantity': quantity})

    def details(self) -> list["OrderDetail"]|list[dict]:
        return self.__detail_records

    def save_to_db(self) -> None:
        if self.__db_connection.connection_type == ConnectionType.MONGODB:
            self.__record.set_field("OrderDetails", self.__detail_records)
        self.__record.save()
        if self.__db_connection.connection_type == ConnectionType.SQLITE:
            # we delete details in db then we recreate them (allows to remove OrderDetail(s) which have been deleted)
            self.__db_connection.delete_record(
                "OrderDetail", {"orderhead_id": self.orderhead_id}
            )
            for detail_record in self.__detail_records:
                detail_record.save_to_db()


class OrderDetail():

    def __init__(
        self,
        db_connection: DBConnection,
        is_new: bool,
        orderhead_id: int,
        product_id: int,
    ):
        self.__record = db_connection.get_record_object(
            "OrderDetail",
            {"orderhead_id": orderhead_id, "product_id": product_id},
            is_new,
        )

    @property
    def orderhead_id(self):
        return self.__record.get_field("orderhead_id")

    @orderhead_id.setter
    def orderhead_id(self, value):
        self.__record.set_field("orderhead_id", value)

    @property
    def product_id(self):
        return self.__record.get_field("product_id")

    @product_id.setter
    def product_id(self, value):
        self.__record.set_field("product_id", value)

    @property
    def quantity(self):
        return self.__record.get_field("quantity")

    @quantity.setter
    def quantity(self, value):
        self.__record.set_field("quantity", value)

    def save_to_db(self):
        self.__record.save(
            True
        )  # details are allways created, never updated (see OrderHead.save_to_db())