from flask import render_template
from auth import bp


@bp.route('/')
def index():
    return render_template('index.html',)
