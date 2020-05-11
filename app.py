from flask import Flask, render_template, redirect, request, url_for, session
from models import dbb #sqlAlchemy용
from models import Main
from models import Quiz
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm, QuizForm
app = Flask(__name__)

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
        u_id = session.get('u_id', None)
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
        session['u_id'] = lform.data.get('u_id')

        return redirect('/main')

    return render_template('login.html', rform=rform, lform=lform)

@app.route('/logout',methods=['GET'])
def logout():
    session.clear()
    return redirect('/')



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





# @app.route('/question', methods=['GET','POST'])
# def db_insert_q():
#     if 'id' and 'u_id' not in session:
#         return redirect('/')
#     form = QuizForm()
#
#     if form.validate_on_submit():
#         question = Quiz()
#         question.user_an = form.data.get('user_an')
#         dbb.session.add(question)
#         dbb.session.commit()
#         return render_template('qeustion_success.html', id = session['id'] )
#     return render_template('question_make.html', form = form, id= session['id'])


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

