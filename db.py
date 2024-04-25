import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'test'
MYSQL_DB = 'mydb'

def get_categories() -> list[dict]:
    conn = mysql.connector.connect(host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
    my_cursor = conn.cursor()

    # Fetch column names for the product_category table
    table_name = 'Product_Category'  
    my_cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_names = my_cursor.fetchall()
    column_names = [col[0] for col in column_names]
    # Fetch records from the product_category table
    my_cursor.execute(f"SELECT * FROM {table_name}")
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
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    table_name = "Product"
    my_cursor.execute(f"SELECT * FROM {table_name}")
    records=my_cursor.fetchall()
    my_cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_names = my_cursor.fetchall()
    column_names = [col[0] for col in column_names]
    l=[]
    if (category_id==0):
        for i in records:
            d={}
            for j in range(len(column_names)):
                d[column_names[j]]=i[j]
            l.append(d)
    else:
        for i in records:
            if (i[6]==category_id):
                d={}
                for j in range(len(column_names)):
                    d[column_names[j]]=i[j]
                l.append(d)
    return l


def get_product(product_id: int) -> dict:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    table_name='Product'
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


def get_cart(username: str) -> list[dict]:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    table_name = 'Cart'
    my_cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_names = my_cursor.fetchall()
    column_names = [col[0] for col in column_names]
    my_cursor.execute("SELECT * FROM Cart WHERE Phone_Number=%s", (username,))
    record_=my_cursor.fetchall()
    l=[]
    for i in record_:
        my_cursor.execute(f"SELECT Name, Price FROM Product WHERE Product.ID={i[3]}")
        data = my_cursor.fetchall()[0]
        name = data[0]
        price = data[1]
        d={}
        d["product_id"]=i[3]
        d["Name"] = name
        d['Quantity']=i[2]
        d['Price'] = price
        l.append(d)
    conn.close()
    return l

def add_to_cart(username: str, product_id: int,quantity:int) -> bool:
    
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    print(username)
    my_cursor.execute("SELECT * FROM Cart WHERE Phone_Number=%s",(username,))
    records=my_cursor.fetchall()
    for i in records:
        if (i[3] == product_id):
            my_cursor.execute("UPDATE Cart SET Quantity=Quantity+%s Where Product_ID=%s",(quantity,product_id,))
            return True
            
    query="INSERT INTO Cart(`Phone_Number`,`Quantity`,`Product_ID`) VALUES (%s,%s,%s)"
    values=(username, quantity, product_id)
    my_cursor.execute(query,values)
    conn.commit()
    conn.close()

    return True

def call_for_trial(username: str) -> bool:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    my_cursor.execute("SELECT * FROM Cart WHERE Phone_Number=%s",(username,))
    records=my_cursor.fetchall()
    for i in records:
        query="INSERT INTO trial_history(`PHONE_NUMBER`,`Product_Id`) VALUES (%s,%s)"
        values=(username,i[3])
        my_cursor.execute(query,values)
        conn.commit()
    return True

def get_trial_history(username: str) -> list[dict]:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    my_cursor.execute("SELECT * FROM trial_history WHERE Phone_Number=%s",(username,))
    record=my_cursor.fetchall()
    l=[]
    for i in record:
        l.append(i[2])
    conn.close()    
    return l

def search_product(prompt: str) -> list[dict]:
    return

def get_order_history(username: str) -> list[dict]:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    query = "SELECT * FROM order_history WHERE PHONE_NUMBER = %s"
    my_cursor.execute(query, (username,))
    order_history = my_cursor.fetchall()
    resp=[]
    for i in order_history:
        my_cursor.execute("SELECT Name FROM Product WHERE ID=%s",(i[2],))
        name=my_cursor.fetchall()[0][0]
        d = {}
        d['name'] = name
        d['qty'] = i[3]
        resp.append(d)


    my_cursor.close()
    conn.close()
    
    return resp

def checkout(username: str) -> str or list[str]:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    my_cursor.execute("SELECT * FROM Cart WHERE Phone_Number=%s",(username,))
    records = my_cursor.fetchall()
    flag = True
    items = []
    for i in records:
        my_cursor.execute("SELECT Quantity, Name FROM Product WHERE ID=%s", (i[3],))
        data = my_cursor.fetchall()[0]
        available = data[0]; name = data[1]
        if(available < i[2]):
            items.append([name, available])
            flag = False

    if(flag):
        resp = ""
        try:
            for i in records:
                query="INSERT INTO order_history(`Phone_Number`,`Product_ID`, `Quantity`) VALUES (%s,%s,%s)"
                values=(i[1], i[3], i[2])
                my_cursor.execute(query,values)
            resp = "SUCCESSFUL!!!"
            my_cursor.execute("DELETE FROM Cart WHERE Phone_Number=%s", (username,))
            print("Deleted from Cart for user:", username)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_SIGNAL_EXCEPTION:
                resp = "Error: Insufficient Stocks for the requested product."
            else:
                resp = "Internal SQL Error"
        finally:
            conn.commit()
            conn.close()
        return resp
    conn.commit()
    conn.close()
    return items


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
    

def register_user(data: dict) -> bool:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    my_cursor.execute("SELECT * FROM customer")
    record=my_cursor.fetchall()
    for i in record:
        if (i[0]==data['Phone Number']):
            return False
    age=calculate_age(data["DOB"])
    query="INSERT INTO `mydb`.`Customer` (`Phone Number`,`User Password`,`Email`, `Sex`, `DOB`, `Name`) VALUES (%s,%s,%s,%s,%s,%s)"
    values=(data['phone_number'],data['password'],data['email'],data['sex'],data['DOB'],data['Name'])
    my_cursor.execute(query,values)
    conn.commit()
    conn.close()
    return True

def delete_item_from_cart(username, product_id):
    # Establish a database connection
    conn = mysql.connector.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
    cursor = conn.cursor()

    # try:
        # SQL statement to delete the specific item from the cart
    query = "DELETE FROM Cart WHERE Phone_Number = %s AND Product_ID = %s"
    values = (username, product_id)

    # Execute the query
    cursor.execute(query, values)

    # Commit the changes to the database
    conn.commit()

    cursor.execute("SELECT * FROM Cart Where Phone_Number = %s", (username, ))
    print(cursor.fetchall())
    
    return True


def buy_now(username:str, product:int, qty: int) -> bool:
    conn=mysql.connector.connect(host=MYSQL_HOST,username=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DB)
    my_cursor=conn.cursor()
    query="INSERT INTO order_history(`Phone_Number`,`Product_ID`, `Quantity`) VALUES (%s,%s,%s)"
    values=(username, product, qty)
    result = ""
    try:
        my_cursor.execute(query,values)
        result = "SUCCESSFUL!!!"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_SIGNAL_EXCEPTION:
            result = "Error: Insufficient Stocks for the requested product."
        else:
            result = "Internal SQL Error"
    finally:
        conn.commit()
        conn.close()
    return result



