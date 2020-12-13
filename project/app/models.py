from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class UserRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Relating = db.Column(db.Integer, nullable=False)
    Related = db.Column(db.Integer, nullable=False)
    Type = db.Column(db.Integer, nullable=False)
    Relating_name = db.Column(db.String(100),  nullable=True, server_default='1')
    Related_name = db.Column(db.String(100),  nullable=True, server_default='1')