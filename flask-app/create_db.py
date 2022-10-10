from application import db, bcrypt
from application.models.models import Users


# default password for all suers is password

db.drop_all()
db.create_all()
hash_pw = bcrypt.generate_password_hash('password')
add = Users(
    user_first_name = "James",
    user_last_name = "Kirk",
    user_email = "jtkirk@starfleet.com",
    passwd = hash_pw
)
db.session.add(add)

# add2 = Users(
#     user_first_name = "Spock",
#     user_middle_name = "Pointy Ears",
#     user_last_name = "Spock",
#     user_email = "spock@starfleet.com",
#     passwd = hash_pw
# )
# db.session.add(add2)

# add3 = Users(
#     user_first_name = "Montgumery",
#     user_middle_name = "scotty",
#     user_last_name = "scot",
#     user_email = "scotty@starfleet.com",
#     passwd = hash_pw
# )
# db.session.add(add3)

# add4 = Users(
#     user_first_name = "Christine",
#     user_middle_name = "Nurse",
#     user_last_name = "Chapple",
#     user_email = "cchapple@starfleet.com",
#     passwd = hash_pw
# )
# db.session.add(add4)

db.session.commit()