from models import ItemModel, db
from schemas import item_schema, items_schema

from flask_restful import Resource, request, abort
from sqlalchemy import exc
from psycopg2.errors import ForeignKeyViolation
from marshmallow import ValidationError


class ItemResource(Resource):
    
    def get(self, item_id: int):
        
        item = ItemModel.query.get_or_404(item_id)

        return item_schema.dump(item), 200

class ItemPostResouce(Resource):

    def post(self):
        
        try:
            item_data = item_schema.load(request.get_json())
        except ValidationError as e:
            abort(400, message=str(e))

        try:
            item = ItemModel(**item_data)

            db.session.add(item)
            db.session.commit()

        except exc.IntegrityError as e:
            abort(500, message=str(e))

        except exc.SQLAlchemyError as e:
            abort(500, message=str(e))

        except Exception as e:
            abort(500, message=str(e))

        return item_schema.dump(item), 201
    
class ItemListResource(Resource):
    
    def get(self):
        
        items = ItemModel.query.all()

        return items_schema.dump(items), 200