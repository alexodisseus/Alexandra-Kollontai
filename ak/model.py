from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# Instância do SQLAlchemy
db = SQLAlchemy()


# Definindo o modelo Lista
class Base_dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)  
    tag = db.Column(db.String(120)) 
    data_create = db.Column(db.Date, default=datetime.utcnow().date(), nullable=False)  
    active = db.Column(db.Boolean, default=True, nullable=True) 

    


def list_all_base():

    bases = Base_dados.query.all()
    return bases

