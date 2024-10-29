from models import UserModel, db
from schemas import user_schema, user_authentication_schema

from flask_restful import Resource, request, abort
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


class UserAuthenticationResource(Resource):

    def post(self):

        user_data = user_authentication_schema.load(request.get_json())

        user = UserModel.query.get(user_data["id"])

        if user and check_password_hash(user.password, user_data["password"]):
            access_token = create_access_token(user_data["id"])
            return {"access_token": access_token}, 201
        
        return abort(401, message="Invalid credentials")