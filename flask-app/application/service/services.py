from flask import redirect, url_for, request
from application import db, bcrypt
from application.models.models import Users #, Address, UserAddress, Phonenumber, UserPhone
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

    def logout():
        logout_user()
        return redirect(url_for('login'))


class Loginservice():
    def is_logged_in():
        if current_user.is_authenticated:
            return redirect(url_for('account'))
    
    def is_not_logged_in():
        if not current_user.is_authenticated:
            return redirect(url_for('sign_up'))

class DbQuery():
    def query_curent_user():
        return Users.query.filter_by(user_id=current_user.user_id).first()
    
    # def query_user_address():
    #     query = db.session.query(
    #         Users, UserAddress, Address
    #         ).filter(Users.user_id==current_user.user_id
    #         ).join(UserAddress,Users.address_id==UserAddress.user_id
    #         ).join(Address,UserAddress.address_id==Address.contact_id
    #         ).first()
    #     for user, useraddress, address in query:
    #         if user.address_id == useraddress.user_id and useraddress.address_id == address.user_id:
    #             return query
    #         else:
    #             return "No Data"
     