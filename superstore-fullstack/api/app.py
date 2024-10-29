from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@database:5432/test_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database
db = SQLAlchemy(app=app)

# JWT Authentication
jwt = JWTManager(app=app)

# API endpoints
api = Api(app=app)

from resources.store import Store, StoreList, StorePostResource
from resources.item import ItemResource, ItemListResource, ItemPostResouce
from resources.user import UserRegisterResource, UserCartItemsResource, UserCartAddItemResource
from resources.authentication import UserAuthenticationResource

api.add_resource(UserAuthenticationResource, '/authenticate/', methods=['POST'])

api.add_resource(Store, '/store/<int:store_id>')
api.add_resource(StoreList, '/store/stores')
api.add_resource(StorePostResource, '/store/add')

api.add_resource(ItemResource, '/item/<int:item_id>', methods=['GET', 'DELETE'])
api.add_resource(ItemListResource, '/item/items', methods=['GET'])
api.add_resource(ItemPostResouce, '/item/add', methods=['POST'])

api.add_resource(UserRegisterResource, '/user/register', methods=['POST'])
api.add_resource(UserCartItemsResource, '/user/<string:user_id>/cart', methods=['GET'])
api.add_resource(UserCartAddItemResource, '/user/add_item', methods=['POST'])


if __name__ == '__main__':

    app.run(debug=True, port=8000)