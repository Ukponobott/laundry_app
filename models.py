from mongoengine import *
connect('laundry-app')

from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

from utils import get_random_string


class AdminModel(Document):

    full_name = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50)
    phone_number = StringField(required=True, max_length=50)
    confirmed = StringField(required=True, default="False")
    password_hash = StringField(max_length=120)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class CustomerModel(Document):
    
    full_name = StringField(required=True, max_length=50)
    email = StringField(required=True, max_length=50)
    phone_number = StringField(required=True, max_length=50)
    address = StringField(max_length=120)
    city = StringField(max_length=50)
    state = StringField(max_length=50)

cus = CustomerModel(full_name="Ukpono", email="ukpono@gmail.com", phone_number="08054494334")
cus.save()

class ItemModel(Document):

    name = StringField(required=True, max_length=50)
    price = FloatField(required=True)


class LocationModel(Document):

    name = StringField(required=True, max_length=50)

loc = LocationModel(name="NigCBA1")
loc.save()


class InventoryModel(Document):

    name = StringField(required=True, max_length=50)
    description = StringField(required=True, max_length=50)
    date_added = DateTimeField(default=datetime.today())
    quantity = IntField(required=True)
    location = ReferenceField(LocationModel)

b = InventoryModel(name="Starch", description="Cold Water", quantity=100)

b.save()
b.location = loc
b.save()


class OrderModel(Document):
    
    customer = ReferenceField(CustomerModel)
    item_ids = ListField(DictField(required=True))
    amount = IntField()
    status = StringField(required=True, max_length=50)
    date_created = DateTimeField(default=datetime.today())
    date_updated = DateTimeField(default=datetime.today())
    created_by = ReferenceField(AdminModel)
    order_id = StringField(required=True, max_length=50, default=get_random_string(6))


order = OrderModel(item_ids=[{"item": "Shirt", "qty": 2, "price": 400.90}], status="Pending")
order.save()

order.customer = cus
order.save()
print(order.id)
print(order.order_id)


class GarmentModel(Document):
    order = ReferenceField(OrderModel)
    location = ReferenceField(LocationModel)
    tracking_id = StringField(required=True, max_length=50, default=get_random_string(8))

gar1 = GarmentModel(order=order, location=loc)

gar1.save()





    # def set_amount(self) -> int:
    #     self.amount = int(self.quantity * (self.item.price))


# a = LocationModel(id_="wudbyf", name="Ukpono")

# a.save()
a = ItemModel( name="Soap", price=56.90)

a.save()
    