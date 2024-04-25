from flask import Flask, render_template, request, session, redirect, url_for
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
    print(category_id)
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
  quantity = int(request.form['quantity'])
  product_id = int(request.form['product_id'])
  action = request.args.get('action')  # Access query parameter if present
  if(action == 'add'):
    status = db.add_to_cart(session['username'], product_id, quantity)
    if(status):
        return "Successful!"
    return "Failed to add  in cart."
  
  print(f"Adding {quantity} of product {product_id} to cart (action: {action})")
  return "Product added to cart (simulation)"

@app.route('/buy', methods=['POST'])
def buy_item():
  id = int(request.form['product_id'])
  qty = int(request.form['quantity'])
  print(id, qty)
  if db.buy_now(session['username'], id, qty):
    return "SUCCESSFUL!"
  return "Either you chose the qty greater than existing quantity or due to some internal error it fails."

@app.route('/cart')
def get_cart():
    cart = db.get_cart(session['username'])
    print(cart)
    total = sum([i["Price"] * i['Quantity'] for i  in cart])
    print(total)
    return render_template('cart.html', cart=cart, total_price=total)

@app.route('/checkout')
def checkout():
    # cart.clear()
    return "Checkout successful (simulation)"

@app.route('/call-for-trial')
def call_for_trial():
    db.call_for_trial(session["username"])
    return "Thank you for your interest! A representative will contact you soon (simulation)"

@app.route('/get-trial')
def get_trial():
    product_ids = db.get_trial_history(session['username'])
    print(product_ids)
    products = []
    for i in product_ids:

        temp = db.get_product(i)[0]
        print(temp)
        products.append(temp)
    print(products)
    return render_template('trial_history.html', trials=products)

@app.route('/get-order-history')
def get_order_history():
    orders = db.get_order_history(session['username'])
    return render_template('order_history.html', orders = orders)

@app.route('/delete-item', methods=['POST'])
def delete_item():
    item_id = int(request.form['item_id'])
    db.delete_item_from_cart(session['username'], item_id)
    return redirect(url_for('get_cart'))



if __name__ == '__main__':
  app.run(debug=True)