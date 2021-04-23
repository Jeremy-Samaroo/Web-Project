from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(120),unique=True, nullable=False)
    email =  db.Column(db.String(120),unique=True, nullable=False)
    password =  db.Column(db.String(120), nullable=False)
    grocery_list = db.relationship('Grocery_List', backref='user', lazy=True)

    def toDict(self):
        return{
            'id': self.user_id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    def set_password(self,password):
      self.password=generate_password_hash(password,method='sha256')
    
    def check_password(self,password):
      return check_password_hash(self.password,password)

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
