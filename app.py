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
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']



@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  elif request.method == 'POST':
    # Handle form submission (validate credentials and handle login)
    username = request.form['username']
    password = request.form['password']
    if validate_login(username, password):  
      return home()
    else:
      return "Invalid username or password."


@app.route('/home')
def home():
    categories = get_categories()
    print(categories)
    return render_template('categories.html', categories=categories)




if __name__ == '__main__':
  app.run(debug=True)