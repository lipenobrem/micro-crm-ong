from flask import Blueprint, render_template, redirect, url_for, request, session
from app import db
from app.models import Voluntario, Doacao
from sqlalchemy import func
import os

web = Blueprint('web', __name__)
SENHA_ADMIN = os.getenv("PAINEL_SENHA") 

@web.route('/')
def home():
    resultados = db.session.query(Doacao.tipo, func.count(Doacao.id)).group_by(Doacao.tipo).all()
    labels = [r[0] for r in resultados]
    valores = [r[1] for r in resultados]
    if not labels:
        labels = ['Financeira', 'Alimentos', 'Roupas']
        valores = [0, 0, 0]
        
    return render_template('cadastros.html', labels=labels, valores=valores)

@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form.get('senha')
        if senha == SENHA_ADMIN:
            session['logado'] = True
            return redirect(url_for('web.index'))
        else:
            return render_template('login.html', erro="Palavra-passe incorreta!")
    return render_template('login.html', erro=None)

@web.route('/logout')
def logout():
    session.pop('logado', None)
    return redirect(url_for('web.home'))

@web.route('/dashboard')
def index():
    if not session.get('logado'):
        return redirect(url_for('web.login'))
        
    lista_voluntarios = Voluntario.query.all()
    return render_template('dashboard.html', voluntarios=lista_voluntarios)

@web.route('/mudar_status/<int:id>', methods=['POST'])
def mudar_status(id):
    if not session.get('logado'):
        return redirect(url_for('web.login'))
        
    voluntario = Voluntario.query.get_or_404(id)
    if voluntario.status == 'Ativo':
        voluntario.status = 'Inativo'
    else:
        voluntario.status = 'Ativo'
        
    db.session.commit()
    return redirect(url_for('web.index'))