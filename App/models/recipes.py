from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class Recipe(db.Model):
  recipe_id = db.Column(db.Integer, primary_key=True)
  recipe_name =  db.Column(db.String(120), nullable=False)
  incrediants =  db.Column(db.String(256), nullable=False)
  recipe_pic = db.Column(db.String(120), nullable=False)
  
  def toDict(self):
        return{
            'recipe_id': self.recipe_id,
            'recipe_name': self.recipe_name,
            'incrediants': self.incrediants,
            'recipe_pic': self.recipe_pic
        }
