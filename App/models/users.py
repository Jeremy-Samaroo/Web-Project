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
