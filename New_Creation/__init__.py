from flask import Flask
from flask_bcrypt import Bcrypt
 
from  .models import db ,login_manager
from .forms import RegistrationForm,LoginForm
 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '86dbba64fcc01c47427a65d4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)
 
 
app.app_context().push()
 



with app.app_context():
    db.create_all()

login_manager.init_app(app)
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'




from New_Creation.Food_details.routes import Food_details
from New_Creation.Shoe_details.routes import Shoe_details
from New_Creation.main.routes import main
from New_Creation.Haircut_details.routes import Haircut_details


app.register_blueprint(Food_details)
app.register_blueprint(Shoe_details)
app.register_blueprint(main)
app.register_blueprint(Haircut_details)

 
 
 