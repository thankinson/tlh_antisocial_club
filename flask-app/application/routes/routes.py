from application import app
from application.service.pages import SignUpPage, LoginPage, AccountPage, LogoutRoute

@app.route('/', methods=['GET', 'POST'])
def sign_up():
    return SignUpPage.sign_up_page()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return LoginPage.login_page()

@app.route('/account')
def account():
    return AccountPage.account_page()

@app.route('/logout')
def logout():
    return LogoutRoute.logout()
