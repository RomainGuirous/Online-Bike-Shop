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


