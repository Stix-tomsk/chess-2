from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String())
    password = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Score(db.Model):
    __tablename__ = 'score'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer())
    value = db.Column(db.Integer())
    date = db.Column(db.Datetime())

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String())
    winner = db.Column(db.Integer())
    loser = db.Column(db.Integer())
    last_turn = db.Column(db.Integer())
    end = db.Column(db.Datetime())

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class Turn(db.Model):
    __tablename__ = 'turn'

    id = db.Column(db.Integer, primary_key=True)
    match = db.Column(db.Integer())
    user = db.Column(db.Integer())
    figure = db.Column(db.Integer())
    move_from = db.Column(db.Integer())
    move_to = db.Column(db.Integer())
    date = db.Column(db.Datetime())

    def __repr__(self):
        return '<id {}>'.format(self.id)