from flask_wtf import FlaskForm
from models import Main
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from flask import session
from models import dbb

class RegisterForm(FlaskForm):
    # 아이디 중복 체크를 하는 코드
    class DuplicatIdCheck(object):
        def __init__(self, message=None):
            self.message = message
        def __call__(self, form, field):
            id = field.data
            sameid = Main.query.filter_by(id=id).first()
            if sameid:
                raise ValueError('  !이미 존재하는 아이디입니다.')

    id = StringField('id', validators=[DataRequired(), DuplicatIdCheck()])
    pw = PasswordField('pw', validators=[DataRequired()])


class LoginForm(FlaskForm):
    class PasswordCheck(object):
        def __init__(self, message=None):
            self.message = message
        def __call__(self,form,field):
            id = form['id'].data
            pw = field.data
            main = Main.query.filter_by(id=id).first()
            if main !=None:
                if  main.pw != pw:
                    raise ValueError('  잘못된 아이디나 비밀번호입니다.')
                else:
                    session['id'] = id
                    for_uid = dbb.session.query(Main.u_id).filter(Main.id == session['id']).all()
                    u_id = ''
                    for what in for_uid:
                        u_id = what[0]
                    session['u_id'] = u_id
            else:
                raise ValueError('  잘못된 아이디나 비밀번호입니다.')

    id = StringField('id', validators=[DataRequired()])
    pw = PasswordField('pw', validators=[DataRequired(), PasswordCheck()])


class QuizForm(FlaskForm):
    user_an = StringField('user_an',validators=[DataRequired()])

class BoardForm(FlaskForm):
    subject = StringField('subject', validators=[DataRequired()])
    contents = StringField('contents', validators=[DataRequired()])