from flask import Flask
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
        return {'item':name}

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
        item = { 'name': name, 'price': 12.99 }
        items.append(item)
        return item, 201 
    
    def put(self, name):
        pass

    def delete(self, name):
        pass

# this replaces @app.route('xxx') under Student:get   
# Test
#api.add_resource(Test,'/item/<string:name>') 
# Item API targets
api.add_resource(Item,'/item/<string:name>') # e.g. http://localhost/item/mittens


app.run(port=5000)




