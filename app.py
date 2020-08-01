from flask_restful import *
from flask import *

class Test(Resource):
    def get(self):
        return {'message':'success'},200


app = Flask(__name__)
api = Api(app)
api.add_resource(Test, '/')
app.run(host='0.0.0.0', port=80)