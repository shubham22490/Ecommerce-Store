from flask import Flask, render_template, request


app = Flask("Luxury Store")

# Database configuration (replace with your details)
MYSQL_HOST = 'localhost'
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'your_database_name'

# Connect to the database
conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
cursor = conn.cursor()

@app.route("/register", methods=['GET', 'POST'])
def register():
    if(request.method == 'GET'):
        return render_template(register.html)
    elif request.method == 'POSt':
        username = request.form['username']
        password = request.form['password']


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    # Display the login form (render the login.html template)
    return render_template('login.html')
  elif request.method == 'POST':
    # Handle form submission (validate credentials and handle login)
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    return username
    # Implement logic to validate username and password against your database
    # (hashed password comparison using Flask-bcrypt is recommended)
    # if validate_credentials(username, password):  # Replace with your validation logic
    #   # Login successful (redirect to a protected page or display success message)
    #   return "Login successful!"  # Replace with actual logic
    # else:
    #   # Login failed (display error message and potentially reload login form)
    #   return "Invalid username or password."  # Replace with user-friendly message


@app.route('/')
def home():
    categories = get_categories()
    return render_template('categories.html', categories=categories)


if __name__ == '__main__':
  app.run(debug=True)