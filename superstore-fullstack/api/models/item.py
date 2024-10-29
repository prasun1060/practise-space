from app import db, app


class ItemModel(db.Model):

    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")

    carts = db.relationship("CartModel", back_populates="item")