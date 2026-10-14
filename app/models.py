from app import db
from datetime import datetime

class Voluntario(db.Model):
    __tablename__ = 'voluntarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    telegram_id = db.Column(db.String(50), unique=True, nullable=True)
    disponibilidade = db.Column(db.String(200), nullable=True)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    status = db.Column(db.String(20), default='Ativo')

    def __repr__(self):
        return f'<Voluntario {self.nome}>'


class Doacao(db.Model):
    __tablename__ = 'doacoes'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=True)     
    descricao = db.Column(db.String(200), nullable=True)
    data_doacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Doacao {self.tipo} - ID {self.id}>'