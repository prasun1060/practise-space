from app import db


class CartModel(db.Model):

    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), unique=False, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), unique=False, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    item = db.relationship('ItemModel', back_populates='carts')
    user = db.relationship('UserModel', back_populates='cart_items')