from flask import Flask, render_template, request, session
import db

app = Flask("Luxury Store")
app.secret_key = 'test'

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
    if db.validate_login(username, password):
        session['username'] = username
        return home()
    else:
      return "Invalid username or password."


@app.route('/home')
def home():
    categories = db.get_categories()
    print(categories)
    return render_template('categories.html', categories=categories)

@app.route('/category/<int:category_id>')
def show_category_products(category_id):
    products = db.get_products(category_id)
    print(products)
    return render_template('products.html', products = products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
  product = db.get_product(product_id)
  print(product)
  if (len(product) == 0):
    return "Product not found!", 404
  return render_template('product.html', product=product[0])

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
  # Implement logic to add product to cart based on quantity and action parameter
  # This example just prints the submitted data for demonstration
  quantity = request.form['quantity']
  product_id = int(request.form['product_id'])
  action = request.args.get('action')  # Access query parameter if present
  if(action == 'add'):
    status = db.add_to_cart(session['username'], product_id, quantity)
    if(status):
        return "Successful!"
    return "Failed to add  in cart."
  
  print(f"Adding {quantity} of product {product_id} to cart (action: {action})")
  return "Product added to cart (simulation)"

@app.route('/cart')
def get_cart():
    return db.get_cart(session['username'])






if __name__ == '__main__':
  app.run(debug=True)