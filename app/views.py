from flask import jsonify
from flask.views import MethodView


class HelloWorldView(MethodView):
    def get(self):
        return jsonify(data="Hello, World!")
