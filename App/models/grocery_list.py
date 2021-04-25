from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class Grocery_List(db.Model):
  grocery_list_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'))
  recipe_name =  db.Column(db.String(120), nullable=False)
  incrediants =  db.Column(db.String(120), nullable=False)
  
  def toDict(self):
        return{
            'grocery_list_id': self.grocery_list_id,
            'user_id': self.user_id,
            'recipe_name': self.recipe_name,
            'incrediants': self.incrediants,
        }
