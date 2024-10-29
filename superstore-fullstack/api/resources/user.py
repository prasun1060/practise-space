from models import UserModel, CartModel, db
from schemas import user_schema, cart_item_schema, user_cart_schema

from flask_restful import Resource, request, abort
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity


class UserResource(Resource):

    def post(self):

        user_data = user_schema.load(request.get_json())

        try:  
            user = UserModel(**user_data)
            user.password = generate_password_hash(user.password)
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return user_schema.dump(user), 201
    
    @jwt_required()
    def get(self):

        user_id = get_jwt_identity()

        user = UserModel.query.get(user_id)
        if user:

            return user_cart_schema.dump(user), 200

        else:

            abort(404, message="User not found")

    @jwt_required()
    def delete(self):

        user_id = get_jwt_identity()

        user = UserModel.query.get(user_id)
        if user:
            
            db.session.delete(user)
            db.session.commit()

            return {"message": "User successfully deleted"}, 200

        else:

            abort(404, message="User not found")
    
class UserCartAddItemResource(Resource):

    @jwt_required()
    def post(self):

        user_id = get_jwt_identity()
        cart_item_data = cart_item_schema.load(request.get_json())

        cart = CartModel(**cart_item_data, user_id=user_id)

        db.session.add(cart)
        db.session.commit()
        
        return cart_item_schema.dump(cart), 201