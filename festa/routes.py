from models import convidado
from flask import render_template, redirect, url_for, flash, request
from festa import bp
from festa.forms import NovoConvidadoForm
from models import Convidado
from app import db


@bp.route('/')
def conv():
    form = NovoConvidadoForm()
    convidados = Convidado.query.all()
    return render_template('festa.html', convidados=convidados, 
                            title='Festa', form=form)


@bp.route('/', methods=['GET', 'POST'])
def create():
    form = NovoConvidadoForm()
    if form.validate_on_submit():
        convidado = Convidado(nome=form.nome.data, acompanhante=form.acomp.data)
        db.session.add(convidado)
        db.session.commit()
        return redirect(url_for('festa.conv'))
    return render_template('festa.html', title='Festa', form=form)

@bp.route('/<int:id>', methods=['GET', 'POST'])
def update(id):
    convidado = Convidado.query.get_or_404(id)
    form = NovoConvidadoForm(nome_original=convidado.nome)
    if form.validate_on_submit():
        convidado.nome = form.nome.data
        convidado.acompanhante = form.acomp.data
        db.session.add(convidado)
        db.session.commit()
        flash('Alteração salva com sucesso!!!')
        return redirect (url_for('festa.conv'))
    elif request.method == 'GET':
        convidado = Convidado.query.get(id)
        form.nome.data = convidado.nome
        form.acomp.data = convidado.acompanhante
        convidados = Convidado.query.all()
    return render_template('festa.html', convidados=convidados, 
                            form=form, title='Festa')


@bp.route('/<int:id>/delete')
def delete(id):
    convidado = Convidado.query.get_or_404(id)
    db.session.delete(convidado)
    db.session.commit()
    return redirect(url_for('festa.conv'))
