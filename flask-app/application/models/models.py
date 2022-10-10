from application import db, login_manager
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(30), nullable=False)
    user_last_name = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(30), nullable=False, unique=True)
    passwd = db.Column(db.String(200), nullable=False)

    def get_id(self):
        return (self.user_id)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))