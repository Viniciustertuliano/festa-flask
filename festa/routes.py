from flask import render_template, redirect, url_for, flash, request
#from flask_login import login_required
from festa import bp
from festa.forms import NovoConvidadoForm
from models import Convidado
from app import db


@bp.route('/')
def conv():
    convidados = Convidado.query.all()
    return render_template('festa.html', convidados=convidados)


@bp.route('/new', methods=['GET', 'POST'])
def create():
    form = NovoConvidadoForm()
    if form.validate_on_submit():
        convidado = Convidado(nome=form.nome.data, acompanhante=form.acomp.data)
        db.session.add(convidado)
        db.session.commit()
        return redirect(url_for('festa.conv'))
    return render_template('novoconv.html', title='Novo Convidado', form=form)
