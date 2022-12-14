from flask import redirect, url_for, request
from application import db, bcrypt
from application.models.models import Users
from flask_login import login_user, current_user, logout_user, login_required

class SignUpLogin():
    def signup(newuser):
        if request.method == 'POST':
            hash_pw = bcrypt.generate_password_hash(newuser.passwd.data)
            print(newuser.passwd.data)
            user = Users(
                user_first_name = newuser.first_name.data,
                user_last_name = newuser.last_name.data,
                user_email = newuser.email.data,
                passwd = hash_pw
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    
    def login(loginform):
        user = Users.query.filter_by(user_email=loginform.email.data).first()
        if request.method == 'POST':
            if user and bcrypt.check_password_hash(user.passwd, loginform.passwd.data):
                print("Login service if hit")
                login_user(user)   
                return redirect(url_for('account'))

class Loginservice():
    def is_logged_in():
        if current_user.is_authenticated:
            return redirect(url_for('account'))