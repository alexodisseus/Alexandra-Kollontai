from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# Instância do SQLAlchemy
db = SQLAlchemy()


# Definindo o modelo Lista
class Painel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)  
    tag = db.Column(db.String(120)) 
    data_create = db.Column(db.Date, default=datetime.utcnow().date(), nullable=False)  
    active = db.Column(db.Boolean, default=True, nullable=True) 

    


def get_all_painel():
    """
    Função para listar todas as listas no banco de dados.
    :return: Lista de objetos Lista.
    """
    # Recupera todas as listas ordenadas pelo campo 'data_create' (se quiser ordenar de forma diferente, altere aqui)
    listas = Lista.query.filter(Lista.active.isnot(False)).all()
    return listas

