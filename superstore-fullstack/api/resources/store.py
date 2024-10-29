from models import StoreModel, db
from schemas import store_schema, stores_schema, plain_store_schema

from flask_restful import Resource, request, abort
from sqlalchemy import exc
from marshmallow import ValidationError


class Store(Resource):

    def get(self, store_id: int):

        store = StoreModel.query.get_or_404(store_id)
        return store_schema.dump(store), 200
    
    def delete(self, store_id: int):

        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()

        return {"message": "store deleted successfully"}, 200

class StorePostResource(Resource):

    def post(self):

        try:
            store_data = plain_store_schema.load(request.get_json())
        except ValidationError as e:
            abort(400, message=str(e))

        try:
            store = StoreModel(**store_data)

            db.session.add(store)
            db.session.commit()
        except exc.IntegrityError as e:

            abort(500, message=str(e))

        return plain_store_schema.dump(store), 201
     
class StoreList(Resource):

    def get(self):

        stores = StoreModel.query.all()
        return stores_schema.dump(stores), 200