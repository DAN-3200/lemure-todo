from flask import (
    jsonify, # formatar em JSON
)
from flask_restx import ( # Suporte para criação de APIs RESTful
    Resource,   
    Namespace
)
from src.server import ( 
    api, # raiz da API RESTful
)

from src.models.request_model import (modelCard)
from useCase.todo_usecase import (
    created, readed, updated, deleted
)

ns = Namespace('toDo', description='CRUD')
api.add_namespace(ns)


# -------------------------------------------
def Routers():
    @ns.route('/cards')
    class systemOne(Resource):
        #@api.expect('') - estabelece um modelo de entradada
        #@api.marshal_with('') - estabelece um modelo de retorno

        def get(self):
            return readed()
        
        @ns.expect(modelCard)
        def post(self):
            return created(ns.payload)
    
    @ns.route('/cards/<int:id>')
    class systemTwo(Resource):	
        @ns.expect(modelCard)
        def put(self, id):
            updated(id, ns.payload)
            return f'put {id}', 
        
        def delete(self, id):
            deleted(id)
            return f'delete {id}'