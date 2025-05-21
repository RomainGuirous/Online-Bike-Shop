-- If exists, drop the tables
DROP TABLE IF EXISTS OrderDetail;
DROP TABLE IF EXISTS OrderHead;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS User;

CREATE TABLE IF NOT EXISTS User(
   user_Id INTEGER,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   email TEXT,
   PRIMARY KEY(user_Id)
);

CREATE TABLE IF NOT EXISTS Product(
   product_Id INTEGER,
   name TEXT,
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

-- add some bikes
INSERT INTO Product (name, description, technical_specification, price, picture) VALUES
('Electric bike', 'An electric bike for effortless riding.', 'Technical specifications: 250W motor, 36V battery, 3 riding modes', 799.99, 'https://lightroom.adobe.com/shares/e3b958527cf44854aff7fe9713f24402/albums/16aeb2f13fda4a2bb64766a802113ec5/assets/973f75a58c6443d6b77d44715e2e978f');


