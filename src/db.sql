CREATE TABLE IF NOT EXISTS User(
   user_Id INTEGER,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   email TEXT,
   PRIMARY KEY(user_Id)
);

CREATE TABLE IF NOT EXISTS Product(
   product_Id INTEGER,
   description TEXT,
   technical_specification TEXT,
   price NUMERIC NOT NULL,
   picture TEXT,
   PRIMARY KEY(product_Id)
);

CREATE TABLE IF NOT EXISTS OrderHead(
   order_id INTEGER,
   date_ TEXT NOT NULL,
   quantity INTEGER NOT NULL,
   user_informations TEXT,
   user_Id INTEGER NOT NULL,
   PRIMARY KEY(order_id),
   FOREIGN KEY(user_Id) REFERENCES User_(user_Id)
);

CREATE TABLE IF NOT EXISTS OrderDetail(
   product_Id INTEGER,
   order_id INTEGER,
   PRIMARY KEY(product_Id, order_id),
   FOREIGN KEY(product_Id) REFERENCES Product(product_Id),
   FOREIGN KEY(order_id) REFERENCES Order_(order_id)
);
