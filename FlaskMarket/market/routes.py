from FlaskMarket.market.forms import LoginForm
from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
@app.route("/")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all() #calling items stored in db

    return render_template('market.html', items = items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():   
        user_to_create = User(username=form.username.data,
        email_adress =form.email_adress.data,
        password=form.password1.data)
        db.session.add(user_to_create)  
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #if there are is errors from the validarions (it returns empty dict if no errors)
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form = form) 

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()

    return render_template('login.html', form = form)



