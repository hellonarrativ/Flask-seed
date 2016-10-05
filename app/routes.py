from flask import Blueprint

from views import HelloWorldView

router = Blueprint('api', __name__, url_prefix='/api/v0/')

router.add_url_rule('/', view_func=HelloWorldView.as_view('hello_world'), methods=['GET',])
