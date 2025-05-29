import datetime
from src.models.db_model import (newToDo)

class ToDoUseCase():
   def __init__(self,db):
      self.db = db

   def created(self,array):
      newCard = newToDo(array['title'], array['content'], array['favorited'])
      print("S", array['favorited'])
      self.db.session.add(newCard)
      self.db.session.commit()

      return {
         'id': newCard.id,
         'title' : newCard.title,
         'content': newCard.content,
         'date': newCard.date.strftime('%Y-%m-%d'),
         'favorited': newCard.favorited,
         'validity': newCard.date.strftime("%Y-%m-%d"),
      }

   def readed():
      # compreensão de lista -> [expressão for item in lista]
      return [{
         'id': card.id,
         'title': card.title,
         'content': card.content,
         'date': card.date.strftime("%Y-%m-%d"),
         'favorited': card.favorited,
         'validity': card.validity.strftime("%Y-%m-%d"),
      } for card in newToDo.query.all()]

   def updated(self, id, array):
      print("input: ", array['validity'])
      setCard = newToDo.query.get(id)
      setCard.title = array['title']
      setCard.content = array['content']
      setCard.favorited = array['favorited']
      setCard.validity = datetime.datetime.strptime(array['validity'], '%Y-%m-%d')

      self.db.session.commit()

   def deleted(self,id):
      trash = newToDo.query.get(id)

      self.db.session.delete(trash)
      self.db.session.commit()
