from app import db


class Convidado(db.Model):
    __tablename__ = 'convidados'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), index=True, unique=True)
    acompanhante = db.Column(db.Integer)

    def __repr__(self):
        return f'<Convidado: {self.nome}>'
