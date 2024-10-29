from models.store import StoreModel
from models.item import ItemModel
from models.user import UserModel
from models.cart import CartModel
from app import app, db

with app.app_context():
    db.create_all()