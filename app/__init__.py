from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Inicializa a extensão do banco de dados 
db = SQLAlchemy()

def create_app():
    # Carrega as variáveis do arquivo .env
    load_dotenv()
    
    # Inicia o Flask dizendo que a pasta raiz de templates e static é a padrão
    app = Flask(__name__)
    
    # Puxa as configurações do .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Vincula o banco de dados
    db.init_app(app)

   # Contexto da aplicação
    with app.app_context():
        # Importa os modelos para o Flask reconhecer as tabelas
        from app import models 
        db.create_all() 
        
        # Importa e regista as rotas da interface web
        from app.routes.web_routes import web
        app.register_blueprint(web)
        
        # Importa e regista as rotas do bot do Telegram
        from app.routes.bot_routes import bot
        app.register_blueprint(bot)
        
    return app