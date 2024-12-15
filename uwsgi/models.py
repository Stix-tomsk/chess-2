from datetime import datetime
from app import db
from utils import hash


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    token = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)
    
    def __init__(self, username, password, token='', is_admin=False):
        self.username = username
        self.password = password
        self.token = token
        self.is_admin = is_admin

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    @staticmethod
    def create(username, password, token='', is_admin=False):
        user = User(username, hash(password), token, is_admin)
        db.session.add(user)
        db.session.commit()
        
        return user

class Score(db.Model):
    __tablename__ = 'score'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer)
    date = db.Column(db.Time)
    
    def __init__(self, user, value, date=datetime.now()):
        self.user = user
        self.value = value
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String())
    winner = db.Column(db.Integer)
    loser = db.Column(db.Integer)
    last_turn = db.Column(db.Integer)
    end = db.Column(db.Time)
    
    def __init__(self, status, winner, loser, last_turn=None, end=None):
        self.status = status
        self.winner = winner
        self.loser = loser
        self.last_turn = last_turn
        self.end = end

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class Turn(db.Model):
    __tablename__ = 'turn'

    id = db.Column(db.Integer, primary_key=True)
    match = db.Column(db.Integer)
    user = db.Column(db.Integer)
    figure = db.Column(db.Integer)
    move_from = db.Column(db.Integer)
    move_to = db.Column(db.Integer)
    date = db.Column(db.Time)
    
    def __init__(self, match, user, figure, move_from, move_to, date=datetime.now()):
        self.match = match
        self.user = user
        self.figure = figure
        self.move_from = move_from
        self.move_to = move_to
        self.date = date

    def __repr__(self):
        return '<id {}>'.format(self.id)