CREATE TABLE IF NOT EXISTS User(
   user_id INTEGER,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   email TEXT NOT NULL,
   username TEXT NOT NULL,
   hashed_password TEXT NOT NULL,
   password_hint TEXT,
   is_admin INTEGER,
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
   user_id INTEGER NOT NULL,
   PRIMARY KEY(orderhead_id),
   FOREIGN KEY(user_id) REFERENCES User(user_id)
);

CREATE TABLE IF NOT EXISTS OrderDetail(
   orderhead_id INTEGER,
   product_id INTEGER,
   quantity INTEGER NOT NULL,
   PRIMARY KEY(product_id, orderhead_id),
   FOREIGN KEY(product_id) REFERENCES Product(product_id),
   FOREIGN KEY(orderhead_id) REFERENCES Orderhead(orderhead_id)
);

-- Insert data into Product table
INSERT OR REPLACE INTO Product (product_id, product_name, product_description, price, picture, spetech_id) VALUES
(1, 'Mountain Bike', 'A rugged mountain bike for off-road adventures.', 499.99, 'https://www.serk.cc/wp-content/uploads/2022/10/DSCF2936.jpg', 1),
(2, 'Road Bike', 'A lightweight road bike for speed and efficiency.', 799.99, 'https://www.serk.cc/wp-content/uploads/2022/10/DSCF4542-Edit.jpg', 2),
(3, 'Hybrid Bike', 'A versatile hybrid bike for city and trail riding.', 599.99, 'https://www.serk.cc/wp-content/uploads/2019/07/A21_1920-300x200.jpg', 3),
(4, 'Electric Bike', 'An electric bike for effortless commuting.', 1299.99, 'https://www.serk.cc/wp-content/uploads/2019/07/A10_1920-300x200.jpg', 4),
(5, 'Kids Bike', 'A fun and safe bike for kids.', 199.99, 'https://www.serk.cc/wp-content/uploads/2019/07/a30M_side.jpg', 5);

-- Insert data into Order table
INSERT OR REPLACE INTO OrderHead (orderhead_id, orderhead_date, user_id) VALUES
(1, '2023-10-01', 1),
(2, '2023-10-02', 2),
(3, '2023-10-03', 3),
(4, '2023-10-04', 4),
(5, '2023-10-05', 5),
(6, '2023-10-06', 1),
(7, '2023-10-07', 2),
(8, '2023-10-08', 3),
(9, '2023-10-09', 4),
(10, '2023-10-10', 5);

-- Insert data into OrderDetail table
INSERT OR REPLACE INTO OrderDetail (orderhead_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(2, 4, 2),
(3, 5, 1),
(4, 1, 1),
(5, 2, 3),
(6, 3, 2),
(7, 4, 1),
(8, 5, 4);

INSERT OR REPLACE INTO User (first_name, last_name, email, username, hashed_password, password_hint, roles) VALUES
('John', 'Doe', 'john.doe@example.com', 'johndoe', '$2b$12$KIXQ1Q1Q1Q1Q1Q1Q1Q1Q1u', 'test', 'user'),
('Jane', 'Smith', 'jane.smith@example.com', 'janesmith', '$2b$12$KIXQ1Q1Q1Q1Q1Q1Q1Q1Q1u', 'test', 'user'),
('Alice', 'Johnson', 'alice.johnson@example.com', 'alicejohnson', '$2b$12$KIXQ1Q1Q1Q1Q1Q1Q1Q1Q1u', 'test', 'user'),
('Bob', 'Brown', 'bob.brown@example.com', 'bobbrown', '$2b$12$KIXQ1Q1Q1Q1Q1Q1Q1Q1Q1u', 'test', 'user'),
('Charlie', 'Davis', 'charlie.davis@example.com', 'charliedavis', '$2b$12$KIXQ1Q1Q1Q1Q1Q1Q1Q1Q1u', 'test', 'user');