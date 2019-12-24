from flask import Flask, escape, url_for,flash,redirect
from flask import render_template
from flask import request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

# Build a form for login
class Login_Form(FlaskForm):
    # todo
    email = StringField('Email',validators=[
        DataRequired(message='email address can not be empty.'),Length(1,64),
        Email(message='please enter a good email address')
    ])
    password = PasswordField('Password',validators=[DataRequired(message='Password can not be empty.')])
    submit = SubmitField('Login')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET','POST'])
@app.route('/index')
@app.route('/omg')
def index():

    if request.method == 'POST':  # 判断是否是 POST 请求
        print(request.form['person'])
        print(request.args)
        # 获取表单数据
        # title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        # year = request.form.get('year')
        # 验证数据
        return redirect(url_for('index',title=request.form['person'],year=request.form['phone']))  # 重定向回主页

    return render_template('temp.html')


@app.route('/user/<user_name>')
def profile(user_name):
    return 'user name: {}'.format(escape(user_name))

@app.route('/login',methods=['GET','POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        print('the user login now!')
        print(form.email._value)
        print(form.password)
    return render_template('login.html',form=form)

@app.route('/project/<project>')
def show_project(project):
    return 'The page of Project {}'.format(project)

@app.route('/about')
def show_about():
    return 'The about page.'

@app.route('/request/')
def get_request():
    return request.args.get('info')


@app.route('/login2', methods=['POST', 'GET'])
def login2():
    error = None
    if request.method == 'POST':
        return request.form['username'] + request.form['password']
    else:
        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login2.html', error=error)


with app.test_request_context():
    print('index: ',url_for('index'))
    print('login: ',url_for('login'))
    print('/:',url_for('login', next='/'))
    print('profile: ',url_for('profile', user_name='John Doe'))




if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1',port=8080)

