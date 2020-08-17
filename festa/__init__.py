from flask import Blueprint

bp = Blueprint('festa', __name__, template_folder='templates')

from festa import routes
