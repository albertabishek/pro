from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_login import UserMixin,LoginManager


 

db = SQLAlchemy()
login_manager = LoginManager()
 


@login_manager.user_loader
def load_user(user_id):
    return Registrationd.query.get(int(user_id)) 

#Database for food table

class Foods(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    category_1 = db.Column(db.String(length=30), nullable=False) #for veg or non-veg and everything
    link = db.Column(db.String(length=200), nullable=False, unique=True)
    filename = db.Column(db.String(100), nullable=False)

    

class Food_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False )
    F_tag = db.Column(db.String(length=50), nullable=False )  #for food name
    P_tag = db.Column(db.String(length=50), nullable=False )  #for location name
    D_tag = db.Column(db.String(length=50), nullable=False )  
    price = db.Column(db.Integer(), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(100), nullable=False )


class Food_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    details = db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)
   






#Database for Shoe table

class Shoe(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    category_1 = db.Column(db.String(length=30), nullable=False) 
    link = db.Column(db.String(length=200), nullable=False, unique=True)
    filename = db.Column(db.String(30), nullable=False)

class Shoe_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False )
    S_tag = db.Column(db.String(length=50), nullable=False )   
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False )
    price = db.Column(db.Integer(), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class Shoe_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    details = db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)


#Database for Haircut table



class Haircut_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False )   
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class Haircut_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    details = db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)










#Database for login system
 

class Registrationd(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False)
    email = db.Column(db.String(length=50),nullable=False)
    password = db.Column(db.String(length=30), nullable=False)

    def __repr__(self):
        return f"Registrationd('{self.username}', '{self.email}')"

class Logind(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(length=50), nullable=False)
    date_logged = db.Column(db.DateTime, nullable=False, default=datetime.now)