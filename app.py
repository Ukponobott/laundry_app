from flask import flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Imperial Kleen"

@app.route("/register-customer")
def register_customer():
    pass

@app.route("/create-order")
def create_order():
    pass

@app.route("/order/<string:order_id")
def order(order_id):
    pass

@app.route("/add-inventory")
def add_inventory():
    pass

@app.route("/inventory/<string:inventory_id"):
def inventory(inventory_id):
    pass




if __name__ == '__main__':
    app.run(port=7000, debug=True)