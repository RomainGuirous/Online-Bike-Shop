from db_api import DBConnection, ConnectionType
import yaml

def get_user_list(db_connection: DBConnection) -> list[dict]:
    """
    Retrieve a DataFrame of all users from the database.
    This function fetches user data from the database and converts it into a DataFrame.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all users.
    """
    users = []
    if db_connection.connection_type == ConnectionType.SQLITE:
        sql = "SELECT * FROM user"
        cursor = db_connection.new_query()
        dataset = cursor.execute(sql)
        for row in dataset:
            user = {
                "user_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "username": row[4],
                "hashed_password": row[5],
                "password_hint": row[6],
                "is_admin": row[7]

            }
            users.append(user)
    #elif db_connection.connection_type == ConnectionType.MONGODB:
    else:
        users_list = db_connection.new_query()["User"].find()
        for user in users_list:
            user_data = {
                "user_id": user.get("_id"),
                "first_name": user.get("first_name"),
                "last_name": user.get("last_name"),
                "email": user.get("email"),
                "username": user.get("username"),
                "hashed_password": user.get("hashed_password"),
                "password_hint": user.get("password_hint"),
                "is_admin": user.get("is_admin")
            }
            users.append(user_data)
    return users

def update_auth_config_froms_users(connection: DBConnection)-> None:
    with open("config.yaml", "r") as file:
        config: dict = yaml.safe_load(file)
    config["credentials"]["usernames"] = {}
    user_list = get_user_list(connection)
    for user_dict in user_list:
        user_yaml = {}
        user_yaml["email"] = user_dict["email"]
        user_yaml["first_name"] = user_dict["first_name"]
        user_yaml["last_name"] = user_dict["last_name"]
        user_yaml["logged_in"] = False
        user_yaml["password"] = user_dict["hashed_password"]
        user_yaml["password_hint"] = user_dict["password_hint"]
        user_yaml["roles"] = ["user"]
        if user_dict["is_admin"]:
            user_yaml["roles"].append("admin")
        config["credentials"]["usernames"][user_dict["username"]] = user_yaml
    with open("config.yaml", "w") as file:
        yaml.dump(config, file)
