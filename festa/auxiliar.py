from models import Convidado


def atualiza_tabela():
    convidados = Convidado.query.all()
