#!/usr/bin/python3
from os import getenv
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from models import storage
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(error):
    '''Closes the connection to the database.'''
    storage.close()

@app.errorhandler(404)
def error_not_found(error):
    '''Method to define the status code.'''
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', '5000')), threaded=True)

