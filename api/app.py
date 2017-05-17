#!flask/bin/python
from drivers import users
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/v1/users', methods=['GET'], strict_slashes=False)
def get_users():
    (status, data) = users.get_users()
    return jsonify(data), status


@app.route('/v1/users/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    (status, data) = users.get_user(user_id)
    return jsonify(data), status


@app.route('/v1/users', methods=['POST'], strict_slashes=False)
def new_user():
    (status, data) = users.new_user(request.json)
    return jsonify(data), status


if __name__ == '__main__':
    if os.environ['env'] == "dev":
        app.run(debug=True, host='0.0.0.0')
    elif os.environ['env'] == "prod":
        app.run(debug=False, host='0.0.0.0')
    else:
        print "'env' environment variable not set (should be [dev|prod])"
