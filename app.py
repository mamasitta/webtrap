import logging

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resource.any_request import AnyRequest


app = Flask(__name__)

# cors
CORS(app)

# logs will be saved in file webtrap.log
logging.basicConfig(filename='webtrap.log', level=logging.DEBUG)

# APIs
api = Api(app)
api.add_resource(AnyRequest, '/api')

if __name__ == '__main__':
    app.run(debug=True)
