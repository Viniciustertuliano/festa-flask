from flask import Blueprint, render_template

festa = Blueprint('festa', __name__, url_prefix='/convidados',
                  template_folder='templates')


@festa.route('/')
def conv():
    return render_template('festa.html')
