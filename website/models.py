from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    email_v = db.Column(db.Integer)
    
class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(100))
    district = db.Column(db.String(100))
    soil = db.Column(db.String(100))
    address = db.Column(db.String(100))
    owner_id = db.Column(db.Integer)
    land_area = db.Column(db.Float)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer)
    plant_name = db.Column(db.String(100))