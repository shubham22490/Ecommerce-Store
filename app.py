from flask import Flask, render_template, request
import db

app = Flask("Luxury Store")

@app.route("/")
def initialize():
    return login()

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
    Implement logic to validate username and password against your database
    (hashed password comparison using Flask-bcrypt is recommended)
    if validate_login(username, password):  
      return "Login successful!"  # Replace with actual logic
    else:
      # Login failed (display error message and potentially reload login form)
      return "Invalid username or password."  # Replace with user-friendly message


@app.route('/')
def home():
    categories = get_categories()
    return render_template('categories.html', categories=categories)


if __name__ == '__main__':
  app.run(debug=True)