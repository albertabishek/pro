from flask import render_template, Blueprint,redirect,url_for,flash
from ..forms import RegistrationForm,LoginForm
from New_Creation import bcrypt,db
from ..models import Registrationd,Logind
from flask_login import login_user,current_user,logout_user,login_required

main = Blueprint('main',__name__)


@main.route('/')
@main.route('/start_page')
def starting_page():
    return render_template('starting_page.html')


@main.route('/home')
@main.route('/home_page')
@login_required
def home_page():
    return render_template('home_page.html')

@main.route('/forms_page')
def forms_page():
    return render_template('forms_page.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
       return redirect(url_for('main.home_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Registrationd(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html',form=form)


 

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('main.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Registrationd.query.filter_by(email=form.email.data).first()
        if user.email == "albertadmin@gmail.com" and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash('Logined successfully','success')
            return redirect(url_for('main.forms_page'))
        elif user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            log = Logind(email= form.email.data )
            db.session.add(log)
            db.session.commit()
            flash('Logined successfully','success')
            return redirect(url_for('main.home_page'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')
         
    return render_template('login.html', form=form)



@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))


 