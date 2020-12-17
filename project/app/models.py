from app import db


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('goal_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.id', ondelete='CASCADE'))
    goal = db.relationship('Goal', backref=db.backref('attendance_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('attendance_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

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