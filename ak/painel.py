from flask import Flask
from flask import Blueprint, render_template, request, session, redirect, url_for, flash

import model



painel = Blueprint('painel', __name__, url_prefix='/')



# Rota para exibir todas as listas (List)
@painel.route('/')
def index():
    data = model.list_all_base()
    print(data)
    return render_template('painel/index.html' , data=data)
    return "<h1>bem vindo</h1><a href='criar/'>entrar</a>"


@painel.route('criar/' , methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        description = request.form['description']
        tag = request.form.get('tag')  # 'tag' pode ser opcional
        active = request.form.get('active') == 'on'  # Converte o checkbox para booleano

        data = model.create_new_base(nome , description , tag , active)
        
        if data:
            return redirect(url_for('painel.index'))  # Ajuste para o caminho correto após criar o item

    return render_template('painel/create.html' )
    
    return "<h1>criar</h1><a href='/ver/'>ver</a>"




@painel.route('ver/<int:id>')
def view(id):
    
    return render_template('painel/create.html' )

    return "<h1>ver</h1><a href='/'>listar</a>"




@painel.route('editar/<int:id>')
def update(id):
    data = model.list_all_base()
    
    return render_template('painel/update.html',data=data )

    return "<h1>ver</h1><a href='/'>listar</a>"



@painel.route('deletar/<int:id>')
def delete(id):
    pass

# Função para configurar o blueprint
def configure(app):
    app.register_blueprint(painel)



