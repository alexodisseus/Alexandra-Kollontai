from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# Instância do SQLAlchemy
db = SQLAlchemy()


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

def get_id_base(id):
    # modificar para buscar po id
    data = Base_dados.query.all()
    return data


def create_new_base(nome , description , tag , active):
    
    novo_item = Base_dados(
        nome=nome,
        description=description,
        tag=tag,
        active=active,
        data_create=datetime.utcnow().date()  # O campo `data_create` será gerado automaticamente pelo modelo
    )

    # Adicionando ao banco de dados
    db.session.add(novo_item)
    db.session.commit()
