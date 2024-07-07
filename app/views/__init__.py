from flask import Blueprint

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)
admin = Blueprint('admin', __name__)
cms = Blueprint('cms', __name__)
api = Blueprint('api', __name__)

