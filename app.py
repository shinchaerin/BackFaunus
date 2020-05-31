from flask import Flask, render_template, redirect, request, url_for, session
from models import dbb #sqlAlchemy용
from models import Main
from models import Quiz
from models import Answer
from models import Board
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from forms import RegisterForm, LoginForm, AnswerForm
app = Flask(__name__)
engine = create_engine('mysql://root:tls0058243@localhost/faunus')
Session = sessionmaker(bind=engine)
dbsession = Session()
Base = declarative_base()

@app.route('/')
def root():
    if 'id' in session: #세션 내에 email이 있는지 확인
        return redirect('/main')
    else:
        return render_template('index.html')

@app.route('/main', methods=['GET','POST'])
def main():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
        return render_template('main.html',id=id)
    else:
        return redirect('/')

@app.route('/login', methods=['GET','POST'])
def login():
    rform = RegisterForm()
    if rform.validate_on_submit():
        user = Main()
        user.id = rform.data.get('id')
        user.pw = rform.data.get('pw')

        print(user.id, user.pw)  # 콘솔 확인용

        dbb.session.add(user)
        dbb.session.commit()

        return redirect('/login')


    lform = LoginForm()

    if lform.validate_on_submit():
        session['id'] = lform.data.get('id')

        return redirect('/main')

    return render_template('login.html', rform=rform, lform=lform)

@app.route('/logout',methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

# birds 정보

@app.route('/birds/parrot', methods=['GET','POST'])
def parrot():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/parrot.html', id=id)

@app.route('/birds/owl', methods=['GET','POST'])
def owl():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/owl.html', id=id)

@app.route('/birds/hummingbird', methods=['GET','POST'])
def hummingbird():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/hummingbird.html', id=id)

@app.route('/birds/paradisaeidae', methods=['GET','POST'])
def paradisaeidae():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/paradisaeidae.html', id=id)

@app.route('/birds/swallow', methods=['GET','POST'])
def swallow():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/swallow.html', id=id)

@app.route('/birds/woodpecker', methods=['GET','POST'])
def woodpecker():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/woodpecker.html', id=id)

@app.route('/birds/commonheron', methods=['GET','POST'])
def commonheron():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/commonheron.html', id=id)

@app.route('/birds/copper', methods=['GET','POST'])
def copper():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/copper.html', id=id)

@app.route('/birds/kingfisher', methods=['GET','POST'])
def kingfisher():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/kingfisher.html', id=id)

@app.route('/birds/flamingos', methods=['GET','POST'])
def flamingos():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('birds/flamingos.html', id=id)







# birds 퀴즈

@app.route('/birdsQuiz/birdsQuiz1', methods=['GET', 'POST'])
def birdsQuiz1():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

    #문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind=='birds',Quiz.number=='1')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '1')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz1.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz2', methods=['GET', 'POST'])
def birdsQuiz2():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '2')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '2')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)

    return render_template('/birdsQuiz/birdsQuiz2.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz3', methods=['GET', 'POST'])
def birdsQuiz3():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '3')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '3')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz3.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz4', methods=['GET', 'POST'])
def birdsQuiz4():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '4')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '4')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz4.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz5', methods=['GET', 'POST'])
def birdsQuiz5():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '5')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '5')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz5.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz6', methods=['GET', 'POST'])
def birdsQuiz6():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '6')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '6')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
        # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz6.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz7', methods=['GET', 'POST'])
def birdsQuiz7():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '7')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '7')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
        # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz7.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz8', methods=['GET', 'POST'])
def birdsQuiz8():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '8')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '8')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz8.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz9', methods=['GET', 'POST'])
def birdsQuiz9():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '9')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '9')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz9.html', quiz=quiz, id=id)

@app.route('/birdsQuiz/birdsQuiz10', methods=['GET', 'POST'])
def birdsQuiz10():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'birds', Quiz.number == '10')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '10')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer# u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer() # 만약 u_id를 비교했을 때 이 문제를 한 번도 풀어보지 않은 유저라면 새 객체를 만들어 주는 코드
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/birdsQuiz/birdsQuiz10.html', quiz=quiz, id=id)






# mammalia 정보

@app.route('/mammalia/arcticfox', methods=['GET','POST'])
def arcticfox():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/arcticfox.html', id=id)

@app.route('/mammalia/squirrel', methods=['GET','POST'])
def squirrel():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/squirrel.html', id=id)

@app.route('/mammalia/spectacledbear', methods=['GET','POST'])
def spectacledbear():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/spectacledbear.html', id=id)

@app.route('/mammalia/thompsongazelle', methods=['GET','POST'])
def thompsongazelle():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/thompsongazelle.html', id=id)

@app.route('/mammalia/inermis', methods=['GET','POST'])
def inermis():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/inermis.html', id=id)

@app.route('/mammalia/baboon', methods=['GET','POST'])
def baboon():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/baboon.html', id=id)

@app.route('/mammalia/sloth', methods=['GET','POST'])
def sloth():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/sloth.html', id=id)

@app.route('/mammalia/jaguar', methods=['GET','POST'])
def jaguar():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/jaguar.html', id=id)

@app.route('/mammalia/raccoondog', methods=['GET','POST'])
def raccoondog():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/raccoondog.html', id=id)

@app.route('/mammalia/marten', methods=['GET','POST'])
def marten():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/mammalia/marten.html', id=id)



# mammalia 퀴즈

@app.route('/mammaliaQuiz/mammaliaQuiz1', methods=['GET', 'POST'])
def mammaliaQuiz1():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '11')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '11')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz1.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz2', methods=['GET', 'POST'])
def mammaliaQuiz2():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '12')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '12')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz2.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz3', methods=['GET', 'POST'])
def mammaliaQuiz3():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '13')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '13')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz3.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz4', methods=['GET', 'POST'])
def mammaliaQuiz4():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '14')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '14')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz4.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz5', methods=['GET', 'POST'])
def mammaliaQuiz5():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '15')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '15')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz5.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz6', methods=['GET', 'POST'])
def mammaliaQuiz6():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '16')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '16')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz6.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz7', methods=['GET', 'POST'])
def mammaliaQuiz7():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '17')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '17')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz7.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz8', methods=['GET', 'POST'])
def mammaliaQuiz8():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '18')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '18')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz8.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz9', methods=['GET', 'POST'])
def mammaliaQuiz9():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '19')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '19')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz9.html', quiz=quiz, id=id)

@app.route('/mammaliaQuiz/mammaliaQuiz10', methods=['GET', 'POST'])
def mammaliaQuiz10():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'mammalia', Quiz.number == '20')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '20')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/mammaliaQuiz/mammaliaQuiz10.html', quiz=quiz, id=id)





# reptile 정보

@app.route('/reptile/basilisklizard', methods=['GET','POST'])
def basilisklizard():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/basilisklizard.html', id=id)

@app.route('/reptile/blackmamba', methods=['GET','POST'])
def blackmamba():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/blackmamba.html', id=id)

@app.route('/reptile/inlandtaipan', methods=['GET','POST'])
def inlandtaipan():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/inlandtaipan.html', id=id)

@app.route('/reptile/greentreepython', methods=['GET','POST'])
def greentreepython():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/greentreepython.html', id=id)

@app.route('/reptile/saltwatercrocodile', methods=['GET','POST'])
def saltwatercrocodile():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/saltwatercrocodile.html', id=id)

@app.route('/reptile/nilecrocodile', methods=['GET','POST'])
def nilecrocodile():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/nilecrocodile.html', id=id)

@app.route('/reptile/dwarfcrocodile', methods=['GET','POST'])
def dwarfcrocodile():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/dwarfcrocodile.html', id=id)

@app.route('/reptile/galapagostortoise', methods=['GET','POST'])
def galapagostortoise():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/galapagostortoise.html', id=id)

@app.route('/reptile/leopardtortoise', methods=['GET','POST'])
def leopardtortoise():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/leopardtortoise.html', id=id)

@app.route('/reptile/hornedlizard', methods=['GET','POST'])
def hornedlizard():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/reptile/hornedlizard.html', id=id)


# reptile 퀴즈

@app.route('/reptileQuiz/reptileQuiz1', methods=['GET', 'POST'])
def reptileQuiz1():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '21')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '21')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz1.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz2', methods=['GET', 'POST'])
def reptileQuiz2():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '22')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '22')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz2.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz3', methods=['GET', 'POST'])
def reptileQuiz3():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '23')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '23')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz3.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz4', methods=['GET', 'POST'])
def reptileQuiz4():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '24')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '24')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz4.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz5', methods=['GET', 'POST'])
def reptileQuiz5():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '25')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '25')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz5.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz6', methods=['GET', 'POST'])
def reptileQuiz6():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '26')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '26')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz6.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz7', methods=['GET', 'POST'])
def reptileQuiz7():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '27')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '27')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz7.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz8', methods=['GET', 'POST'])
def reptileQuiz8():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '28')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '28')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz8.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz9', methods=['GET', 'POST'])
def reptileQuiz9():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '29')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '29')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz9.html', quiz=quiz, id=id)

@app.route('/reptileQuiz/reptileQuiz10', methods=['GET', 'POST'])
def reptileQuiz10():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'reptile', Quiz.number == '30')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '30')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/reptileQuiz/reptileQuiz10.html', quiz=quiz, id=id)





# amphibia 정보

@app.route('/amphibia/bullfrog', methods=['GET','POST'])
def bullfrog():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/bullfrog.html', id=id)

@app.route('/amphibia/toad', methods=['GET','POST'])
def toad():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/toad.html',id=id)

@app.route('/amphibia/treefrog', methods=['GET','POST'])
def treefrog():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/treefrog.html', id=id)

@app.route('/amphibia/pelophylax', methods=['GET','POST'])
def pelophylax():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/pelophylax.html', id=id)

@app.route('/amphibia/leopardfrog', methods=['GET','POST'])
def leopardfrog():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/leopardfrog.html', id=id)

@app.route('/amphibia/glandirana', methods=['GET','POST'])
def glandirana():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/glandirana.html', id=id)

@app.route('/amphibia/narrowmouthfrog', methods=['GET','POST'])
def narrowmouthfrog():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/narrowmouthfrog.html', id=id)

@app.route('/amphibia/newt', methods=['GET','POST'])
def newt():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/newt.html', id=id)

@app.route('/amphibia/salamander', methods=['GET','POST'])
def salamander():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/salamander.html', id=id)

@app.route('/amphibia/ranaamurensis', methods=['GET','POST'])
def ranaamurensis():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/amphibia/ranaamurensis.html', id=id)




# amphibia 퀴즈

@app.route('/amphibiaQuiz/amphibiaQuiz1', methods=['GET', 'POST'])
def amphibiaQuiz1():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '31')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '31')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz1.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz2', methods=['GET', 'POST'])
def amphibiaQuiz2():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '32')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '32')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz2.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz3', methods=['GET', 'POST'])
def amphibiaQuiz3():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '33')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '33')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz3.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz4', methods=['GET', 'POST'])
def amphibiaQuiz4():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '34')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '34')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz4.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz5', methods=['GET', 'POST'])
def amphibiaQuiz5():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '35')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '35')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz5.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz6', methods=['GET', 'POST'])
def amphibiaQuiz6():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '36')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '36')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz6.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz7', methods=['GET', 'POST'])
def amphibiaQuiz7():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '37')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '37')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz7.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz8', methods=['GET', 'POST'])
def amphibiaQuiz8():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '38')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '38')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz8.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz9', methods=['GET', 'POST'])
def amphibiaQuiz9():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '39')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '39')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz9.html', quiz=quiz, id=id)

@app.route('/amphibiaQuiz/amphibiaQuiz10', methods=['GET', 'POST'])
def amphibiaQuiz10():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)

        # 문제 보여주기
        quiz = Quiz.query.filter(and_(Quiz.kind == 'amphibia', Quiz.number == '40')).first()
        an_id = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id == '40')).first()

        if an_id:
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                an_id.user_an = user_answer  # u_id가 이 문제를 풀어본 적이 있는지 비교하는 코드 -> 있을 때 초기화하는 게 아니라 저장해야 하는 ㄱ
                dbb.session.commit()
                print(an_id)
        else:
            answer = Answer()
            # 사용자 값 받아오기
            if request.method == 'POST':
                user_answer = request.form['gtpQ']
                answer.user_an = user_answer
                answer.u_id = u_id
                answer.q_id = quiz.number
                answer.t_an = quiz.answer
                dbb.session.add(answer)
                dbb.session.commit()
                print(answer)
    return render_template('/amphibiaQuiz/amphibiaQuiz10.html', quiz=quiz, id=id)





#채점 파트

@app.route('/grade/<int:kind>', methods=['GET', 'POST'])
def grade(kind=None):
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        answer = Answer.query.filter(and_(Answer.u_id == u_id, Answer.q_id >= kind * 10 + 1, Answer.q_id <= kind * 10 + 10)).all()
        user = Main.query.filter(Main.u_id == u_id).first()  # 하나만 불러오려면(찾으려면) first() -> 아니면 all()
        score = 0

        for i in answer:
            if i.user_an == i.t_an:
                score = score+10
            print(score)

        if kind == 0:
            user.score_b = score
            dbb.session.commit()
            print(user.score_b)

        elif kind == 1:
            user.score_m = score
            dbb.session.commit()
            print(user.score_m)

        elif kind == 2:
            user.score_r = score
            dbb.session.commit()
            print(user.score_r)

        else:
            user.score_a = score
            dbb.session.commit()
            print(user.score_a)

        return render_template('quizresult.html', id=id, answer=answer, kind=kind, score=score)




# 게시글

@app.route('/bulletinboard', methods=['GET','POST'])
def bulletinboard():
    if 'id' in session: #세션 내에 email이 있는지 확인
        id = session.get('id', None)
    return render_template('/bulletinboard.html', id=id)


@app.route('/write', methods=['POST', 'GET'])
def write():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
        print(u_id)
        if request.method == 'POST':
            board = Board(request.form['subject'], request.form['contents'])
            board.u_id = u_id
            board.views = 0
            board.heart = 0
            dbb.session.add(board)
            dbb.session.commit()
            return redirect(url_for('all'))

    return render_template('write.html')

# 게시글 조회
@app.route('/show')
def all():
    if 'id' in session:
        id = session.get('id', None)
        u_id = session.get('u_id')
    board = Board.query.all()
    return render_template('showboard.html', board=board)

# 게시글 수정
@app.route('/edit/<int:bid>', methods=['POST', 'GET'])
def edit(bid):
    # if 'id' in session:
    #     #todo: board의 u_id가 세션의 u_id와 같은지.
    #     u_id = session.get('u_id')
    board = Board.query.get(bid)
    if request.method == 'POST':
        board.subject = request.form['subject']
        board.contents = request.form['contents']
        dbb.session.commit()
        return redirect(url_for('all'))

    return render_template('edit.html', board=board)

# 게시글 삭제
@app.route('/delete/<int:bid>', methods=['POST', 'GET'])
def delete(bid):
    board = Board.query.get(bid)
    dbb.session.delete(board)
    dbb.session.commit()

    return redirect(url_for('all'))




if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cpt:tls0058243@localhost/faunus' ##서버의 db설정으로 변경 필요
                                                    #데베유저이름:데베비번@localhost/데베이름(faunus)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = 'fewgjhgegfdglkjwnkfsd'

    #csrf 위변조 공격을 막기위한 코드
    csrf = CSRFProtect()
    CSRFProtect(app)
    csrf.init_app(app)

    dbb.init_app(app)
    dbb.app = app
    dbb.create_all()  # SQLAlchemy 이용한 db 생성
    app.run(host='127.0.0.1', port=5000, debug=True) #local에서 테스트 할때는 '127.0.0.1'로.