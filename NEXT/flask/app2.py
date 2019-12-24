from flask import Flask, url_for, render_template
from flask import request,flash

app = Flask(__name__)
app.secret_key = 'dev'

@app.route('/',methods=['GET','POST'])
def hello():
    
    flash('hohohoho,it is flash')

    if request.method == 'POST':
        # get form data
        title = request.form.get('title')
        year = request.form.get('year')
        print('path: {}'.format(request.path))
        print('The request method is {}'.format(request.method))
        return '<h1>Title: {}, Year: {}</h1>'.format(title, year)
    url_hello = url_for('static',filename='images/totoro.gif')
    print(url_hello)
    title = 'Temp'
    year = 2000
    return render_template('index.html',title=title,year=year)

@app.route('/user/<name>')
def user_page(name):
    return '<h2>This is User: {}</h2>'.format(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='Jim'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test Page'

@app.errorhandler(404)
def page_not_found(e):
    user = 'Jim'
    return render_template('404.html',user=user), 404

if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1',port=8080)
