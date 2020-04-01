from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    """
    """
    def get(self, name):
        """
        get name of student
        """
        return {'student':name}

# this replaces @app.route('xxx') under Student:get   
api.add_resource(Student,'/student/<string:name>') #http://localhost/student/Rolf

app.run(port=5000)




