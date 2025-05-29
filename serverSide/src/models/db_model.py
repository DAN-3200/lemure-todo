from db.connect_sql import db
import datetime

class newToDo(db.Model):
    __tablename__ = 'ToDo'

    id = db.Column(db.Integer, primary_key=True, nullable=True)
    title = db.Column(db.String(50), nullable=True)
    content = db.Column(db.String(50), nullable=True)
    favorited = db.Column(db.Boolean, nullable=True)
    date = db.Column(db.Date, nullable=True)
    validity = db.Column(db.Date, nullable=True)

    def __init__(self, title, content, favorited):
        self.title = title
        self.content = content
        self.favorited = favorited
        self.date = datetime.datetime.now()
        self.validity = datetime.datetime.now()
    
    def __str__(self):
        return f"Card{self.id}"
    
    # *validação de campos