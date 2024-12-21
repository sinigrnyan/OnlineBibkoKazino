from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    cardNumber = db.Column(db.String(150), unique=True)
    securityCode= db.Column(db.Integer)
    expirationDateMonth=db.Column(db.Integer)
    expirationDateYear=db.Column(db.Integer)
    Bibki= db.Column(db.Integer)

