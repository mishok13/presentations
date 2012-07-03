from flask import Blueprint

API = Blueprint(
    'API', __name__, url_prefix='/api/v1')

@API.route('/foo')
def foo():
    ...
