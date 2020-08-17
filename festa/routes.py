from flask import render_template
from festa import bp
# from festa.auxiliar import atualiza_tabela
from models import Convidado
# from app import db


@bp.route('/')
def conv():
    convidados = Convidado.query.all()
    return render_template('festa.html', convidados=convidados)
