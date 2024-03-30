import pymysql

MYSQL_HOST = 'localhost'
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'your_database_name'

conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
cursor = conn.cursor()


def get_categories() -> list[dict]:

    return


def get_products(category_id: int) -> list[dict]:
    # if category_id = -1, return all products.
    return

def get_product(product_id: int) -> dict:

    return

def get_user_details(username: str) -> dict:

    return

def get_cart(username: str) -> list[dict]:
    return

def add_to_cart(username: str, product_id: int) -> bool:
    return

def call_for_trial(username: str, product_ids: list[int]) -> bool:
    return

def get_trial_history(username: str) -> list[dict]:
    return

def search_product(prompt: str) -> list[dict]:
    return

def get_order_history(username: str) -> list[dict]:
    return

def checkout(username: str, product_id: int) -> bool:
    return

def validate_login(username: str, password: str) -> bool:

    return

def register_user(data: dict) -> bool:

    return


