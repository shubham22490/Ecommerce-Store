import pymysql
from datetime import datetime
from fastapi import FASTAPI
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'mydb'
app = FastAPI()
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
@app.get("/show_product/{product_id}") 
def get_product(product_id: int) -> dict:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    table_name='product'
    my_cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_names = my_cursor.fetchall()
    column_names = [col[0] for col in column_names]
    query = "SELECT * FROM Product WHERE ID = %s"  # Use parameterized query to avoid SQL injection
    my_cursor.execute(query, (product_id,)) 
    record=my_cursor.fetchall()
    l=[]
    for i in record:
        d={}
        for j in range(len(column_names)):
            d[column_names[j]]=i[j]
        l.append(d)
    conn.close()
    return l

@app.get("/user_detail/{username}")
def get_user_details(username: str) -> dict:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    my_cursor.execute("SELECT * FROM customer WHERE PHONE_NUMBER=%s",(username,))
    record=my_cursor.fetchall()
    print(record)
    table_name='customer'

    my_cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_names = my_cursor.fetchall()
    column_names = [col[0] for col in column_names]
    d={}
    print(column_names)
    for  i in record:
        for j in range(len(column_names)):
            
            d[column_names[j]]=i[j]
    return d
@app.get("/show_cart/{username}")
def get_cart(username: str) -> list[dict]:
    my_cursor=conn.cursor()
    table_name = 'cart'  
    my_cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_names = my_cursor.fetchall()
    column_names = [col[0] for col in column_names]
    my_cursor.execute("SELECT * FROM customer WHERE Phone_Number=%s", (username,))

    record=my_cursor.fetchall()
    cart_id=-1
    for i in record:
    
        cart_id=i[9]
    if cart_id==-1:
        return [-1]
    my_cursor.execute("SELECT * FROM cart")
    record_=my_cursor.fetchall()
    l=[]
    for i in record_:
        if (i[1]==cart_id):
            d={}
            d[column_names[0]]=i[0]
            d[column_names[2]]=i[2]
            l.append(d)
    conn.close()
    return l

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

@app.get("/login")
def validate_login(username: str, password: str) -> bool:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    my_cursor.execute("SELECT * FROM Customer")
    record=my_cursor.fetchall()
    for i in record:
        if (i[0]==username):
            if (i[1]==password):
                return True
    return False
def calculate_age(date_of_birth):
    today = datetime.today()
    dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
    
@app.post("/signup_user")
def register_user(data: dict) -> bool:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    my_cursor.execute("SELECT * FROM customer")
    record=my_cursor.fetchall()
    for i in record:
        if (i[0]==data['Phone Number']):
            return False
    age=calculate_age(data["DOB"])
    query="INSERT INTO `mydb`.`Customer` (`Phone Number`,`User Password`,`Email`, `Sex`, `DOB`, `Name`, `Subscription_ID`, `Age`,`Cart_quantity`, `Cart_Id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(data['phone_number'],data['password'],data['email'],data['sex'],data['DOB'],data['Name'],data['subscription_id'],age,data['cart_quantity'],data['cart_id'])
    my_cursor.execute(query,values)
    my_cursor.commit()
    conn.close()
    return True



