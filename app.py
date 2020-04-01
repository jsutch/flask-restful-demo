from flask import Flask, request
from flask_restful import Resource, Api

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
        for item in items:
            if item['name'] == name:
                return item
            else:
                return {'item':None}, 404 # setting return code value

    def post(self, name):
        # methods to quell errors
        #data = request.get_json(force=True) # don't look at header - coerce into json
        #data = request.get_json(silent=True)# 
        data = request.get_json()
        new_item = {
            'name' : name,
            'price' : data['price']
            }
        items.append(new_item)
        return new_item, 201 
    
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




