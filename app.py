from flask import flask, render_template, redirect, url_for


from models import AdminModel, CustomerModel, ItemModel, InventoryModel, LocationModel, GarmentModel, OrderModel
app = Flask(__name__)


items = {
    "Shirt": {"price": 500},
    "Trouser": {"price": 800},
    "Senator": {"price": 2500}
}

@app.route("/")
def index():
    return "Welcome to Imperial Kleen"

@app.route("/register-customer", method=["GET", "POST"])
def register_customer():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        address = request.form["address"]
        new_customer = CustomerModel(full_name=full_name, email=email, phone_number=phone_number, address=address)
        new_customer.save()

order_items = []

@app.route("/cart", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        name = request.form["name"]
        qty = request.form["qty"]        

        global order_items.append({"name": name, "qty": qty, "cost": items[name][price] * qty })
    else:
        return render_template("cart.html", order_items=order_items)


@app.route("/create-order", methods=["GET", "POST"])
def create-order():
    global order_items
    if request.method == "POST":
        customer = request.form["customer"]
        item_ids = order_items
        amount_list = [i["price"] for i in order_items]
        amount = sum(amount_list)
    else:
        return render_template("create-order.html", order_items=order_items)

@app.route("/create-location", methods=["GET", "POST"])
def create_location():
    if request.method == "POST":
        name = request.form["name"]
        new_location = LocationModel(name=name)
        new_location.save()

    else:
        return render_template("add-location.html")
        
    pass

@app.route("/order/<string:order_id")
def order(order_id):
    pass

@app.route("/add-inventory")
def add_inventory():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        date_added = request.form["date_added"]
        quantity= request.form["quantity"]
        location = request.form["location"]

        new_inventory = InventoryModel(name=name, description=description, date_added=date_added, quatity=quantity, location=location)
        new_inventory.save()
    else:
        return render_template("add_inventory.html")

@app.route("/inventory/<string:inventory_id"):
def inventory(inventory_id):
    pass




if __name__ == '__main__':
    app.run(port=7000, debug=True)