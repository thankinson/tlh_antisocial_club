from application import db, login_manager
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(30), nullable=False)
    user_last_name = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(30), nullable=False, unique=True)
    passwd = db.Column(db.String(200), nullable=False)
    # phone_id = db.relationship('UserPhone', backref='users')
    # address_id = db.relationship('UserAddress', backref='users')

    def get_id(self):
        return (self.user_id)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# phone number model 
# class UserPhone(db.Model):
#     __tablename__ = 'user_phone'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
#     phone_id = db.Column('phone_id', db.Integer, db.ForeignKey('phonenumber.phone_id'))

# class Phonenumber(db.Model):
#     phone_id = db.Column(db.Integer, primary_key=True)
#     phone_number = db.Column(db.Integer, nullable=False)
#     user_id = db.relationship('UserPhone', backref='phonenumber')

# # Address model

# class UserAddress(db.Model):
#     __tablename__ = 'user_address'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
#     address_id = db.Column('address_id', db.Integer, db.ForeignKey('address.contact_id'))

# class Address(db.Model):
#     contact_id = db.Column(db.Integer, primary_key=True)
#     address_line_one = db.Column(db.String(30), nullable=False)
#     address_line_two = db.Column(db.String(30), nullable=False)
#     address_location = db.Column(db.String(30), nullable=False)
#     address_postcode = db.Column(db.String(30), nullable=False)
#     user_id = db.relationship('UserAddress', backref='address')




    
