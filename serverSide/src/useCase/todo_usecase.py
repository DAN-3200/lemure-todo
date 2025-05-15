from src.server import ( 
   db, 
)
import datetime
from src.models.db_model import (cards)

def created(array):
   newCard = cards(array['title'], array['content'], array['favorited'])
   print("S", array['favorited'])
   db.session.add(newCard)
   db.session.commit()

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
   } for card in cards.query.all()]

def updated(id, array):
   print("input: ", array['validity'])
   setCard = cards.query.get(id)
   setCard.title = array['title']
   setCard.content = array['content']
   setCard.favorited = array['favorited']
   setCard.validity = datetime.datetime.strptime(array['validity'], '%Y-%m-%d')

   db.session.commit()

def deleted(id):
   trash = cards.query.get(id)

   db.session.delete(trash)
   db.session.commit()
