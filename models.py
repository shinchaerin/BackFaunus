#DB
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

dbb = SQLAlchemy()

class Main(dbb.Model):
    __tablename__='main'
    u_id = dbb.Column(dbb.Integer, primary_key = True, autoincrement=True)
    id = dbb.Column(dbb.String(50), unique=True)  # ID
    pw = dbb.Column(dbb.String(50))
    score_a = dbb.Column(dbb.Integer)
    score_b = dbb.Column(dbb.Integer)
    score_m = dbb.Column(dbb.Integer)
    score_r = dbb.Column(dbb.Integer)


class Quiz(dbb.Model):
    __tablename__ = 'quiz'
    number = dbb.Column(dbb.Integer, primary_key=True, autoincrement=True)
    question = dbb.Column(dbb.String(200))
    answer = dbb.Column(dbb.String(100))
    user_an = dbb.Column(dbb.String(100))
    kind = dbb.Column(dbb.String(50))

class Board(dbb.Model):
    __tablename__ = 'board'
    board_id = dbb.Column(dbb.Integer, primary_key=True, autoincrement=True)
    subject = dbb.Column(dbb.String(100))
    contents = dbb.Column(dbb.String)
    u_id = dbb.Column(dbb.Integer, ForeignKey('main.u_id'))
    w_date = dbb.Column(dbb.TIMESTAMP)
    views = dbb.Column(dbb.Integer)
    heart = dbb.Column(dbb.Integer)