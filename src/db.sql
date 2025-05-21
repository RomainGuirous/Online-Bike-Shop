-- If exists, drop the tables
DROP TABLE IF EXISTS OrderDetail;
DROP TABLE IF EXISTS OrderHead;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS User;

CREATE TABLE IF NOT EXISTS User(
   user_id INTEGER,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   email TEXT,
   PRIMARY KEY(user_id)
);

CREATE TABLE IF NOT EXISTS SpeTech(
   spetech_id INTEGER,
   spetech_type TEXT,
   color TEXT,
   spetech_weight NUMERIC(15,2),
   brand TEXT,
   frame_size TEXT,
   PRIMARY KEY(spetech_id)
);

CREATE TABLE IF NOT EXISTS Product(
   product_id INTEGER,
   product_name TEXT NOT NULL,
   product_description TEXT,
   price NUMERIC NOT NULL,
   picture TEXT,
   spetech_id INTEGER NOT NULL,
   PRIMARY KEY(product_id),
   FOREIGN KEY(spetech_id) REFERENCES SpeTech(spetech_id)
);

CREATE TABLE IF NOT EXISTS OrderHead(
   orderhead_id INTEGER,
   orderhead_date TEXT NOT NULL,
   quantity INTEGER NOT NULL,
   user_id INTEGER NOT NULL,
   PRIMARY KEY(orderhead_id),
   FOREIGN KEY(user_id) REFERENCES User(user_id)
);

CREATE TABLE IF NOT EXISTS OrderDetail(
   product_id INTEGER,
   orderhead_id INTEGER,
   PRIMARY KEY(product_id, orderhead_id),
   FOREIGN KEY(product_id) REFERENCES Product(product_id),
   FOREIGN KEY(orderhead_id) REFERENCES Orderhead(orderhead_id)
);

-- Insert data into Product table
INSERT INTO Product (product_id, product_name, product_description, price, picture, spetech_id) VALUES
(1, 'Mountain Bike', 'A rugged mountain bike for off-road adventures.', 499.99, 'https://www.serk.cc/wp-content/uploads/2022/10/DSCF2936.jpg', 1),
(2, 'Road Bike', 'A lightweight road bike for speed and efficiency.', 799.99, 'https://www.serk.cc/wp-content/uploads/2022/10/DSCF4542-Edit.jpg', 2),
(3, 'Hybrid Bike', 'A versatile hybrid bike for city and trail riding.', 599.99, 'https://www.serk.cc/wp-content/uploads/2019/07/A21_1920-300x200.jpg', 3),
(4, 'Electric Bike', 'An electric bike for effortless commuting.', 1299.99, 'https://www.serk.cc/wp-content/uploads/2019/07/A10_1920-300x200.jpg', 4),
(5, 'Kids Bike', 'A fun and safe bike for kids.', 199.99, 'https://www.serk.cc/wp-content/uploads/2019/07/a30M_side.jpg', 5);