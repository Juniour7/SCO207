from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    destination = db.Column(db.String(1000))
    item= db.Column(db.String(1000))
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150))
    name = db.Column(db.String(150))
    people = db.Column(db.Integer)
    rdate = db.Column(db.String(1000))
    rtime= db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    orders = db.relationship('Order')
    reservations = db.relationship('Reservation')