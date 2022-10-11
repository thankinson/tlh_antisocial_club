from flask import render_template, redirect, url_for
from application.forms.forms import SignUpForm, LoginForm
from application.service.services import SignUpLogin, DbQuery
from flask_login import current_user

class SignUpPage():
    def sign_up_page():
        if current_user.is_authenticated:
            return redirect(url_for('account'))
        newuser = SignUpForm()
        if newuser.validate_on_submit():
            return SignUpLogin.signup(newuser=newuser)
        return render_template('sign_up.html', form=newuser)

class LoginPage():
    def login_page():
        if current_user.is_authenticated:
            return redirect(url_for('account'))
        loginform = LoginForm()
        if loginform.validate_on_submit():
            return SignUpLogin.login(loginform=loginform)
        return render_template('login.html', form=loginform)

class AccountPage():
    def account_page():
        if not current_user.is_authenticated:
            return redirect(url_for('sign_up'))
        user = DbQuery.query_curent_user()
        return render_template('account.html', user=user)

class LogoutRoute():
    def logout():
        return SignUpLogin.logout()