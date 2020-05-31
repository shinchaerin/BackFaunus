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
    def __repr__(self):
        return f"<Main ('{self.u_id}','{self.id}','{self.score_a}','{self.score_b}','{self.score_m}','{self.score_r}')>"

class Quiz(dbb.Model):
    __tablename__ = 'quiz'
    number = dbb.Column(dbb.Integer, primary_key=True, autoincrement=True)
    question = dbb.Column(dbb.String(200))
    answer = dbb.Column(dbb.String(100))
    first = dbb.Column(dbb.String(100))
    second = dbb.Column(dbb.String(100))
    third = dbb.Column(dbb.String(100))
    fourth = dbb.Column(dbb.String(100))
    kind = dbb.Column(dbb.String(50))
    def as_dict(self):
        return{x.name:getattr(self,x.name) for x in self.__table__.columns}
    def __repr__(self):
        return '<Quiz %r %r %r %r %r %r %r %r >' % (self.number, self.question, self.answer, self.first, self.second, self.third, self.fourth, self.kind)

class Board(dbb.Model):
    __tablename__ = 'board'
    board_id = dbb.Column(dbb.Integer, primary_key=True, autoincrement=True)
    subject = dbb.Column(dbb.String(100))
    contents = dbb.Column(dbb.String)
    u_id = dbb.Column(dbb.Integer, ForeignKey('main.u_id'))
    w_date = dbb.Column(dbb.TIMESTAMP)
    views = dbb.Column(dbb.Integer)
    heart = dbb.Column(dbb.Integer)

    def __init__(self, subject, contents):
        self.subject = subject
        self.contents = contents

    def __repr__(self):
        return '<Board %r %r %r %r %r %r %r>' % (self.board_id, self.subject, self.contents, self.u_id, self.w_date, self.views, self.heart)

class Answer(dbb.Model):
    __tablename__ = 'answer'

    a_id = dbb.Column(dbb.Integer, primary_key=True, autoincrement=True)
    user_an = dbb.Column(dbb.String(100))
    u_id = dbb.Column(dbb.Integer, ForeignKey('main.u_id'))
    q_id = dbb.Column(dbb.Integer, ForeignKey('quiz.number'))
    t_an = dbb.Column(dbb.String, ForeignKey('quiz.answer'))
    def __repr__(self):
        return '<Answer %r %r %r %r %r>' % (self.a_id, self.user_an, self.u_id, self.q_id, self.t_an)