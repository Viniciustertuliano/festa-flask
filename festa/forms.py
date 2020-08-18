from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Convidado


class NovoConvidadoForm(FlaskForm):

    nome = StringField('Nome do convidado',
                            validators=[DataRequired(), Length(min=3, max=50)])
    acomp = StringField('Número de acompanhantes')
    enviar = SubmitField('enviar')

    def __init__(self, nome_original=None, *args, **kwargs):
        super(NovoConvidadoForm, self).__init__(*args, **kwargs)
        self.nome_original = nome_original