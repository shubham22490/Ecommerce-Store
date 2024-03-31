import pymysql
from datetime import datetime
from fastapi import FASTAPI
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'mydb'

# show all different categories
@app.get("/show_product_categories")
def get_categories() -> list[dict]:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()

    # Fetch column names for the product_category table
    table_name = 'product_category'  
    my_cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_names = my_cursor.fetchall()
    column_names = [col[0] for col in column_names]
    # Fetch records from the product_category table
    my_cursor.execute("SELECT * FROM product_category")
    records = my_cursor.fetchall()
    # Construct dictionary with column names as keys and record values as values
    result = []
    for record in records:
        record_dict = {}
        for j in range(len(column_names)):
            record_dict[column_names[j]]=record[j]
        result.append(record_dict)

    conn.close()
    return result


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


