from flask import render_template
from application.forms.forms import SignUpForm, LoginForm
from application.service.services import SignUpLogin

class SignUpPage():
    def sign_up_page():
        newuser = SignUpForm()
        if newuser.validate_on_submit():
            return SignUpLogin.signup(newuser=newuser)
        return render_template('sign_up.html', form=newuser)

class LoginPage():
    def login_page():
        loginform = LoginForm()
        if loginform.validate_on_submit():
            return SignUpLogin.login(loginform=loginform)
        return render_template('login.html', form=loginform)

class AccountPage():
    def account_page():
        return render_template('account.html')
