from app import db


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.String(10), primary_key=True, unique=True)
    name = db.Column(db.String(40), nullable=False)
    email_id = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    cart_items = db.relationship('CartModel', back_populates='user', lazy="dynamic")
