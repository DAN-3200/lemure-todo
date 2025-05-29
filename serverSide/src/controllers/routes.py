from flask_restx import ( 
    Resource,   
    Namespace,
    Api,
    fields,
)
from useCase.todo_usecase import ToDoUseCase

def ToDoRoutes(useCase: ToDoUseCase, api: Api):
    ns = Namespace('ToDoNotes', description='Restful ToDo Service')
    api.add_namespace(ns)

    requestModel = api.model('ToDo',{
        'title' : fields.String(description='Título'),
        'content' : fields.String(description='Conteúdo')
    })

    @ns.route('/ToDo')
    class systemOne(Resource):
        #@api.expect('') - estabelece um modelo de 'request'
        #@api.marshal_with('') - estabelece um modelo de 'response'

        def get(self):
            return useCase.readed()
        
        @ns.expect(requestModel)
        def post(self):
            return useCase.created(ns.payload)
    
    @ns.route('/ToDo/<int:id>')
    class systemTwo(Resource):	
        @ns.expect(requestModel)
        def put(self, id):
            useCase.updated(id, ns.payload)
            return f'put {id}', 
        
        def delete(self, id):
            useCase.deleted(id)
            return f'delete {id}'