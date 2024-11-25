from flask import Flask
from flask import Blueprint, render_template, request, session, redirect, url_for, flash

import model



painel = Blueprint('painel', __name__, url_prefix='/')



# Rota para exibir todas as listas (List)
@painel.route('/')
def index():
    data = model.list_all_base()
    print(data)
    #return render_template('painel/index.html' , data=data)
    return "<h1>bem vindo</h1><a href='criar/'>entrar</a>"

@painel.route('criar/')
def create():
    return "<h1>criar</h1><a href='/ver/'>ver</a>"

@painel.route('ver/')
def view():
    return "<h1>ver</h1><a href='/'>listar</a>"


# Função para configurar o blueprint
def configure(app):
    app.register_blueprint(painel)






