from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from controllers.routes import ToDoRoutes
from useCase.todo_usecase import ToDoUseCase
from db.connect_sql import db

def Server() -> Flask:
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    Config(app)

    api = Api(app, title='Py Smart-API', description='Um simples API em flask')
    # *comando de criar banco
    
    ToDoRoutes(ToDoUseCase(db),api)

    return app


def Config(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.app_context().push() # !analisar
    app.config['SECRET_KEY'] = 'ab44d789595b66efeda6b633e686a9db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
