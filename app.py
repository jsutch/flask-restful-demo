from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
api = Api(app)

# datastore
items = []

class Test(Resource):
    """
    test harness. return whatever name passed
    """
    def get(self, name):
        return {'test':name}

class Item(Resource):
    """
    Main Item Class
    Flask-RESTful does not need jsonify for returns
    """
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #next() returns only the first item from filter(lambda)
        # return {'item': item}, 200 if item is not None else 404
        return {'item': item}, 200 if item else 404 #shortened version

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {
            'name' : name,
            'price' : data['price']
            }
        items.append(item)
        return item, 201 
    
    def put(self, name):
        pass

    def delete(self, name):
        pass

class ItemList(Resource):
    def get(self):
        return {'items': items}

# Adding resources:
# api.add_resource(xxx) replaces @app.route('xxx') under Student:get   
# Raw API Tester
api.add_resource(Test,'/test/<string:name>') 
# Application API targets
api.add_resource(Item,'/item/<string:name>') # e.g. http://localhost/item/mittens
api.add_resource(ItemList, '/items')

# Debug
app.run(port=5000, debug=True)
# Regular
#app.run(port=5000)




