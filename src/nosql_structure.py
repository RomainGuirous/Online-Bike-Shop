from pymongo import MongoClient

# Connect to MongoDB (default localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# Drop the database if it exists (for fresh start)
# client.drop_database("BikeShopDB")

# Create/use the database
db = client["BikeShopDB"]

# Create collections (MongoDB creates them on first insert)
users = db["User"]
spetechs = db["SpeTech"]
products = db["Product"]
order_heads = db["OrderHead"]
order_details = db["OrderDetail"]

# Insert into Product
products.insert_many(
    [
        {
            "product_id": 1,
            "product_name": "Mountain Bike",
            "product_description": "A rugged mountain bike for off-road adventures.",
            "price": 499.99,
            "picture": "https://www.serk.cc/wp-content/uploads/2022/10/DSCF2936.jpg",
            "spetech_id": 1,
        },
        {
            "product_id": 2,
            "product_name": "Road Bike",
            "product_description": "A lightweight road bike for speed and efficiency.",
            "price": 799.99,
            "picture": "https://www.serk.cc/wp-content/uploads/2022/10/DSCF4542-Edit.jpg",
            "spetech_id": 2,
        },
        {
            "product_id": 3,
            "product_name": "Hybrid Bike",
            "product_description": "A versatile hybrid bike for city and trail riding.",
            "price": 599.99,
            "picture": "https://www.serk.cc/wp-content/uploads/2019/07/A21_1920-300x200.jpg",
            "spetech_id": 3,
        },
        {
            "product_id": 4,
            "product_name": "Electric Bike",
            "product_description": "An electric bike for effortless commuting.",
            "price": 1299.99,
            "picture": "https://www.serk.cc/wp-content/uploads/2019/07/A10_1920-300x200.jpg",
            "spetech_id": 4,
        },
        {
            "product_id": 5,
            "product_name": "Kids Bike",
            "product_description": "A fun and safe bike for kids.",
            "price": 199.99,
            "picture": "https://www.serk.cc/wp-content/uploads/2019/07/a30M_side.jpg",
            "spetech_id": 5,
        },
    ]
)

# Insert into OrderHead
order_heads.insert_many(
    [
        {"orderhead_id": 1, "orderhead_date": "2023-10-01", "user_id": 1},
        {"orderhead_id": 2, "orderhead_date": "2023-10-02", "user_id": 2},
        {"orderhead_id": 3, "orderhead_date": "2023-10-03", "user_id": 3},
        {"orderhead_id": 4, "orderhead_date": "2023-10-04", "user_id": 4},
        {"orderhead_id": 5, "orderhead_date": "2023-10-05", "user_id": 5},
        {"orderhead_id": 6, "orderhead_date": "2023-10-06", "user_id": 1},
        {"orderhead_id": 7, "orderhead_date": "2023-10-07", "user_id": 2},
        {"orderhead_id": 8, "orderhead_date": "2023-10-08", "user_id": 3},
        {"orderhead_id": 9, "orderhead_date": "2023-10-09", "user_id": 4},
        {"orderhead_id": 10, "orderhead_date": "2023-10-10", "user_id": 5},
    ]
)

# Insert into OrderDetail
order_details.insert_many(
    [
        {"orderhead_id": 1, "product_id": 1, "quantity": 2},
        {"orderhead_id": 1, "product_id": 2, "quantity": 1},
        {"orderhead_id": 2, "product_id": 3, "quantity": 1},
        {"orderhead_id": 2, "product_id": 4, "quantity": 2},
        {"orderhead_id": 3, "product_id": 5, "quantity": 1},
        {"orderhead_id": 4, "product_id": 1, "quantity": 1},
        {"orderhead_id": 5, "product_id": 2, "quantity": 3},
        {"orderhead_id": 6, "product_id": 3, "quantity": 2},
        {"orderhead_id": 7, "product_id": 4, "quantity": 1},
        {"orderhead_id": 8, "product_id": 5, "quantity": 4},
    ]
)

# Insert into SpeTech
spetechs.insert_many(
    [
        {
            "spetech_id": 1,
            "spetech_type": "Bike",
            "color": "Red",
            "spetech_weight": 12.5,
            "brand": "Speedster",
            "frame_size": "M",
        },
        {
            "spetech_id": 2,
            "spetech_type": "Bike",
            "color": "Blue",
            "spetech_weight": 13.0,
            "brand": "TrailBlazer",
            "frame_size": "L",
        },
        {
            "spetech_id": 3,
            "spetech_type": "Bike",
            "color": "Green",
            "spetech_weight": 11.5,
            "brand": "EcoRider",
            "frame_size": "S",
        },
        {
            "spetech_id": 4,
            "spetech_type": "Bike",
            "color": "Yellow",
            "spetech_weight": 12.0,
            "brand": "SunRider",
            "frame_size": "M",
        },
        {
            "spetech_id": 5,
            "spetech_type": "Bike",
            "color": "Black",
            "spetech_weight": 14.0,
            "brand": "NightRider",
            "frame_size": "XL",
        },
        {
            "spetech_id": 6,
            "spetech_type": "Bike",
            "color": "White",
            "spetech_weight": 12.8,
            "brand": "CloudRider",
            "frame_size": "M",
        },
    ]
)

# Insert into User
users.insert_many(
    [
        {
            "user_id": 1,
            "username": "johndoe",
            "password": "securepassword123",
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
        },
        {
            "user_id": 2,
            "username": "janedoe",
            "password": "securepassword456",
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@example.com",
        },
        {
            "user_id": 3,
            "username": "alice",
            "password": "securepassword789",
            "first_name": "Alice",
            "last_name": "Wonderland",
            "email": "alice@example.com",
        },
        {
            "user_id": 4,
            "username": "bob",
            "password": "securepassword101",
            "first_name": "Bob",
            "last_name": "Builder",
            "email": "bob@example.com",
        },
        {
            "user_id": 5,
            "username": "charlie",
            "password": "securepassword202",
            "first_name": "Charlie",
            "last_name": "Brown",
            "email": "charlie@example.com",
        },
    ]
)
